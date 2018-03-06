#Preprocessing, opportunity to replace words or phrases with ECs
#  DO NOT add "president" --> "presidentTrump" here, otherwise all instances
#  of "president obama" would be converted to "presidentTrump obama"
#  this should be used for fixed phrases ONLY


def get_phrases():
    #phrase_dict = {
    return {
            "Trans-Pacific Partnership": "TPP",\
            "North American Free Trade Agreement":"NAFTA",\
            "World Trade Organization":"WTO",\
            "fire and fury":"fireAndFury",\
            "lost jobs":"jobLosses",\
            "job losses":"jobLosses",\
            "chief of staff":"chiefOfStaff",\
            "E&E News":"EandENews",\
            "S&P 500":"SandP500",\
            "Immigration and Nationality Act":"immigrationAndNationalityAct",\
            "Club For Growth and Heritage":"clubForGrowthAndHeritage",\
            "Freedom Caucus":"freedomCaucus",\
            "Office of Personnel Management ":"officeOfPersonnelManagement",\
            "Office of Management and Budget":"officeOfManagementAndBudget",\
            "Office of Special Counsel":"officeOfSpecialCounsel",\
            #Here is my first hack-y cheat. To avoid phrase clumping, insert a determiner to force phrase-split
            #   the below will force the code to split this into "memorandum" and "donald trump", instead of a single term
            "memorandum donald trump":"memorandum which donald trump",\
            #My 2nd hack-y cheat: pre-filtering some terms that would be tricky to remove otherwise
            #   these terms become "nested" with other terms, easier to just axe them here
            "[sic]":"",\
            "percent":"",\
            "percentage":"",\
            }
