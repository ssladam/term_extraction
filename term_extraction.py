# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import itertools, nltk, re, os, docx, unicodedata
#If you've never setup nltk previously, execute the following line
#nltk.download()

corpus_path = "C:/Users/adams/OneDrive/Documents/Northwestern/453 - Text/CS2/" #location where all corpus .docx files are stored
output_path =   "C:/Users/adams/OneDrive/Documents/Northwestern/453 - Text/output/" #location you will output all CSV files

#Preprocessing, opportunity to replace words or phrases with ECs
#  DO NOT add "president" --> "presidentTrump" here, otherwise all instances
#  of "president obama" would be converted to "presidentTrump obama"
#  this should be used for fixed phrases ONLY
phrase_dict = {"Trans-Pacific Partnership": "TPP",\
            "North American Free Trade Agreement":"NAFTA",\
            "World Trade Organization":"WTO",\
            "fire and fury":"fireAndFury",\
            "lost jobs":"jobLosses",\
            "job losses":"jobLosses",\
            "chief of staff":"chiefOfStaff",\
            "E&E News":"EandENews",\
            "S&P 500":"SandP500",\
            "memorandum donald trump":"memorandum which donald trump",\
            "Immigration and Nationality Act":"immigrationAndNationalityAct",\
            "Club For Growth and Heritage":"clubForGrowthAndHeritage",\
            "Freedom Caucus":"freedomCaucus",\
            "Office of Personnel Management ":"officeOfPersonnel Management",\
            "Office of Management and Budget":"officeOfManagementAndBudget",\
            #Okay, I cheat just a bit by pre-filtering some terms that would be tricky to remove otherwise
            #   these terms become "nested" with other terms, easier to just axe them here
            "[sic]":"",\
            "percent":"",\
            "percentage":"",\
            
          }

#This will be swapped out after processing is complete, now you're safe to
#  swap out individual words for their EC equivalent
ec_dict = {'trump':'presidentDonaldTrump',\
               'president':'presidentDonaldTrump',\
               "us":"unitedStates",\
               "usa":"unitedStates",\
               "united states":"unitedStates",\
               "mr trump":"presidentDonaldTrump",\
               "mr trumps":"presidentDonaldTrump",\
               "president trump":"presidentDonaldTrump",\
               "president trumps":"presidentDonaldTrump",\
               "President Donald Trump":"presidentDonaldTrump",\
               "Donald Trump":"presidentDonaldTrump",\
               "president-elect donald trump":"presidentElectDonaldTrump",\
               "presidentelect donald trumps":"presidentElectDonaldTrump",\
               "presidentelect donald trump":"presidentElectDonaldTrump",\
               "presidentelect donald j trump":"presidentElectDonaldTrump",\
               "presidentelects":"presidentElectDonaldTrump",\
               "presidentelect":"presidentElectDonaldTrump",\
               "Melania Trump":"melaniaTrump",\
               "trumps":"presidentDonaldTrump",\
               "us president donald trump":"presidentDonaldTrump",\
               "fbi director james comey":"jamesComey",\
               "comey":"jamesComey",\
               "mr rosss":"wilburRoss",\
               "mr ross":"wilburRoss",\
               "commerce secretary wilbur ross":"wilburRoss",\
               "ross":"wilburRoss",\
               "sen dianne feinstein":"dianneFienstein",\
               "feinstein":"dianneFienstein",\
               "mueller":"robertMueller",\
               "robert mueller":"robertMueller",\
               "counsel robert mueller":"robertMueller",\
               "special counsel":"robertMueller",\
               "eu":"europeanUnion",\
               "european union":"europeanUnion",\
               "white house press secretary sarah huckabee sanders":"sarahHuckabeeSanders",\
               "trump administration":"trumpAdministration",\
               "united nations":"unitedNations",\
               "un":"unitedNations",\
               "ina":"immigrationAndNationalityAct",\
               "south korea":"southKorea",\
               "south koreas":"southKorea",\
               "ocare":"obamacare",\
               "russias":"russia",\
               "tariffs":"tariff",\
               "us tariff":"tariff",\
               "percent tariff":"tariff",\
               "tariff hike":"tariff"

               
               }
