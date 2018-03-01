# -*- coding: utf-8 -*-
#a lot of credit goes to:
#    http://bdewilde.github.io/blog/2014/09/23/intro-to-automatic-keyphrase-extraction/
import pandas as pd
import numpy as np
import itertools, nltk, re, os, docx, unicodedata, pickle
#If you've never setup nltk previously, execute the following line
#nltk.download()

#todo: currently use first 6 letters of DOCX to determine id. Expecting "DSI-06" to be the name
#   Currently hard-coded to read [0:6]. This will break once DSI passes 100.
#   DSI-100 will overwrite DSI-10. Add logic to get full DSI name. Or just skip
#   naming by the file, and simply assign your own number by order read in

def main():
    corpus_path = "C:/temp/NU/453/CS2/" #location where all corpus .docx files are stored
    output_path = "C:/temp/NU/453/output/" #location you will output all CSV files
    pickle_path = "C:/temp/NU/453/pickle/" #where do you want to read / write the phrase list / filters, etc.

    #use phrase_dict.py, ec_dict.py, concept_dict.py, and filter_words.py to create dictionaries
    try:
        phrase_dict = pickle.load(open(pickle_path + 'phrase_dict.p', 'rb'))
        ec_dict = pickle.load(open(pickle_path + 'ec_dict.p', 'rb'))
        filter_words = pickle.load(open(pickle_path + 'filter_words.p', 'rb'))
        concept_dict = pickle.load(open(pickle_path + 'concept_dict.p', 'rb'))
    except IOError:
        print('Error opening dictionary file, confirm directory and pickle files exist')
        return
    
    return make_magic_happen(corpus_path, output_path, phrase_dict, ec_dict, filter_words, concept_dict)


#===========================================================
#               Helper functions
#===========================================================
def lambda_unpack(f):
    return lambda args: f(*args)

#============System to chunk individual terms into phrases ===================
def extract_candidate_chunks(text, filter_words, grammar=r'KT: {(<NN.*>+)? <NN.*>+}'):
    #strip_text = re.sub(r"[^\-\,\.\?\!\'\(\)\w\d'\s]+",'',text) #remove unicode characters
    #strip_text = re.sub(r"[^\'\!\"\#\$\&\\\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\\\]\^\_\`\{\|\}\~\'\w\d'\s]+",'',text) #removes unicode punctuation 
    #Note: I no longer strip all unicode characters. unicodedata helpfully does a "best near match" with ascii
    strip_text = unicodedata.normalize('NFKD', text).encode('ascii','ignore').decode('utf-8')
    #Note: now I leave all punctuation to aid with sentence tokenization
    stop_words = set(nltk.corpus.stopwords.words('english'))
    stop_words |= filter_words
    
    # tokenize, POS-tag, and chunk using regular expressions
    #todo: currently the grammar chunker noun-strings strings possessives, "trump's plan" --> "trumps plan"
    #   ideally, that should be two tokens, "trump" and "plan". Without this change you get a lot of
    #   "floater" terms unlikley to pair up. For example, if Trump was always used in a possessive, like
    #   "donald trump's trade plan", or "donald trump's rhetoric", then you'd never match with the term for just "trump".
    #   In an ideal solution, you'd keep ALL three, "donald trump" and "trade plan", and "donald trumps trade plan"
    #   in that way you'd correctly associate with "donald trump", as well as a loose association with an article on
    #   obama's "trade plan", and then a very strong link with any article also discusing "donald trumps trade plan".
    chunker = nltk.chunk.regexp.RegexpParser(grammar)
    tagged_sents = nltk.pos_tag_sents(nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(strip_text))
    all_chunks = list(itertools.chain.from_iterable(nltk.chunk.tree2conlltags(chunker.parse(tagged_sent))
                                                    for tagged_sent in tagged_sents))

    candidates = [' '.join(nltk.stem.WordNetLemmatizer().lemmatize(word.lower().strip()) for word, pos, chunk in group)
        for key, group in itertools.groupby(all_chunks, lambda_unpack(lambda word, pos, chunk: chunk != 'O')) if key]
    
    #We had left standard punctuation to aid in sentence chunking. Now delete all intra-word punctuation. "f.b.i. --> "fbi"
    for idx in range(len(candidates)):
        candidates[idx] = re.sub(r"[!\"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]", '', candidates[idx])
    #Did not use string.punctuation, since we need to escape the [brackets] for re.sub
    
    return [cand.strip() for cand in candidates if cand not in stop_words]
    #strip again, because filtering punctuation above may re-introduce floating spaces, "% people" --> " people"

