import pickle
pickle_path = "C:/temp/NU/453/pickle/" #where do you want to read / write the phrase list / filters, etc.

concept_dict = {
"arm sale decision":"arms",\
"assault rifle":"arms",\
"arm control advocate":"arms",\
"arm export policy":"arms",\
"us weapon":"arms",\
"weapon program":"arms",\
"arm export":"arms",\
"arm maker":"arms",\
"usmexico border":"borderSecurity",\
"border protection":"borderSecurity",\
"border security issue":"borderSecurity",\
"border security budget document":"borderSecurity",\
"southern border":"borderSecurity",\
"border security":"borderSecurity",\
"homeland security":"borderSecurity",\
"barrier":"borderSecurity",\
"security":"borderSecurity",\
"border":"borderSecurity",\
"border barrier":"borderWall",\
"fencing":"borderWall",\
"border wall prototype":"borderWall",\
"border wall":"borderWall",\
"wall":"borderWall",\
"gas":"business",\
"business":"business",\
"defense contractor":"business",\
"steel":"business",\
"coal":"business",\
"commerce secretary":"commerceSecretary",\
"commerce department highlight sheet":"commerceSecretary",\
"commerce department":"commerceSecretary",\
"wilburRoss":"commerceSecretary",\
}

#index keys are case sensitive, let's use all lower() to ensure success in match
concept_dict = {key.lower(): value for key, value in concept_dict.items()}
#todo: build case-insensitive matching

pickle.dump(concept_dict, open(pickle_path + 'concept_dict.p', 'wb'))