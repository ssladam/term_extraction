#IMPORTANT: currently this weighting is only applied to EC TERMS!! What that means:
#  If you have "arms sales" and "foreign arms dealers" all belonging to an "arms" concept,
#  and you weight "arms", then you could even FAIL to apply any weighting at all to the
#  overall concept, since there is no instance of "arms". Similarly, if you weight
#  "arms sales" as 2x, then you have effectively increased the weight of the "arms"
#  concept since one of it's contributing terms is weighted higher. However, if you
#  create an EC so that both "arms sales" and "foreign arms dealers" both roll into
#  an "arms" EC (not concept!) then your "arms" weighting WILL be applied to both
#  instances, in whatever DSI they appear in.

#Todo: Create another "weighted_concept_dict" to allow weighting CONCEPTS, indpendent of ECs

#import pickle
#if __name__ == '__main__':
#    pickle_path = "C:/temp/NU/453/pickle/" #where do you want to read / write the phrase list / filters, etc.

weight_dict = {
"presidentDonaldTrump":0.1,\
"conflict":0.1,\
"economy":0.1,\
"trumpAdministration":0.1,\
"unitedStates":0.1,\
"borderWall":2,\
"daca":2,\
"wto":2,\
"nafta":2,\
"healthcare":2,\

}
#pickle.dump(weight_dict, open(pickle_path + 'weight_dict.p', 'wb'))
