#This will be swapped out after processing is complete, now you're safe to
#  swap out individual words for their EC equivalent.

import pickle
pickle_path = "C:/temp/NU/453/pickle/" #where do you want to read / write the phrase list / filters, etc.

ec_dict = {
               'trump':'presidentDonaldTrump',\
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

pickle.dump(ec_dict, open(pickle_path + 'ec_dict.p', 'wb'))