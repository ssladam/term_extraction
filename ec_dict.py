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
"cruz":"ted cruz",\
"dean heller":"deanHeller",\
"deferred action":"daca",\
"democratic party":"democrat",\
"doddfrank":"doddfrank act",\
"emergency action perry":"rickPerry",\
"energy commissioner miguel arias canete":"ariasCanete",\
"energy secretary rick perry":"rickPerry",\
"environmental protection agency":"usEnvironmentalProtectionAgency",\
"environmental protection agency headquarters":"usEnvironmentalProtectionAgency",\
"environmental protection agency tuesday":"usEnvironmentalProtectionAgency",\
"epa":"usEnvironmentalProtectionAgency",\
"epa grant":"usEnvironmentalProtectionAgency",\
"epa rule":"usEnvironmentalProtectionAgency",\
"epa transition team":"usEnvironmentalProtectionAgency",\
"epas clean power plan":"usEnvironmentalProtectionAgency",\
"erdogan":"turkey",\
"erdogans":"turkey",\
"fbi director comey":"jamesComey",\
"fleming":"terryFlemings",\
"flemingss experience":"terryFlemings",\
"florida governor rick scott":"rickScott",\
"florida sen marco rubio":"marcoRubio",\
"former president bill clinton":"billClinton",\
"forney":"ben forney",\
"fort myers airport":"fortMeyers",\
"fort myers area":"fortMeyers",\
"george w bush":"georgeBush",\
"gop lawmaker":"gop",\
"gop leader":"gop",\
"gop senator":"gop",\
"gop voter":"gop",\
"gov":"government",\
"graham":"senator lindsey graham",\
"grassley":"chuck grassley",\
"haitian":"haiti",\
"heller":"deanHeller",\
"heller":"deanHeller",\
"hillary":"hillaryClinton",\
"homeland security secretary":"secretary john kelly",\
"homeland security secretary john kelly":"secretary john kelly",\
"house appropriation":"houseAppropriationCommittee",\
"house appropriation committee chairman hal rogers":"houseAppropriationCommittee",\
"house democrat friday morning":"democrat",\
"house democratic caucus chairman":"democrat",\
"house gop":"gop",\
"house gop plan":"gop",\
"house majority whip steve scalise":"steveScalise",\
"house minority leader nancy pelosi":"nancy pelosi",\
"house speaker paul ryan":"paul ryan",\
"hyundai motor":"hyundai motor co",\
"hyundai research institute":"hyundai motor co",\
"ier":"institue of energy research",\
"iers study":"institue of energy research",\
"immigration enforcement":"immigration",\
"immigration reform":"immigration",\
"immigration service":"immigration",\
"immigrationAndNationalityAct":"immigration",\
"internet user":"technology",\
"james b comey":"fbiDirector",\
"james comey":"fbiDirector",\
"job growth":"jobs",\
"job offer":"jobs",\
"joblosses":"jobs",\
"johnson":"ron johnson",\
"kennedy":"anthony kennedy",\
"kim regime":"kim jongun",\
"laggard united state":"unitedStates",\
"language trump":"presidentDonaldTrump",\
"law enforcement community":"lawEnforcement",\
"law enforcement official":"lawEnforcement",\
"leader kim jong un":"northKorea",\
"liberal hate him":"hate",\
"lighthizer":"robert lighthizer",\
"limit refugee":"refugee",\
"lockheed":"lockheed martin",\
"lt gen h r mcmaster":"general mcmaster",\
"macri":"mauricio macri",\
"macro advisor":"macroeconomics advisor",\
"magazine cover":"magazine",\
"malloy":"dannel malloy",\
"manufacturing":"manufacturer",\
"market behavior":"stock market",\
"market news":"stock market",\
"market share":"stock market",\
"mass deportation force":"immigration",\
"mcconnell":"mitch mcconnell",\
"mcconnell hasnt":"mitch mcconnell",\
"mcconnells job":"mitch mcconnell",\
"mcmaster":"general mcmaster",\
"mean trump":"presidentDonaldTrump",\
"measure trump":"presidentDonaldTrump",\
"media bias":"media",\
"media outlet":"media",\
"media site":"media",\
"medicaid block grant":"medicaid",\
"medicaid expansion":"medicaid",\
"medicaid funding level":"medicaid",\
"meeting mr comey":"jamesComey",\
"meeting mr trump":"presidentDonaldTrump",\
"memoranda obama":"barackObama",\
"merkel":"angela merkel",\
"methane emission":"methane",\
"mexico city":"mexico",\
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
"mr amolilarijani":"ali larijani",\
"mr blumenthal":"richard blumenthal",\
"mr farage":"nigel farage",\
"mr field":"mark fields",\
"mr flynn":"michael flynn",\
"mr kims":"kim jonghoon",\
"mr kislyak":"sergey i kislyak",\
"mr kushners team":"jared kushner",\
"mr mattis":"jim mattiss",\
"mr mattiss assertion":"jim mattiss",\
"mr mueller":"robert mueller",\
"mr muellers":"robert mueller",\
"mr muellers investigation":"robert mueller",\
"mr muellers office":"robert mueller",\
"mr navarro":"peter navarro",\
"mr navarros":"peter navarro",\
"mr obama":"barackObama",\
"mr pence":"mikePence",\
"mr putin":"vladimir putin",\
"mr tillerson":"rex tillerson",\
"mr trump action":"presidentDonaldTrump",\
"mr xi":"xi jinping",\
"mr zinke":"ryan zinke",\
"ms clifford":"stephanie clifford",\
"mulvaney":"mick mulvaney",\
"nancy":"nancyPelosi",\
"nancy pelosi":"nancyPelosi",\
"navarro":"peter navarro",\
"negotiating table":"negotiator",\
"new york attorney general eric schneiderman":"eric schneiderman",\
"new york time":"new york",\
"news medium":"news outlet",\
"news organization":"news outlet",\
"nfl owner":"nfl",\
"nfl player":"nfl",\
"obama administration":"barackObama",\
"obamacare marketplace":"obamacare",\
"obamas":"barackObama",\
"osc":"office of special counsel",\
"panetta":"leon panetta",\
"paris accord":"paris climate accord",\
"paris deal":"paris climate accord",\
"paris pledge":"paris climate accord",\
"paul":"paul ryan",\
"perry":"rickPerry",\
"police department":"police",\
"policy proposal":"policy",\
"pres":"president",\
"president barack obama":"barackObama",\
"president barack obamas health care initiative":"obamacare",\
"president bill clinton":"billClinton",\
"president donald trump administration":"trumpAdministration",\
"president donald trump wall":"borderWall",\
"president george w bush":"georgeBush",\
"president obama":"barackObama",\
"president robert s mueller iii":"robert mueller",\
"president trump call":"presidentDonaldTrump",\
"president trump decision":"presidentDonaldTrump",\
"president vladimir putin":"vladimir putin",\
"president xi":"xi jinping",\
"president xi jinping":"xi jinping",\
"president xi jinpings help":"xi jinping",\
"presidential adviser kellyanne conway":"kellyanne conway",\
"press secretary sean spicer":"sean spicer",\
"priebus":"reince priebus",\
"priebuss":"reince priebus",\
"prime minister shinzo abe":"shinzo abe",\
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
"recep erdogan":"turkey",\
"regulation enforcement":"regulation",\
"regulation policy":"regulation",\
"remember trump":"presidentDonaldTrump",\
"renegotiations":"renegotiation",\
"renew daca":"daca",\
"repeal obamacare":"obamacare",\
"replace obamacare act":"obamacare",\
"report cnbc":"cnbc",\
"republican chairman":"republican",\
"republican congress":"republican",\
"republican district":"republican",\
"republican house speaker paul ryan":"paul ryan",\
"republican lawmaker":"republican",\
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
"republican senator":"republican",\
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
"robart":"judge james robart",\
"robarts":"james robart",\
"rogers":"houseAppropriationCommittee",\
"ronald reagan pentagon buildup":"ronald reagan",\
"ronald reagan playbook":"ronald reagan",\
"ronald reagan white house":"ronald reagan",\
"rosenberg":"chuck rosenberg",\
"rubio":"marcoRubio",\
"ruffin":"phill ruffin",\
"ruffins complaint":"phill ruffin",\
"russia ambassador":"russiaElectionHacking",\
"russia hoax":"russiaElectionHacking",\
"russia policy":"russiaElectionHacking",\
"russia story":"russiaElectionHacking",\
"russian involvement":"russiaElectionHacking",\
"russian president":"vladimir putin",\
"russiatrump collusion story":"russiaElectionHacking",\
"ruth bader ginsburg":"justice ruth bader ginsburg",\
"ryan":"paul ryan",\
"ryans":"paul ryan",\
"ryans dream":"paul ryan",\
"san juan":"puerto rico",\
"scalia":"antonin scalia",\
"scaramucci":"anthony scaramucci",\
"scaramuccis":"anthony scaramucci",\
"schneiderman":"eric schneiderman",\
"secrecy":"secret",\
"sen dean heller":"deanHeller",\
"senate conservative":"republican",\
"senate democrat":"democrat",\
"senate judiciary committee":"senate",\
"senate leader":"senate",\
"senate majority leader mitch mcconnell":"mitch mcconnell",\
"senate minority leader chuck schumer":"chuck schumer",\
"senate race":"senate",\
"senate republican":"republican",\
"senator marco rubio":"marco rubio",\
"senator richard blumenthal":"richard blumenthal",\
"simpson":"glenn simpson",\
"spicer":"sean spicer",\
"state department spokesman john kirby":"john kirby",\
"state rex tillerson":"rex tillerson",\
"steele":"christopher steele",\
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
"tillerson":"rex tillerson",\
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
"trump":"presidentDonaldTrump",\
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
"trump foundation":"presidentDonaldTrump",\
"trump home state":"presidentDonaldTrump",\
"trump interview":"presidentDonaldTrump",\
"trump million":"presidentDonaldTrump",\
"trump move":"presidentDonaldTrump",\
"trump must be":"presidentDonaldTrump",\
"trump one":"presidentDonaldTrump",\
"trump people":"trumpAdministration",\
"trump pick":"presidentDonaldTrump",\
"trump plan":"presidentDonaldTrump",\
"trump pledge":"presidentDonaldTrump",\
"trump presidency":"presidentDonaldTrump",\
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
"u intelligence agency":"intelligenceAgency",\
"u intelligence chief":"intelligenceAgency",\
"u intelligence community":"intelligenceAgency",\
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
"us intelligence agency":"intelligenceAgency",\
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
"vice president mike penny":"mike pence",\
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
"white house press secretary":"press secretary",\
"white house press secretary sarah huckabee sander":"sarah huckabee sanders",\
"white house rose garden":"white house",\
"white house source":"white house",\
"white house staff secretary rob porter":"rob porter",\
"wikileaks founder assange":"julian assange",\
"wildlife service":"us fish and wildlife service",\
"wind farm trump":"presidentDonaldTrump",\
"wisconsin republican":"republican",\
"wolff":"michael wolff",\
"world bank international financial corporation":"world bank",\
"world hegemonya description":"hegemony",\
"wto manages":"world trade organization",\
"wto rule":"world trade organization",\
"xi":"xi jinping",\
"zandi":"mark zandi",\
"activist base":"activist",\
"allegation business":"allegation",\
"allegation trump":"allegation",\
"job":"jobs",\
"president barack obamas nominee":"barackObama",\
"backlash online":"backlash",\
"nancy":"nancyPelosi",\
"nancy pelosi":"nancyPelosi",\

               
#================end pasted section====================               
               
               }
#the parser converts all entries to lower case, so we should do the same
ec_dict = {key.lower(): value for key, value in ec_dict.items()}

pickle.dump(ec_dict, open(pickle_path + 'ec_dict.p', 'wb'))
