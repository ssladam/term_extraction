#add all words you want to filter into filter_words, this also occurs POST PROCESSING, so now if you filter
#  the term "friday" it will drop that singular term, but WOULD NOT filter "friday night" since it doesn't match

import pickle
filter_words = set()
pickle_path = "C:/temp/NU/453/pickle/" #where do you want to read / write the phrase list / filters, etc.

filter_words.update(['year', 'week', 'month', 'day', 'hour', 'minute', 'time','past','morning','afternoon', 'evening', 'night'])
filter_words.update(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','today','yesterday','tomorrow'])
filter_words.update(['january','february', 'march', 'april','may','june','july','august','september','october','november','december'])
filter_words.update(['jan','feb', 'mar', 'apr','jun','jul','aug','sep','oct','nov','dec'])
filter_words.update(['others', 'contrast','approach','change','response','people','possibility'])
filter_words.update(['recommendation', 'side','control','fact','win','attempt','amid','something','eg','isnt','ive','hes','im','ill'])
filter_words.update(['rky','dc','dny','rfla','rid', 'try','weve','pas','co','km','sens','rokla','am','cnn'])
filter_words.update(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
filter_words.update(['']) #this was added since the % symbol returns as a valid single token, and is then stripped
filter_words.update(['zero','one','two','three','four','five','six','seven','eight','nine'])


pickle.dump(filter_words, open(pickle_path + 'filter_words.p', 'wb'))