#==========Take a single long string of text and convert it into terms / phrases========
def parse_article(dsi_text, phrase_dict, ec_dict, filter_words, grammar=r'KT: {(<NN.*>+)? <NN.*>+}'):
    dsi_sentences = nltk.sent_tokenize(dsi_text)
    ec_text = ""
    insensitive_phrase = ""
    #Before processing, let's capture combinatory-word-phrases to avoid incorrect splitting
    #   e.g., "Cash for guns" --> "cashForGuns", to prevent "cash" and "guns" indivudually
    #   Currently very wasteful iteration, done for readability. If you build a large corpus and phrase dictionaries
    #   You'd be well serviced to optimize this implementation.
    for sentence in dsi_sentences:
        for phrase, ec in phrase_dict.items():
            if phrase.lower() in sentence.lower():
                #case insenstive matching, so that "CAsh For GUNS" will equal "cash for guns"
                insensitive_phrase = re.compile(re.escape(phrase), re.IGNORECASE)
                sentence = insensitive_phrase.sub(ec, sentence)         
        ec_text += ' ' + sentence
    del sentence, phrase, ec, insensitive_phrase
    #Now that EC swapping is complete, let's chunk the terms
    chunked_list = extract_candidate_chunks(ec_text, filter_words, grammar)
    #We now have a series of all terms, in lower case. Now let's swap out EC terms

    chunked_series = pd.Series(chunked_list)
    chunked_series.replace(to_replace=ec_dict, inplace=True)
    
    return pd.DataFrame(chunked_series, columns=['terms'])

#===========================================================
#               True main program
#===========================================================

