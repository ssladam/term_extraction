import pickle
pickle_path = "C:/temp/NU/453/pickle/" #where do you want to read / write the phrase list / filters, etc.

weight_dict = {
    'presidentDonaldTrump':0.1,\

}
pickle.dump(weight_dict, open(pickle_path + 'weight_dict.p', 'wb'))