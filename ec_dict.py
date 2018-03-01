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
               "united state":"unitedStates",\
               "mr trump":"presidentDonaldTrump",\
               "mr trumps":"presidentDonaldTrump",\
               "president trump":"presidentDonaldTrump",\
               "president trumps":"presidentDonaldTrump",\
               "President Donald Trump":"presidentDonaldTrump",\
               "donald j trump":"presidentDonaldTrump",\
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
               "tariff hike":"tariff",\
#====================Begin pasted from excel generator=====================
"trump":"presidentDonaldTrump",\
"emergency action perry":"rickPerry",\
"energy commissioner miguel arias canete":"ariasCanete",\
"energy secretary rick perry":"rickPerry",\
"environmental protection agency headquarters":"usEnvironmentalProtectionAgency",\
"environmental protection agency tuesday":"usEnvironmentalProtectionAgency",\
"epa grant":"usEnvironmentalProtectionAgency",\
"epa rule":"usEnvironmentalProtectionAgency",\
"epa transition team":"usEnvironmentalProtectionAgency",\
"epas clean power plan":"usEnvironmentalProtectionAgency",\
"environmental protection agency":"usEnvironmentalProtectionAgency",\
"erdogan":"recepErdogan",\
"erdogans":"recepErdogan",\
"fbi director comey":"jamesComey",\
"flemingss experience":"terryFlemings",\
"florida governor rick scott":"rickScott",\
"florida sen marco rubio":"marcoRubio",\
"former president bill clinton":"billClinton",\
"fort myers airport":"fortMeyers",\
"fort myers area":"fortMeyers",\
"heller":"deanHeller",\
"hillary":"hillaryClinton",\
"house appropriation":"houseAppropriationCommittee",\
"house appropriation committee chairman hal rogers":"houseAppropriationCommittee",\
"house democrat friday morning":"democrat",\
"house democratic caucus chairman":"democrat",\
"house majority whip steve scalise":"steveScalise",\
"hyundai motor":"hyundai motor co",\
"hyundai research institute":"hyundai motor co",\
"james b comey":"fbiDirector",\
"james comey":"fbiDirector",\
"laggard united state":"unitedStates",\
"language trump":"presidentDonaldTrump",\
"law enforcement community":"lawEnforcement",\
"law enforcement official":"lawEnforcement",\
"leader kim jong un":"northKorea",\
"liberal hate him":"hate",\
"limit refugee":"refugee",\
"lockheed":"lockheed martin",\
"lt gen h r mcmaster":"general mcmaster",\
"macri":"mauricio macri",\
"macro advisor":"macroeconomics advisor",\
"magazine cover":"magazine",\
"malloy":"dannel malloy",\
"market behavior":"stock market",\
"market news":"stock market",\
"market share":"stock market",\
"mcconnell hasnt":"mitch mcconnell",\
"mcconnells job":"mitch mcconnell",\
"mcmaster":"general mcmaster",\
"mean trump":"presidentDonaldTrump",\
"measure trump":"presidentDonaldTrump",\
"medicaid block grant":"medicaid",\
"medicaid funding level":"medicaid",\
"media bias":"media",\
"media outlet":"media",\
"media site":"media",\
"meeting mr comey":"jamesComey",\
"memoranda obama":"barackObama",\
"methane emission":"methane",\
"michael t flynn":"michael flynn",\
"middle eastern country":"middle east",\
"middle eastern peace":"middle east",\
"military armistice commission":"military",\
"military option":"military",\
"missile defense system":"missile",\
"missile launch":"missile",\
"missile site":"missile",\
"missile submarine":"missile",\
"mnuchin":"steven mnuchin",\
"mnuchins":"steven mnuchin",\
"monday night trump":"presidentDonaldTrump",\
"monica lewinsky":"billClinton",\
"moody chief economist mark zandi":"mark zandi",\
"mortgage guarantor fannie mae":"fannie mae",\
"move mr trump":"presidentDonaldTrump",\
"mr farage":"nigel farage",\
"mr kims":"kim jonghoon",\
"mr kushners team":"jared kushner",\
"mr mattis":"jim mattiss",\
"mr mattiss assertion":"jim mattiss",\
"mr muellers investigation":"robert mueller",\
"mr navarros":"peter navarro",\
"mr obama":"barackObama",\
"mr pence":"mikePence",\
"nancy":"nancyPelosi",\
"nancy pelosi":"nancyPelosi",\
"president barack obamas health care initiative":"obamacare",\
"president bill clinton":"billClinton",\
"president donald trump administration":"trumpAdministration",\
"president donald trump wall":"borderWall",\
"president robert s mueller iii":"robert mueller",\
"president trump call":"presidentDonaldTrump",\
"president trump decision":"presidentDonaldTrump",\
"president xi jinping":"xi jinping",\
"president xi jinpings help":"xi jinping",\
"presidential adviser kellyanne conway":"kellyanne conway",\
"program trump":"presidentDonaldTrump",\
"promise obama":"barackObama",\
"prosecution interview":"prosecution",\
"puerto rico capital city":"puerto rico",\
"pundit ann coulter":"ann coulter",\
"putin cool":"vladimir putin",\
"rachel maddow tuesday night":"rachel maddow",\
"radio talk show host":"radio show",\
"range missile":"missile",\
"realdonaldtrump interesting":"presidentDonaldTrump",\
"realdonaldtrump just":"presidentDonaldTrump",\
"recep erdogan":"recepErdogan",\
"regulation enforcement":"regulation",\
"regulation policy":"regulation",\
"remember trump":"presidentDonaldTrump",\
"renegotiations":"renegotiation",\
"renew daca":"daca",\
"repeal obamacare":"obamacare",\
"replace obamacare act":"obamacare",\
"report cnbc":"cnbc",\
"republican district":"republican",\
"republican house speaker paul ryan":"paul ryan",\
"republican leader":"republican",\
"republican majority":"republican",\
"republican matchup":"republican",\
"republican national committee chairman trump":"presidentDonaldTrump",\
"republican national committee spokesman sean spicer":"sean spicer",\
"republican official":"republican",\
"republican orthodoxy":"republican",\
"republican party":"republican",\
"republican philanthropist betsy devos":"betsy devos",\
"republican president":"presidentDonaldTrump",\
"republican presidentelect":"presidentDonaldTrump",\
"republican rick scott":"rickScott",\
"republican trump":"presidentDonaldTrump",\
"republican voter":"republican",\
"residence time":"residency",\
"residency status":"residency",\
"retaliation trump":"presidentDonaldTrump",\
"rex w tillerson":"rex tillerson",\
"rhode island democratic leadership":"democrat",\
"right activist":"republican",\
"right concern":"republican",\
"right investigation":"republican",\
"right organization":"republican",\
"robarts":"james robart",\
"ronald reagan pentagon buildup":"ronald reagan",\
"ronald reagan playbook":"ronald reagan",\
"ronald reagan white house":"ronald reagan",\
"rosenberg":"chuck rosenberg",\
"rubio":"marcoRubio",\
"ruffin":"phill ruffin",\
"ruffins complaint":"phill ruffin",\
"russia hoax":"russiaElectionHacking",\
"russia policy":"russiaElectionHacking",\
"russia story":"russiaElectionHacking",\
"russian involvement":"russiaElectionHacking",\
"russiatrump collusion story":"russiaElectionHacking",\
"russia ambassador":"russiaElectionHacking",\
"ruth bader ginsburg":"justice ruth bader ginsburg",\
"ryans":"paul ryan",\
"ryans dream":"paul ryan",\
"sen dean heller":"deanHeller",\
"heller":"deanHeller",\
"dean heller":"deanHeller",\
"tea party express":"tea party",\
"tea party favorite":"tea party",\
"term globalization":"globalization",\
"terror":"terrorism",\
"terror attack":"terrorism",\
"terrorism activity":"terrorism",\
"terrorprone region":"terrorism",\
"test launch":"missile",\
"the wall":"borderWall",\
"thenspeaker boehner":"boehner",\
"to do with russia":"russia",\
"today republican party":"republican",\
"tourist":"tourism industry",\
"tourist sector":"tourism industry",\
"toyota":"toyota motor corp",\
"tpp negotiation":"tpp",\
"tpp trade deal":"tpp",\
"trade adviser peter navarro":"peter navarro",\
"treasury secretary":"steven mnuchin",\
"treasury secretary steven mnuchin":"steven mnuchin",\
"treasury steven mnuchin":"steven mnuchin",\
"treaty limit":"treaty",\
"trump action":"presidentDonaldTrump",\
"trump administration move":"trumpAdministration",\
"trump aide steve bannon":"steve bannon",\
"trump bump":"presidentDonaldTrump",\
"trump bump hasnt":"presidentDonaldTrump",\
"trump cabinet":"trumpAdministration",\
"trump cabinet promise":"trumpAdministration",\
"trump confidante":"trumpAdministration",\
"trump criticism":"presidentDonaldTrump",\
"trump deal":"presidentDonaldTrump",\
"trump decision":"presidentDonaldTrump",\
"trump demand":"presidentDonaldTrump",\
"trump democratic predecessor":"barackObama",\
"trump desk":"presidentDonaldTrump",\
"trump doesnt recant":"presidentDonaldTrump",\
"trump effort":"presidentDonaldTrump",\
"trump employee":"presidentDonaldTrump",\
"trump era":"presidentDonaldTrump",\
"trump home state":"presidentDonaldTrump",\
"trump interview":"presidentDonaldTrump",\
"trump million":"presidentDonaldTrump",\
"trump move":"presidentDonaldTrump",\
"trump must be":"presidentDonaldTrump",\
"trump one":"presidentDonaldTrump",\
"trump people":"trumpAdministration",\
"trump pick":"presidentDonaldTrump",\
"trump pledge":"presidentDonaldTrump",\
"trump presidency cast":"presidentDonaldTrump",\
"trump revel":"presidentDonaldTrump",\
"trump rhetoric":"presidentDonaldTrump",\
"trump ruffin commercial llc":"presidentDonaldTrump",\
"trump russia story":"russiaElectionHacking",\
"trump spokeswoman":"trumpAdministration",\
"trump transition":"presidentDonaldTrump",\
"trump transition staff":"trumpAdministration",\
"trump transition team":"trumpAdministration",\
"trump view":"presidentDonaldTrump",\
"tweet friday morning":"twitter",\
"tweet meant":"twitter",\
"tweet wednesday morning":"twitter",\
"twitter post":"twitter",\
"twitter time":"twitter",\
"twitter tirade":"twitter",\
"twitter vernacular":"twitter",\
"twitter wednesday morning":"twitter",\
"u administration":"government",\
"u agency":"government",\
"u agreement":"domesticPolicy",\
"u border":"borderWall",\
"u circuit court":"courtSystem",\
"u congress":"government",\
"u constitution":"government",\
"u court":"courtSystem",\
"u diplomat":"usPolitician",\
"u election":"presidentialElection",\
"u fish":"us fish and wildlife service",\
"u government":"government",\
"u immigration":"immigration",\
"u immigration policy":"immigration",\
"u industry":"economy",\
"u influence":"foreignPolicy",\
"u intelligence chief":"intelligenceAgency",\
"u interior secretary ryan zinke":"ryan zinke",\
"u leader":"presidentDonaldTrump",\
"u president donald trump":"presidentDonaldTrump",\
"u trade":"trade",\
"un appearance":"united nations",\
"un conference":"united nations",\
"un general assembly":"united nations",\
"un official":"united nations",\
"un priority":"united nations",\
"un reform":"united nations",\
"united nation framework convention":"united nations",\
"united nation general assembly debut":"united nations",\
"united nation stage":"united nations",\
"uranium energy corp":"uranium",\
"uranium resource inc":"uranium",\
"us attorney":"eric holder",\
"us attorney general eric holder":"eric holder",\
"us district judge james robart":"james robart",\
"us factory":"us auto industry",\
"us factory automaker":"us auto industry",\
"us intelligence community":"intelligenceAgency",\
"us intelligence expert":"intelligenceAgency",\
"us intelligence report":"intelligenceAgency",\
"us manufacturer":"us manufacturing",\
"us manufacturing business environment":"us manufacturing",\
"us should brace for reputational cost china role":"china",\
"us taxfree":"taxes",\
"us taxpayer fund":"taxes",\
"us trade gap soar":"us trade gap",\
"us trade remedy law":"us trade law",\
"us trade representative robert lighthizer":"robert lighthizer",\
"us vehicle":"us auto industry",\
"utah mike lee":"mike lee",\
"veteran affair":"veteran",\
"veteran negotiator":"veteran",\
"vice president al gore":"al gore",\
"vice president joe biden":"joe biden",\
"video address":"video",\
"video speech":"video",\
"virginia republican":"republican",\
"virtual private network":"vpn",\
"vladimir v putin":"vladimir putin",\
"vote tally":"voter",\
"voter rate":"voter",\
"wa president trump decision":"presidentDonaldTrump",\
"wa trump":"presidentDonaldTrump",\
"wall promise":"borderWall",\
"wall street bank":"wall street",\
"wall street executive":"wall street",\
"wall upfront":"borderWall",\
"washington act":"washingtonDC",\
"washington embassy":"washingtonDC",\
"washington today":"washingtonDC",\
"wastewater disposal":"wastewater",\
"wastewater project":"wastewater",\
"water commission":"water quality",\
"water pipe":"water quality",\
"water resource":"water quality",\
"water treatment plant":"water quality",\
"water treatment project":"water quality",\
"weapon buildup":"weapons",\
"weapon capability":"weapons",\
"weapon export":"weapons",\
"weapon state":"weapons",\
"weaponryfrom":"weapons",\
"wednesday morning tweet":"twitter",\
"white house briefing room":"white house",\
"white house celebration":"white house",\
"white house departure":"white house",\
"white house deputy press secretary raj shah":"raj shah",\
"white house press secretary sarah huckabee sander":"sarah huckabee sanders",\
"white house press secretary":"press secretary",\
"white house rose garden":"white house",\
"white house source":"white house",\
"white house staff secretary rob porter":"rob porter",\
"wikileaks founder assange":"julian assange",\
"wildlife service":"us fish and wildlife service",\
"wind farm trump":"presidentDonaldTrump",\
"wisconsin republican":"republican",\
"world bank international financial corporation":"world bank",\
"world hegemonya description":"hegemony",\
"wto manages":"world trade organization",\
"wto rule":"world trade organization",\
"zandi":"mark zandi",\
"george w bush":"georgeBush",\
"gop lawmaker":"gop",\
"gop leader":"gop",\
"gop voter":"gop",\
"gov":"government",\
"graham":"senator lindsey graham",\
"grassley":"chuck grassley",\
"haitian":"haiti",\
"homeland security secretary":"secretary john kelly",\
"homeland security secretary john kelly":"secretary john kelly",\
"house gop":"gop",\
"house gop plan":"gop",\
"house minority leader nancy pelosi":"nancy pelosi",\
"house speaker paul ryan":"paul ryan",\
"immigration enforcement":"immigration",\
"immigration reform":"immigration",\
"immigration service":"immigration",\
"immigrationAndNationalityAct":"immigration",\
"internet user":"technology",\
"job growth":"jobs",\
"job offer":"jobs",\
"joblosses":"jobs",\
"kim regime":"kim jongun",\
"lighthizer":"robert lighthizer",\
"mass deportation force":"immigration",\
"medicaid expansion":"medicaid",\
"meeting mr trump":"presidentDonaldTrump",\
"merkel":"angela merkel",\
"mexico city":"mexico",\
"mr amolilarijani":"ali larijani",\
"mr field":"mark fields",\
"mr kislyak":"sergey i kislyak",\
"mr muellers office":"robert mueller",\
"mr tillerson":"rex tillerson",\
"mr trump action":"presidentDonaldTrump",\
"mulvaney":"mick mulvaney",\
"navarro":"peter navarro",\
"negotiating table":"negotiator",\
"new york attorney general eric schneiderman":"eric schneiderman",\
"news medium":"news outlet",\
"news organization":"news outlet",\
"nfl owner":"nfl",\
"nfl player":"nfl",\
"obamacare marketplace":"obamacare",\
"obamas":"barackObama",\
"paris deal":"paris climate accord",\
"paris pledge":"paris climate accord",\
"paul":"paul ryan",\
"police department":"police",\
"policy proposal":"policy",\
"pres":"president",\
"president george w bush":"georgeBush",\
"press secretary sean spicer":"sean spicer",\
"priebuss":"reince priebus",\
"prime minister shinzo abe":"shinzo abe",\
"republican chairman":"republican",\
"republican congress":"republican",\
"republican lawmaker":"republican",\
"san juan":"puerto rico",\
"scaramuccis":"anthony scaramucci",\
"schneiderman":"eric schneiderman",\
"secrecy":"secret",\
"senate judiciary committee":"senate",\
"senate leader":"senate",\
"senate race":"senate",\
"senate republican":"republican",\
"senator marco rubio":"marco rubio",\
"senator richard blumenthal":"richard blumenthal",\
"simpson":"glenn simpson",\
"state department spokesman john kirby":"john kirby",\
"democratic party":"democrat",\
"doddfrank":"doddfrank act",\
"fleming":"terryFlemings",\
"forney":"ben forney",\
"gop senator":"gop",\
"ier":"institue of energy research",\
"iers study":"institue of energy research",\
"manufacturing":"manufacturer",\
"mr blumenthal":"richard blumenthal",\
"mr muellers":"robert mueller",\
"mr navarro":"peter navarro",\
"mr putin":"vladimir putin",\
"mr xi":"xi jinping",\
"mr zinke":"ryan zinke",\
"osc":"office of special counsel",\
"paris accord":"paris climate accord",\
"perry":"rickPerry",\
"president vladimir putin":"vladimir putin",\
"president xi":"xi jinping",\
"republican senator":"republican",\
"robart":"judge james robart",\
"rogers":"houseAppropriationCommittee",\
"russian president":"vladimir putin",\
"scalia":"antonin scalia",\
"senate conservative":"republican",\
"senate democrat":"democrat",\
"state rex tillerson":"rex tillerson",\
"steele":"christopher steele",\
"trump plan":"presidentDonaldTrump",\
"u intelligence agency":"intelligenceAgency",\
"us intelligence agency":"intelligenceAgency",\
"vice president mike penny":"mike pence",\
"wolff":"michael wolff",\
"xi":"xi jinping",\

               
#================end pasted section====================               
               
               }
#the parser converts all entries to lower case, so we should do the same
ec_dict = {key.lower(): value for key, value in ec_dict.items()}

pickle.dump(ec_dict, open(pickle_path + 'ec_dict.p', 'wb'))