#the parser converts all entries to lower case, so we should do the same
ec_dict = {key.lower(): value for key, value in ec_dict.items()}


#add all words you want to filter into filter_words, this also occurs POST PROCESSING, so now if you filter
#  the term "friday" it will drop that singular term, but WOULD NOT filter "friday night" since it doesn't match
filter_words = set()
filter_words.update(['year', 'week', 'month', 'day', 'hour', 'minute', 'time','past','morning','afternoon', 'evening', 'night'])
filter_words.update(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','today','yesterday','tomorrow'])
filter_words.update(['january','february', 'march', 'april','may','june','july','august','september','october','november','december'])
filter_words.update(['jan','feb', 'mar', 'apr','jun','jul','aug','sep','oct','nov','dec'])
filter_words.update(['others', 'contrast','approach','change','response','people','possibility'])
filter_words.update(['recommendation', 'side','control','fact','win','attempt','amid','something','e.g','isnt','ive','hes','im','ill'])
filter_words.update(['rky','dc','dny','rfla','rid', 'try','weve','pas','co.','km','sens','rokla','am','cnn'])
filter_words.update(['a','b','c','d','e','f','g','h'])
filter_words.update(['']) #this was added, because the % symbol returns a valid single token, and is then stripped
filter_words.update(['zero','one','two','three','four','five','six','seven','eight','nine'])
#filter_words.update(set(nltk.corpus.stopwords.words('english'))
#I intentionally didn't add STOP_WORDS to this list, otherwise it would filter mis-categorizations
#   For example, "S&P 500" became "S", and "P", and 500 was lost. Only add this line when confident you've
#   cleaned the articles



#===========================================================
#               Helper functions
#===========================================================
def lambda_unpack(f):
    return lambda args: f(*args)

#============System to chunk individual terms into phrases ===================
def extract_candidate_chunks(text, filter_words, grammar=r'KT: {(<NN.*>+)? <NN.*>+}'):
    #strip_text = re.sub(r"[^\-\,\.\?\!\'\(\)\w\d'\s]+",'',text) #remove unicode characters
    #strip_text = re.sub(r"[^\'\!\"\#\$\&\\\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\\\]\^\_\`\{\|\}\~\'\w\d'\s]+",'',text) #removes unicode punctuation 
    strip_text = unicodedata.normalize('NFKD', text).encode('ascii','ignore').decode('utf-8')
    #Note: now I leave all punctuation to aid with sentence tokenization
    stop_words = set(nltk.corpus.stopwords.words('english'))
    stop_words |= filter_words
    
    # tokenize, POS-tag, and chunk using regular expressions
    #todo: currently the grammar chunker incorrectly strings possessives, "trump's plan" --> "trumps plan"
    #   ideally, that should be two tokens, "trump" and "plan"
    chunker = nltk.chunk.regexp.RegexpParser(grammar)
    tagged_sents = nltk.pos_tag_sents(nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(strip_text))
    all_chunks = list(itertools.chain.from_iterable(nltk.chunk.tree2conlltags(chunker.parse(tagged_sent))
                                                    for tagged_sent in tagged_sents))
    candidates = [' '.join(nltk.stem.WordNetLemmatizer().lemmatize(word) for word, pos, chunk in group).lower()
        for key, group in itertools.groupby(all_chunks, lambda_unpack(lambda word, pos, chunk: chunk != 'O')) if key]
    
    #We had left standard punctuation to aid in sentence chunking. Now delete all intra-word punctuation. "f.b.i. --> "fbi"
    for idx in range(len(candidates)):
        candidates[idx] = re.sub(r"[!\"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]", '', candidates[idx])

    return [cand.lstrip() for cand in candidates if cand not in stop_words]

#==========Take a single long string of text and convert it into terms / phrases========
def parse_article(dsi_text, phrase_dict, ec_dict, grammar=r'KT: {(<NN.*>+)? <NN.*>+}'):
    dsi_sentences = nltk.sent_tokenize(dsi_text)
    ec_text = ""
    insensitive_phrase = ""
    #Before processing, let's capture combinatory-word-phrases to avoid incorrect splitting
    #   e.g., "Cash for guns" --> "cashForGuns", to prevent "cash" and "guns" indivudually
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
#               Main program
#===========================================================

corpus = []
file_list = [f for f in os.listdir(corpus_path) if os.path.isfile(os.path.join(corpus_path, f))]

#Let's open all DSI, and append the text of each to a list
for f in file_list:
    document = docx.Document(corpus_path+f)
    dsi_text = ""
    #Luckily, metadata is in a table, and the paragraphs functions will skip it
    for p in document.paragraphs:
        dsi_text += ' ' + p.text
    corpus.append(dsi_text)
del f, p, document, dsi_text
#corpus now contains all raw text of all DSI, each article as a solid string.


#Next, let's parse each article into grammar chunks, phrases, and terms

#Use the following to include adjectives and preposition / conjunction chunks
#    e.g., "cash for guns" rather than split, "cash", "guns"
#    e.g., "dire days on Wall Street", rather than "dire days", "Wall Street"
grammar_conjunctions = r'KT: {(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+}'
#Use the following to include adjective modifiers
#    e.g., "blue car" rather than just "car"
grammar_adjectives = r'KT: {(<JJ>* <NN.*> <NN.*>+)? <JJ>* <NN.*>+}'
#Only chunk noun-linked sections
#    e.g., "bird house", or "emergency road flare"
grammar_nouns = r'KT: {(<NN.*>+)? <NN.*>+}'

#convert each string-of-text into a list comprised of DataFrame-of-terms
corpus_phrases = []
for dsi in corpus:
    corpus_phrases.append(parse_article(dsi, phrase_dict, ec_dict, grammar_nouns))
del dsi

#gather all terms to build our "master" list of terms
#create a new list of all dsi, and "pivot" on terms for total counts
master = pd.DataFrame()
corpus_term_counts = []
for i in range(0, len(file_list)):
    corpus_phrases[i]['dsi'] = file_list[i][0:6]
    master = pd.concat([master, corpus_phrases[i]])
    #countdf_terms = corpus_phrases[i].terms.value_counts()
    corpus_term_counts.append(pd.DataFrame(corpus_phrases[i].terms.value_counts()))
    corpus_term_counts[i].columns = (['t_count'])
    corpus_term_counts[i].loc[:,'tf'] = 0.0
    corpus_term_counts[i].loc[:,'idf'] = 0.0
    corpus_term_counts[i].loc[:,'tf_idf'] = 0.0
del i#, countdf_terms

master = master.reset_index(drop=True)

#count number TOTAL times a term occurs in whole corpus
master_terms = master.terms.value_counts()

term_loc_series = master.groupby(['terms','dsi']).size()

masterdf_terms = pd.DataFrame(master_terms)
masterdf_terms.columns=(['t_count'])
masterdf_terms['d_count'] = 0
terms_in_corpus = sum(masterdf_terms['t_count'])
masterdf_terms.loc[:,'tf'] = 0.0
masterdf_terms.loc[:,'idf'] = 0.0
masterdf_terms.loc[:,'tf_idf'] = 0.0
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

#masterdf_terms.to_csv(output_path+'master.csv')

#calculate tf_idf for INDIVIDUAL DSI
for i in range(0, len(corpus_term_counts)):
    for term in corpus_term_counts[i].index:
        corpus_term_counts[i].set_value(term,'tf',masterdf_terms.loc[term]['tf'])
        corpus_term_counts[i].set_value(term,'idf',masterdf_terms.loc[term]['idf'])
        #todo: fix idf calculation for each individual DSI
        corpus_term_counts[i].set_value(term,'tf_idf',masterdf_terms.loc[term]['tf_idf'])
del i,term#, countdf_terms


#create the matrix of terms across each DSI
for i in range(0, len(corpus_term_counts)):
    for term in corpus_term_counts[i].index:
        masterdf_terms.set_value(term,file_list[i][0:6],corpus_term_counts[i]['t_count'][term])
del i,term

#write the master matrix out to a CSV file
masterdf_terms.to_csv(output_path+'master.csv')

#write out all of the individual DSI to their own CSV
for i in range(0, len(corpus_term_counts)):
    corpus_term_counts[i].to_csv(output_path + file_list[i][0:6] + '.csv')
    #todo: the above [0:6] will start overwriting DSI once we hit #100
    #     [DSI-12], would be overwritten by [DSI-12]1, for example
del i