def make_magic_happen(corpus_path, output_path, phrase_dict, ec_dict, filter_words, concept_dict):

    corpus = []
    file_list = [f for f in os.listdir(corpus_path) if os.path.isfile(os.path.join(corpus_path, f))]
    
    #Let's open all DSI, and append the text of each to a list
    try:
        for f in file_list:
            document = docx.Document(corpus_path+f)
            dsi_text = ""
            #Luckily, PRED453 DOCX template has metadata in a table, and the paragraphs functions will skip it
            for p in document.paragraphs:
                dsi_text += ' ' + p.text
                #You may want to add a '.' to the space above. Section title tend to not have punctuation. It could create false sentences.
            corpus.append(dsi_text)
        del f, p, document, dsi_text
    except IOError:
        print('Error reading corpus DSI docx files')
        return
    #corpus now contains all raw text of all DSIs, each article as a solid string.
    
    #Next, let's parse each article into grammar chunks, phrases, and terms
    
    #Use the following to include adjectives and preposition / conjunction chunks
    #    e.g., automatically retain "cash for guns" rather than split, "cash", "guns"
    #    e.g., "dire days on Wall Street", rather than "dire days", "Wall Street"
    grammar_conjunctions = r'KT: {(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+}'
    #Use the following to include adjective modifiers
    #    e.g., "blue car" rather than just "car"
    grammar_adjectives = r'KT: {(<JJ>* <NN.*> <NN.*>+)? <JJ>* <NN.*>+}'
    #Only chunk noun-linked sections, this is the default option if you don't specify
    #    e.g., "bird house", or "emergency road flare"
    grammar_nouns = r'KT: {(<NN.*>+)? <NN.*>+}'
    
    #convert each string-of-text into a list comprised of DataFrame-of-terms
    corpus_phrases = []
    for dsi in corpus:
        corpus_phrases.append(parse_article(dsi, phrase_dict, ec_dict, filter_words, grammar_nouns))
        #replace above 'grammar_nouns' with your preferred chunker
    del dsi
    
    #gather all terms to build our "master" list of terms
    #create a new list of all dsi, and "pivot" on terms for total counts
    master = pd.DataFrame()
    corpus_term_counts = []
    for i in range(0, len(file_list)):
        corpus_phrases[i]['dsi'] = file_list[i][0:6]
        master = pd.concat([master, corpus_phrases[i]])
        corpus_term_counts.append(pd.DataFrame(corpus_phrases[i].terms.value_counts()))
        corpus_term_counts[i].columns = (['t_count'])
        corpus_term_counts[i].loc[:,'tf'] = 0.0
    del i
    
    #calculate term frequency for INDIVIDUAL DSI
    for i in range(0, len(corpus_term_counts)):
        dsi_num_terms = corpus_term_counts[i].t_count.sum()
        for term in corpus_term_counts[i].index:
            term_count = corpus_term_counts[i].loc[term].t_count
            corpus_term_counts[i].set_value(term,'tf',term_count / dsi_num_terms)
    del i,term, dsi_num_terms, term_count
    
    #The index is a mish-mash of each individual DSI. Rebuild it. (Not really necessary, just being pedantic)
    master = master.reset_index(drop=True)
    
    #count number TOTAL times a term occurs in whole corpus
    master_terms = master.terms.value_counts()
    
    term_loc_series = master.groupby(['terms','dsi']).size()
    
    masterdf_terms = pd.DataFrame(master_terms)
    masterdf_terms.columns=(['t_count'])
    masterdf_terms['concept'] = 'UNKNOWN'
    masterdf_terms['d_count'] = 0
    masterdf_terms.loc[:,'tf'] = 0.0
    masterdf_terms.loc[:,'idf'] = 0.0
    masterdf_terms.loc[:,'tf_idf'] = 0.0
    
    terms_in_corpus = sum(masterdf_terms['t_count'])
    
    #assign each term to it's concept class, if known
    #indexSr = pd.Series(masterdf_terms.index)
    indexSr = pd.Series(masterdf_terms.index).str.lower()
    for key, value in concept_dict.items():
        #must confirm the key actually exists as a term, or else it'd be shoe-horned in with blank row values
        
        #todo: major bug! "match" will return true if the BEGINNING matches, such that a search to
        #  match "hillary" will return TRUE if the set contains "hillaryClinton". Need to find way
        #  to match EXACT string, since above would kick an exception to write "hillary" if that
        #  exact key does not exist, even though "hillaryClinton" returned TRUE
        #  I want to avoid doing it with another 'for' loop, which would be an easy fix
        if(indexSr.str.match(key,case=False).any()):
            try: masterdf_terms.at[masterdf_terms.index[indexSr[indexSr==key].index[0]], 'concept'] = value
            except: print("error, key matched in search, but not in term index: \""+key+"\"")
    del indexSr
    
    #calcualte tf_idf statistics on the FULL SET
    for term in masterdf_terms.index:
        #count the number times term occurs in a DSI
        masterdf_terms.set_value(term,'d_count',len(term_loc_series[term]))
        #calculate tf = Term_Feq_Count / Total_Terms_In_Cohort
        term_count = masterdf_terms.loc[term]['t_count']
        masterdf_terms.set_value(term,'tf',term_count / terms_in_corpus)
        #calculate idf = LOG10(#DSI / d_count)
        num_dsi = len(corpus_phrases)
        masterdf_terms.set_value(term,'idf',np.log10(num_dsi / masterdf_terms.loc[term]['d_count'] ))
        #calculate tf*idf
        masterdf_terms.set_value(term,'tf_idf', masterdf_terms.loc[term]['tf'] * masterdf_terms.loc[term]['idf'] )
    del term, term_count, num_dsi
    
    
    
    #create the matrix of terms across each DSI
    for i in range(0, len(corpus_term_counts)):
        for term in corpus_term_counts[i].index:
            #masterdf_terms.set_value(term,file_list[i][0:6],corpus_term_counts[i]['t_count'][term])
            masterdf_terms.set_value(term,file_list[i][0:6],corpus_term_counts[i]['tf'][term])
    del i,term
    
    
    #First we pivot by concept, and sum all columns
    masterdf_concepts = masterdf_terms.groupby(['concept']).sum()
    #document count shouldn't be sum'd, we should max to find real doc count, fix those values.
    #   There is probably a better way to do this, but I'm bad with pivot logic!
    for concept in masterdf_concepts.index:
        #Ignore first 5 columns to only count # of items in the DSI's
        masterdf_concepts.set_value(concept, 'd_count', masterdf_concepts.loc[concept][5:].count())
    del concept
    
    
    #write the master matrix out to a CSV file
    masterdf_terms.to_csv(output_path+'master.csv')
    masterdf_concepts.to_csv(output_path+'master_concepts.csv')
    
    #write out all of the individual DSI to their own CSV
    for i in range(0, len(corpus_term_counts)):
        corpus_term_counts[i].to_csv(output_path + file_list[i][0:6] + '.csv')
        #todo: the above [0:6] will start overwriting DSI once we hit #100
        #     e.g., [DSI-12], would be overwritten by DSI-120 when it's pruned to 6 chars
        #     hack-fix: rename all past DSI as "DSI-027", then change 6 --> 7 (in all locations!)
    del i
    
    #return the primary dataframes to allow exploration in the var browser
    return (masterdf_terms, masterdf_concepts)
    
if __name__ == '__main__':
    (terms, concepts) = main()
