import pickle
pickle_path = "C:/temp/NU/453/pickle/" #where do you want to read / write the phrase list / filters, etc.

concept_dict = {

#===================Begin pasted section from excel generator=============
"arm sale decision":"arms",\
"assault rifle":"arms",\
"arm control advocate":"arms",\
"arm export policy":"arms",\
"u.s. weapon":"arms",\
"weapon program":"arms",\
"arm export":"arms",\
"arm maker":"arms",\
"u.s.-mexico border":"borderSecurity",\
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
"7th circuit":"federalCourt",\
"aapl":"business",\
"abbasi":"middleEasternPolitics",\
"abc":"finance",\
"abcs good morning america":"media",\
"aberdeen":"europeanCity",\
"aca":"healthcarePolicy",\
"accident":"event",\
"aclu":"domesticPolicy",\
"acquisition":"business",\
"action may be taken":"event",\
"actions speak louder than words realm":"statement",\
"activist base":"conflict",\
"activist group nextgen climate":"environmentalPolicy",\
"activist tom steyer":"environmentalPolicy",\
"ad":"media",\
"additional aide":"trumpAdministration",\
"administration budget":"finance",\
"administration hasnt":"trumpAdministration",\
"administration intensifies negotiation":"trumpAdministration",\
"administration lawyer":"trumpAdministration",\
"administration policy":"trumpAdministration",\
"administration preparation":"trumpAdministration",\
"administration response":"trumpAdministration",\
"administration tuesday night":"trumpAdministration",\
"administrator trump":"trumpAdministration",\
"advantage china":"foreignPolicy",\
"advertisement":"media",\
"advertiser":"media",\
"affiliate kia motors corp":"business",\
"affordable care act isnt exploding":"domesticPolicy",\
"afghanistan all muslim majority nation":"muslimCountry",\
"afternoon broadcast fox news shep smith":"media",\
"agitator":"conflict",\
"agreement mr trump":"negotiation",\
"agricultural bank":"business",\
"agriculture":"agriculture",\
"agriculture secretary sonny perdue":"usPolitician",\
"agriculture something":"agriculture",\
"aide briefed":"trumpAdministration",\
"aide meeting":"trumpAdministration",\
"air conditioning":"comfort",\
"air force":"military",\
"air force one":"transportation",\
"alabama sen jeff sessions":"usPolitician",\
"alabama us senate":"usGovernment",\
"alamo":"historicLocation",\
"alaska":"usState",\
"alaskas lisa murkowski":"usPolitician",\
"alberta":"canadianProvence",\
"albertas oil":"environmental",\
"aleksey pushkov":"russianPolitican",\
"ali larijani":"middleEasternPolitics",\
"alien":"immigration",\
"allegation business":"conflict",\
"allegation trump":"conflict",\
"allocation":"finance",\
"ally japan":"foreignPolicy",\
"almighty god":"religion",\
"aluminum case":"arms",\
"alzheimer":"medical",\
"ambivalence":"attitude",\
"americafirst energy policy":"environmentalPolicy",\
"american conservative union":"environmentalPolicy",\
"american energy alliance":"environmentalPolicy",\
"american energy reserve":"environmentalPolicy",\
"american federalist system":"usGovernment",\
"american household income":"economy",\
"american medical association":"medical",\
"americas defense":"nationalSecurity",\
"americas energy problem":"environmentalPolicy",\
"americas water":"environmentalPolicy",\
"americorps":"environmentalPolicy",\
"ammunition":"arms",\
"amnesty":"conflict",\
"amnesty don":"conflict",\
"amnesty international":"conflict",\
"amy spitalnick":"usPolitician",\
"andrew cuomo":"usPolitician",\
"annexation":"conflict",\
"annie leonard":"environmentalPolicy",\
"announce":"event",\
"anthony scaramucci":"entrepreneur",\
"anticlinton":"conflict",\
"anticorruption group":"scandal",\
"antidefamation league":"conflict",\
"antitrump":"conflict",\
"antiunion consulting firm":"economy",\
"antius credential":"conflict",\
"antonin scalia":"supremeCourtJudge",\
"antonio villaraigosa":"usPolitician",\
"appalachian":"geography",\
"appeal court":"courtSystem",\
"appeal court judge":"courtSystem",\
"applause":"event",\
"appropriations committee":"usGovernment",\
"argentine counterpart mauricio macri":"southAmericanPolitics",\
"argentine journalist jorge lanata":"southAmericanPolitics",\
"arizonas capital":"usState",\
"arm control advocate":"arms",\
"arm deal":"arms",\
"arm export":"arms",\
"arm export policy":"arms",\
"arm maker":"arms",\
"arm proliferation":"arms",\
"arm sale":"arms",\
"arm sale decision":"arms",\
"arm supplier":"arms",\
"armageddon":"disaster",\
"arms control association":"arms",\
"arms regulations":"arms",\
"arms regulations besides":"arms",\
"army":"military",\
"arsenal":"arms",\
"artillery":"arms",\
"asan institute":"education",\
"asia development bank":"finance",\
"assault rifle":"arms",\
"associate professor":"education",\
"asylum claim":"foreignPolicy",\
"atlantic":"geography",\
"atlantic city":"usCity",\
"atlantic ocean":"geography",\
"atlantic reserve":"military",\
"attorney general jeff sessions":"usPolitician",\
"audience wider":"event",\
"author michael wolff":"media",\
"author mike godwin":"media",\
"authoritarianism":"government",\
"auto industry account":"business",\
"auto industry committee":"business",\
"auto maker":"business",\
"automation":"business",\
"automation plan":"business",\
"automobile":"business",\
"away south korea":"southKorea",\
"axios":"media",\
"ayatollah sadegh amolilarijani":"middleEasternPolitics",\
"backlash online":"conflict",\
"bahrain":"middleEast",\
"bald threat":"conflict",\
"bali":"asia",\
"bank building":"finance",\
"banker":"finance",\
"banking":"finance",\
"bankruptcy law":"finance",\
"barack obamas government":"barackObama",\
"barack obamas presidency":"barackObama",\
"barack obamas work":"barackObama",\
"barrage":"arms",\
"bbc":"media",\
"bearing factory":"business",\
"becerra":"usPolitician",\
"ben forney":"southKorea",\
"benefitcost analysis":"finance",\
"bernstein research":"business",\
"bestseller list":"media",\
"betsy devos":"usPolitician",\
"bfps ventures":"business",\
"big bend":"geography",\
"bigcity mayor":"usPolitician",\
"biggest foreign policy headache":"foreignPolicy",\
"bigotry strike":"conflict",\
"bill frist":"usPolitician",\
"bill kristol":"media",\
"billionaire developer":"business",\
"billionaire education secretary":"usPolitician",\
"billionaire environmentalist tom steyer":"environmentalPolicy",\
"biological diversity":"environmental",\
"bipartisanship":"communication",\
"blackmail":"conflict",\
"blind trust issue a number":"finance",\
"bloodbath":"conflict",\
"bloomberg":"media",\
"bloomberg news":"media",\
"bluffing":"conflict",\
"blunt tweet":"communication",\
"bob fleisher":"education",\
"body language":"communication",\
"boehner":"usPolitician",\
"boeing":"business",\
"boeing co":"business",\
"bomber":"violentCrime",\
"bond holder":"finance",\
"bonus check":"economy",\
"border fence":"immigration",\
"border fencing":"immigration",\
"border measure":"immigration",\
"border patrol agent":"immigration",\
"border security budget document":"immigration",\
"border security issue":"immigration",\
"border security spokesman":"immigration",\
"border study institute":"immigration",\
"border tax proposal":"immigration",\
"border wall funding":"immigration",\
"border wall money":"immigration",\
"border wall prototype":"immigration",\
"borderless world":"immigration",\
"bottom line":"finance",\
"bp":"business",\
"bracket":"finance",\
"brand terrorist":"conflict",\
"brave soldier":"military",\
"breach":"event",\
"breitbart news":"media",\
"brexit vote":"foreignPolicy",\
"brian segee":"environmental",\
"briefer side":"communication",\
"britain":"europeanCountry",\
"broad restriction":"foreignPolicy",\
"broadcast":"media",\
"bruce bennett":"media",\
"bruce cain":"education",\
"bruce kasman":"business",\
"bucknell university":"education",\
"budget deficit":"economy",\
"budget document":"economy",\
"budget process":"economy",\
"budget resolution":"economy",\
"budget resolution deadline":"economy",\
"budget year":"economy",\
"buenos aires":"southAmericanCountry",\
"burden sharing":"immigration",\
"bush administration official":"georgeBush",\
"bush appointee":"georgeBush",\
"business associate":"business",\
"business bankruptcy":"finance",\
"business concern":"business",\
"business dealing area":"business",\
"business economics":"business",\
"business equipment":"business",\
"business holding":"business",\
"business insider":"business",\
"business intersects":"business",\
"business model":"business",\
"business owner":"business",\
"business partners":"business",\
"business people":"business",\
"business person":"business",\
"business professor":"business",\
"business sense":"business",\
"business setback":"business",\
"business tax cut":"taxes",\
"business trip":"business",\
"business trump":"scandal",\
"businessman":"business",\
"businesspeople":"business",\
"buy american plan":"economy",\
"buyer":"business",\
"c40 conference":"environmental",\
"cabinet member":"trumpAdministration",\
"cabinet official":"trumpAdministration",\
"cabinet pick":"trumpAdministration",\
"cable news":"media",\
"cable news network":"media",\
"calculus":"education",\
"calexico":"usCity",\
"california democrats":"usGovernment",\
"california berkeley":"usCity",\
"cameco corp":"business",\
"camp david meeting":"governmentLocation",\
"campaign adviser":"presidentialCampaign",\
"campaign arm":"presidentialCampaign",\
"campaign chairman":"presidentialCampaign",\
"campaign dollar":"presidentialCampaign",\
"campaign manager":"presidentialCampaign",\
"campaign memoir":"presidentialCampaign",\
"campaign official":"presidentialCampaign",\
"campaign pledge trump":"presidentialCampaign",\
"campaign position":"presidentialCampaign",\
"campaign promise":"presidentialCampaign",\
"campaign speech":"presidentialCampaign",\
"campaign talk":"presidentialCampaign",\
"campaign target":"presidentialCampaign",\
"cancer":"medical",\
"candidacy":"presidentialCampaign",\
"candidate hillary clinton":"presidentialCampaign",\
"capital gain tax":"taxes",\
"car attack":"violentCrime",\
"car dealership":"business",\
"car maker":"business",\
"carbon emitter":"environmental",\
"carbon trading":"environmental",\
"care physician":"medical",\
"career":"business",\
"carl c icahn":"entrepreneur",\
"carmen yulin cruz":"usPolitician",\
"carrier corp":"economy",\
"carrier corp factory":"economy",\
"carrier deal":"economy",\
"carrier job cut":"economy",\
"carrier official":"economy",\
"carrier worker":"economy",\
"carter page":"usPolitician",\
"casino":"business",\
"casino magnate phil ruffin":"entrepreneur",\
"catastrophe":"disaster",\
"catos brannon":"immigration",\
"cayman":"finance",\
"cayman islands":"finance",\
"cbo score":"finance",\
"cbp proposal":"immigration",\
"cbs":"media",\
"celebrity golf tournament":"event",\
"central park":"geography",\
"century tax code":"taxes",\
"ceo credibility":"conflict",\
"ceo mark zuckerberg":"entrepreneur",\
"certification":"event",\
"challenge senator":"conflict",\
"challenger":"conflict",\
"chancellor angela merkel":"europeanPolitican",\
"charles sykes":"media",\
"charter flight":"transportation",\
"cheapest":"finance",\
"chemical":"environmental",\
"cheng xiaohe":"education",\
"chicago council":"usGovernment",\
"child care":"employmentBenefit",\
"childcare":"employmentBenefit",\
"china delivers":"foreignPolicy",\
"china development bank":"finance",\
"china expert":"foreignPolicy",\
"china gain credibility":"foreignPolicy",\
"china hawk":"foreignPolicy",\
"chinas militarism means":"foreignPolicy",\
"chinas president xi jinping":"asianPolitician",\
"chinas role":"foreignPolicy",\
"chinas steadfastness":"foreignPolicy",\
"chinas trade policy":"trade",\
"chinas willingness":"foreignPolicy",\
"chinese official":"asianPolitician",\
"chris collins":"usPolitician",\
"chris warren":"athlete",\
"christiana figueres":"southAmericanPolitics",\
"christiane amanpour":"media",\
"christopher steele":"entrepreneur",\
"chuck":"usPolitician",\
"chuck rosenberg":"usPolitician",\
"cia":"usGovernment",\
"circuit decision":"courtSystem",\
"circuit ruling":"courtSystem",\
"civic committee":"usGovernment",\
"civil right":"conflict",\
"clapper laid bare":"scandal",\
"clean":"environmental",\
"climate agreement":"environmentalPolicy",\
"climate change accord":"environmentalPolicy",\
"climate change action":"environmentalPolicy",\
"climate change communication":"environmentalPolicy",\
"climate change jonathan pershing":"environmentalPolicy",\
"climate deal":"environmentalPolicy",\
"climate diplomacy":"environmentalPolicy",\
"climate leader":"environmentalPolicy",\
"climate science center":"environmentalPolicy",\
"climate talk":"environmentalPolicy",\
"clinton administration":"hillaryClinton",\
"clinton campaign":"hillaryClinton",\
"clinton plan":"hillaryClinton",\
"clinton voter":"hillaryClinton",\
"clintons extremist agenda":"conflict",\
"cnbc":"media",\
"cnn analyst":"media",\
"cnn reporter jim acosta":"media",\
"cnn review":"media",\
"cnns":"media",\
"cnns report":"media",\
"coal lease":"environmental",\
"coal mine":"environmental",\
"coal mining":"environmental",\
"coal power":"environmental",\
"coal power coal":"environmental",\
"coal power plant":"environmental",\
"coal production":"environmental",\
"coal shipment":"environmental",\
"coal mining job":"environmental",\
"coastline":"geography",\
"college degree":"education",\
"college student":"education",\
"columbia":"usCity",\
"columbia circuit":"courtSystem",\
"columbia journalism review":"education",\
"columbia universitys center":"education",\
"comcast":"business",\
"comey firing":"event",\
"commander":"peopleRole",\
"commerce department official":"usGovernment",\
"commerce departments inspector general":"usGovernment",\
"committee room":"location",\
"common wealth":"foreignPolicy",\
"comms team":"business",\
"communication director":"usGovernment",\
"communication job":"economy",\
"communication method":"communication",\
"communist china":"foreignPolicy",\
"communist partys congress":"foreignPolicy",\
"community development grant":"economy",\
"community grapple":"conflict",\
"community perspective":"communication",\
"community relation":"communication",\
"companies resulting":"business",\
"company investment":"business",\
"company share":"business",\
"competitive enterprise institutes center":"education",\
"computer simulation":"technology",\
"computer system":"technology",\
"concerned scientists":"environmental",\
"confirmation fight":"conflict",\
"congressional budget office":"usGovernment",\
"congressional hispanic caucus":"usGovernment",\
"congressional official":"usPolitician",\
"congressman mike capuano":"usPolitician",\
"congresss approval":"actOfGovernment",\
"congresss budget process":"actOfGovernment",\
"connecticut democrat":"usPolitician",\
"connecticut gov":"usPolitician",\
"conservation voters":"usGovernment",\
"construction equipment":"economy",\
"construction job":"economy",\
"consulate":"governmentLocation",\
"consumer behavior":"economy",\
"consumer permission":"economy",\
"consumer right":"economy",\
"contribution thousand":"presidentialCampaign",\
"control center":"governmentLocation",\
"control panel factory":"economy",\
"convince voter":"presidentialCampaign",\
"cooperative congressional election study":"education",\
"copenhagen":"europeanCity",\
"core trump supporter":"presidentialCampaign",\
"corn":"agriculture",\
"cornyn":"usPolitician",\
"cornyn spoke":"event",\
"correspondent":"media",\
"cost estimate":"finance",\
"cost restoring community safety act":"domesticPolicy",\
"counterstrike":"military",\
"country independence":"foreignPolicy",\
"country mexico":"foreignPolicy",\
"country withdrawal":"foreignPolicy",\
"country were":"foreignPolicy",\
"court decision":"courtSystem",\
"court nominee":"courtSystem",\
"court ruling":"courtSystem",\
"cox media institute":"education",\
"create job":"economy",\
"credit scenario":"finance",\
"crimea":"europeanGeography",\
"criminal defense attorney alan dershowitz":"courtSystem",\
"crooked hillary":"conflict",\
"crooked hillary clinton":"conflict",\
"cuban":"immigration",\
"cuban exile community":"immigration",\
"cuban americans":"immigration",\
"culinary workers union":"economy",\
"cuomo":"usPolitician",\
"currency":"finance",\
"curry tweet":"communication",\
"customs enforcement":"immigration",\
"cyber capability":"technology",\
"cyber domain":"technology",\
"cyber hacking":"technology",\
"cyberattacks trump":"technology",\
"cyberreview team":"technology",\
"cybersabotage":"technology",\
"cyberthreats thursday":"technology",\
"daca":"daca",\
"daca cover":"immigration",\
"daca permit":"immigration",\
"dakota access pipeline":"environmental",\
"damage lighthizer uncovers":"trade",\
"dannel malloy":"usPolitician",\
"daryl kimball":"arms",\
"david koch":"entrepreneur",\
"david sandalow":"environmental",\
"david sanger":"media",\
"dc court":"courtSystem",\
"dc insider":"media",\
"dcalif":"communication",\
"dean":"education",\
"dearborn":"usCity",\
"debate begin tuesday":"event",\
"debris":"disaster",\
"debris block road":"disaster",\
"debt ceiling":"economy",\
"debt ceiling deal":"economy",\
"debt limit":"economy",\
"december meeting":"event",\
"decree":"event",\
"deepwater horizon oil rig disaster":"environmental",\
"defense agreement":"domesticPolicy",\
"defense attorney":"courtSystem",\
"defense department asia specialist":"foreignPolicy",\
"defense industry official":"business",\
"defense minister":"government",\
"defense program":"nationalSecurity",\
"defiance":"conflict",\
"delaware":"usState",\
"delaware gov":"usPolitician",\
"deliberate":"communication",\
"deliberation":"event",\
"demagogue":"government",\
"democracy promotion":"foreignPolicy",\
"demonstrator":"conflict",\
"denmark":"europeanCountry",\
"denuclearization":"nuclearPolicy",\
"department authority":"usGovernment",\
"dependability":"jobs",\
"deportation proceeding":"immigration",\
"desert town":"geography",\
"destroyer":"military",\
"deterrence capability":"northKorea",\
"deutsche bank debt":"finance",\
"developing policy":"policy",\
"dhs inspector general":"usPolitician",\
"dhs spokeswoman":"borderWall",\
"diane sykes":"courtSystem",\
"dictator":"government",\
"diplomacy fails":"foreignPolicy",\
"dire strait":"immigration",\
"director christopher wray":"media",\
"disarray":"trade",\
"disaster relief funding":"disaster",\
"disaster relief official":"disaster",\
"disaster zone":"disaster",\
"disclosure form":"media",\
"discrepancy":"conflict",\
"discrimination":"conflict",\
"disdain":"conflict",\
"dissent":"conflict",\
"distribute largesse":"jobs",\
"diverse":"conflict",\
"diversity visa lottery":"immigration",\
"djt foundation":"controversy",\
"d massachusetts":"usPolitician",\
"dmitry peskov":"europeanPolitican",\
"d new york":"usPolitician",\
"doctor":"medical",\
"document dump":"russiaElectionHacking",\
"doddfrank act":"economy",\
"dominance":"trait",\
"donald j trump":"presidentDonaldTrump",\
"donald trump jr":"trumpFamily",\
"donald trump resistance":"governmentLocation",\
"donald trumps energy plan":"environmentalPolicy",\
"doublelayer fencing":"immigration",\
"douglas harris":"economy",\
"dow jones":"finance",\
"dozen coal miner":"environmental",\
"dozen lawmaker":"usPolitician",\
"dozen pacific rim nation":"foreignPolicy",\
"dozen us official":"usPolitician",\
"dr joseph mason":"medical",\
"dream":"immigration",\
"dreamer":"immigration",\
"drilling plan":"environmental",\
"drilling zone":"environmental",\
"drug":"medical",\
"drutman":"media",\
"durbin":"usPolitician",\
"duterte":"asianPolitician",\
"dutertes affinity":"foreignPolicy",\
"eagle protection act":"environmentalPolicy",\
"eandenews":"media",\
"earnings":"finance",\
"earth":"environmental",\
"east asia":"geography",\
"eastern district":"geography",\
"economic advisers chairman kevin hassett":"usPolitician",\
"economic cooperation network":"economy",\
"economic dialogue":"economy",\
"economic theory":"economy",\
"economics department":"economy",\
"economics section":"economy",\
"economist mark zandi":"media",\
"economy but":"economy",\
"ed wasserman":"education",\
"edelman trust barometer":"business",\
"education betsy devos":"usPolitician",\
"education opportunity act":"education",\
"educator":"education",\
"edward luce":"media",\
"effigy":"foreignPolicy",\
"efren c olivares":"immigration",\
"eldercare act":"domesticPolicy",\
"election campaign":"presidentialCampaign",\
"election campaign mr trump":"presidentialCampaign",\
"election campaign promise":"presidentialCampaign",\
"election contest":"presidentialCampaign",\
"election interference":"russiaElectionHacking",\
"election issue":"russiaElectionHacking",\
"election operation":"presidentialCampaign",\
"election result":"presidentialCampaign",\
"election voter":"presidentialCampaign",\
"election win":"presidentialCampaign",\
"electoral college":"presidentialCampaign",\
"electronic frontier foundation":"domesticPolicy",\
"embarrassment":"foreignPolicy",\
"rick perry":"usPolitician",\
"emirati business partner hussain sajwani":"middleEastTies",\
"emirati businessman":"middleEastTies",\
"emission limit":"environmental",\
"emissions reduction target priority":"environmental",\
"emmett okeefe":"technology",\
"emoluments clause":"controversy",\
"employee interest":"controversy",\
"encroachment":"foreignPolicy",\
"end filibuster":"courtSystem",\
"end illegal immigration act":"immigration",\
"end illegal immigration act fully funds":"immigration",\
"enemy relationship":"northKorea",\
"energy agency":"environmentalPolicy",\
"energy analyst":"environmentalPolicy",\
"energy clean technology solar":"environmental",\
"energy commission":"environmentalPolicy",\
"arias canete":"environmentalPolicy",\
"energy company":"environmental",\
"energy department report":"environmentalPolicy",\
"energy development":"environmentalPolicy",\
"energy developmentall action":"environmentalPolicy",\
"energy dominance":"environmentalPolicy",\
"energy efficiency equipment online":"environmentalPolicy",\
"energy flourish":"environmental",\
"energy governance system":"environmentalPolicy",\
"energy incentive":"environmentalPolicy",\
"energy infrastructure project":"environmentalPolicy",\
"energy issue":"environmentalPolicy",\
"energy job":"environmental",\
"energy panel":"environmentalPolicy",\
"energy policy":"environmentalPolicy",\
"energy price":"environmentalPolicy",\
"energy provider":"environmentalPolicy",\
"energy regulation":"environmentalPolicy",\
"energy research":"environmentalPolicy",\
"energy show":"environmentalPolicy",\
"energy source":"environmental",\
"energy study":"environmentalPolicy",\
"energy superpower":"environmentalPolicy",\
"energy technology":"environmentalPolicy",\
"energy weakness":"environmentalPolicy",\
"energy worker":"environmentalPolicy",\
"energy and":"environmentalPolicy",\
"engineering job":"economy",\
"enterprise":"daca",\
"envoy xie yesterday":"environmentalPolicy",\
"epicenter":"foreignPolicy",\
"equity giant blackstone":"controversy",\
"eric cantor":"usPolitician",\
"eric trump foundation":"trumpFamily",\
"establishment republicans":"domesticPolicy",\
"estate tax repeal":"taxes",\
"estate technology startup":"technology",\
"ethic reform":"government",\
"euphoria":"business",\
"european":"foreignPolicy",\
"europeans court":"foreignPolicy",\
"evidence russia":"russiaElectionHacking",\
"examine visa program":"immigration",\
"exchange commission":"domesticPolicy",\
"executive power":"presidentDonaldTrump",\
"exemption":"taxes",\
"expiration deadline":"immigration",\
"export good":"trade",\
"export restriction":"trade",\
"export rule":"trade",\
"exxon mobil chief":"controversy",\
"facebook ad":"russiaElectionHacking",\
"faceoff":"controversy",\
"fact coalition":"controversy",\
"fact iea energy head dave turk":"environmentalPolicy",\
"fake news mainstream media":"controversy",\
"fake news media":"controversy",\
"fake news networks":"controversy",\
"fallen americans":"racialProvocation",\
"farflung province":"foreignRelations",\
"farmer":"agriculture",\
"fatigue":"trumpAdministration",\
"fbi headquarters":"government",\
"fbi investigator":"russiaElectionHacking",\
"federal communications commission":"domesticPolicy",\
"federal emergency management agency":"disaster",\
"federal energy regulatory commission":"environmentalPolicy",\
"federal water pollution control act":"environmentalPolicy",\
"federalist society":"courtSystem",\
"felony conviction":"immigration",\
"fema":"disaster",\
"feud":"controversy",\
"fiat chrysler automobiles nv":"business",\
"fidel castro":"southAmericanPolitics",\
"finance unit":"finance",\
"financial times":"media",\
"fired":"controversy",\
"fitness column":"scandal",\
"flake spokesman jason samuels":"media",\
"floor adviser":"government",\
"florida estate":"trumpProperty",\
"rick scott":"usPolitician",\
"florida republicans":"politicalGroup",\
"Marco Rubio":"usPolitician",\
"ford":"business",\
"ford ceo mark fields":"business",\
"ford executive":"business",\
"fords decision":"trade",\
"foreclosure machine":"controversy",\
"foreign affairs committee":"russiaElectionHacking",\
"foreign minister yun byungse":"asianPolitician",\
"foreign relations":"foreignRelations",\
"foreign terrorist entry into":"nationalSecurity",\
"foreigner":"foreignPolicy",\
"former clinton administration treasury secretary lawrence summers":"usPolitician",\
"bill clinton":"billClinton",\
"fort myers":"disaster",\
"four seasons hotel":"location",\
"fox news":"media",\
"abc good morning america":"media",\
"1990s":"trade",\
"ability":"conflict",\
"accord":"foreignPolicy",\
"actionsspeaklouderthanwords":"northKorea",\
"administration budget isnt":"domesticPolicy",\
"affiliate kia motor corp":"trade",\
"afghanistanall muslimmajority nation":"immigration",\
"alabama sen jeff session":"republican",\
"alabama u senate":"democrat",\
"alaska lisa murkowski":"republican",\
"alberta oil":"oil",\
"america defense":"arms",\
"america energy problem":"energy",\
"america void":"climate",\
"america water":"environmentalPolicy",\
"appropriation committee":"borderWall",\
"arizona capital":"usCity",\
"arm control association":"arms",\
"arm regulation":"arms",\
"arm regulation besides":"arms",\
"assertion":"media",\
"attorney general jeff session":"republican",\
"billClinton":"democrat",\
"blindtrust issue a number":"conflict",\
"buenos aire":"conflict",\
"business partner":"conflict",\
"california democrat":"democrat",\
"californiaberkeley":"media",\
"cayman island":"conflict",\
"china militarism mean":"foreignPolicy",\
"china president xi jinping":"china",\
"china role":"china",\
"china steadfastness":"china",\
"china trade policy":"trade",\
"china willingness":"china",\
"clinton extremist agenda":"hillaryClinton",\
"clubforgrowthandheritage":"democrat",\
"coalmining job":"jobs",\
"comment periodwhich":"energy",\
"commerce department inspector general":"commerceSecretary",\
"communist party congress":"china",\
"companiesresulting":"trade",\
"competitive enterprise institute center":"energy",\
"concerned scientist":"energy",\
"congress approval":"energy",\
"congress budget process":"budget",\
"conservation voter":"environmentalPolicy",\
"countrywere":"jobs",\
"cox medium institute":"fakeNews",\
"cubanamericans":"immigration",\
"culinary worker union":"americanBusiness",\
"custom enforcement":"trade",\
"dmassachusetts":"democrat",\
"dnew york":"democrat",\
"donald trump energy plan":"energy",\
"dozen u official":"northKorea",\
"economic adviser chairman kevin hassett":"republican",\
"economybut":"trade",\
"emissionsreduction target priority":"climate",\
"emolument clause":"conflict",\
"end illegal immigration act fullyfunds":"immigration",\
"energy commissioner miguel aria canete":"energy",\
"energyand":"energy",\
"epa clean power plan":"energy",\
"european court":"foreignPolicy",\
"fake news mainstream medium":"fakeNews",\
"fake news medium":"fakeNews",\
"fake news network":"fakeNews",\
"federal communication commission":"domesticPolicy",\
"fiat chrysler automobile nv":"jobs",\
"financial time":"economy",\
"flake spokesman jason samuel":"borderSecurity",\
"fleming experience":"jobs",\
"florida republican":"republican",\
"ford ceo mark field":"americanBusiness",\
"ford decision":"americanBusiness",\
"foreign affair committee":"foreignPolicy",\
"foreign relation":"foreignPolicy",\
"former clinton administration treasury secretary lawrence summer":"democrat",\
"four season hotel":"conflict",\
"fox news executive bill shine":"media",\
"framework convention":"climate",\
"fraud":"media",\
"freddie investment":"economy",\
"freddie mac":"economy",\
"friday sanction":"russiaElectionHacking",\
"fsb diplomatic spat":"russiaElectionHacking",\
"fta":"nafta",\
"fta outright":"nafta",\
"fuel capability":"fuel",\
"fuel industry stooge":"fuel",\
"fuel production":"fuel",\
"fuel source":"fuel",\
"fuel technology company":"fuel",\
"funding need":"borderWall",\
"funding package":"budget",\
"funding request":"borderWall",\
"fundraising activity":"conflict",\
"fundraising operation":"conflict",\
"furnace production job":"jobs",\
"g20 summit":"foreignPolicy",\
"g20 summit confront":"foreignPolicy",\
"gain tax":"taxes",\
"gallup":"presidentialElection",\
"gallup poll":"presidentialElection",\
"gamesmanship":"russiaElectionHacking",\
"gang ms13":"daca",\
"gary kalman":"conflict",\
"gas company":"naturalGas",\
"gas exploration":"naturalGas",\
"gas leasing program":"naturalGas",\
"gas power plant":"naturalGas",\
"gasoline price":"fuel",\
"gavin newsom":"democrat",\
"general dynamic corp":"americanBusiness",\
"general electric":"americanBusiness",\
"general mcmaster line":"americanBusiness",\
"general motor co":"americanBusiness",\
"geng shuang":"china",\
"george f kennan":"northKorea",\
"george papadopoulos":"trumpAdministration",\
"george w bush presidency":"georgeBush",\
"george w bushera level":"georgeBush",\
"george w bushera rhetoric":"georgeBush",\
"george washington university law school":"domesticPolicy",\
"georgetown":"conflict",\
"glenn simpson":"russiaElectionHacking",\
"global affair":"trade",\
"global energy policy":"energy",\
"godwins law":"fakeNews",\
"golden state warrior":"controversy",\
"goldman sachs":"conflict",\
"good deficit":"trade",\
"gop candidate":"republican",\
"gop coalition":"republican",\
"gop conference meeting":"republican",\
"gop congress":"republican",\
"gop control":"republican",\
"gop conundrum":"republican",\
"gop credit":"republican",\
"gop fortune":"republican",\
"gop hand":"republican",\
"gop holdout":"republican",\
"gop priority":"republican",\
"gop proposal":"republican",\
"gop rhetoric":"republican",\
"gop takeover":"republican",\
"gopheld house seat":"republican",\
"gore":"democrat",\
"gorsuchs":"supremeCourtJudge",\
"gorsuchs ability":"supremeCourtJudge",\
"gorsuchs confirmation hearing":"supremeCourtJudge",\
"gorsuchs nomination":"supremeCourtJudge",\
"government accountability office":"borderWall",\
"government agency":"energy",\
"government approach":"arms",\
"government employee":"conflict",\
"government ethic":"conflict",\
"government ethic form":"controversy",\
"government ethic office":"controversy",\
"government ethic rule":"controversy",\
"government fund":"education",\
"government funding":"borderWall",\
"government funding bill":"borderWall",\
"government general service administration":"conflict",\
"government intrusion":"climate",\
"government leader":"foreignPolicy",\
"government official":"trade",\
"government operative":"russiaElectionHacking",\
"government oversight":"jobs",\
"government participation":"americanBusiness",\
"government regulation":"energy",\
"government responsibility":"conflict",\
"government source":"arms",\
"government spending":"military",\
"government technology":"conflict",\
"governor mansion":"democrat",\
"governor race":"democrat",\
"governor responsibility":"democrat",\
"grady newsource":"media",\
"grassley beforehand":"russiaElectionHacking",\
"great wall":"borderWall",\
"green supply chain":"climate",\
"greenhouse emission":"climate",\
"greenhouse gas emitter":"climate",\
"greenpeace china":"climate",\
"greenpeace usa":"climate",\
"greg valliere":"taxes",\
"grenada":"climate",\
"groundwater":"energy",\
"group earthjustice":"climate",\
"growth strategy":"trade",\
"guam":"northKorea",\
"guatemala":"immigration",\
"gulf coast":"energy",\
"gulf state":"energy",\
"gun maker":"arms",\
"gunman":"economy",\
"gwenda blair":"media",\
"habitat":"energy",\
"hacking allegation":"russiaElectionHacking",\
"hacking tool":"russiaElectionHacking",\
"hamburg police":"foreignPolicy",\
"hamidreza taraghi":"iran",\
"hannity":"media",\
"hardworking american":"taxes",\
"harvard business school":"americanBusiness",\
"harvard law school":"education",\
"harvard school":"climate",\
"harvard university robert stavins":"climate",\
"harvey":"disaster",\
"hassan rouhani":"iran",\
"hate group":"conflict",\
"havana":"cuba",\
"hawaii attorney general":"immigration",\
"headline trump":"media",\
"health benefit":"healthcare",\
"health bill":"healthcare",\
"health care act":"healthcare",\
"health care debate":"healthcare",\
"health care dollar":"healthcare",\
"health care law":"healthcare",\
"health care legislation":"healthcare",\
"health care product":"healthcare",\
"health care repeal effort":"healthcare",\
"health insurance":"healthcare",\
"health insurance program":"healthcare",\
"health plan":"healthcare",\
"health policy expert":"healthcare",\
"health policy goal":"healthcare",\
"health service":"healthcare",\
"health system":"healthcare",\
"healthcare":"healthcare",\
"heath shuler":"usPolitician",\
"heather heyer":"violentCrime",\
"heating assistance":"domesticPolicy",\
"hegemony":"government",\
"dean heller":"usPolitician",\
"heritage foundation":"policy",\
"highpaying job":"economy",\
"highway bill":"domesticPolicy",\
"hill member":"politicalGroup",\
"hillary":"hillaryClinton",\
"hindu temple":"religiousSite",\
"hiring process":"economy",\
"hofstra university":"education",\
"homeland security discretion":"nationalSecurity",\
"homeland security travel ban":"nationalSecurity",\
"honduran":"immigration",\
"hospital":"medical",\
"house appropriation committee":"politicalGroup",\
"democrat":"democrat",\
"house freedom caucus":"domesticPolicy",\
"house gop conference":"domesticPolicy",\
"house intelligence committee":"russiaElectionHacking",\
"house leader":"governmentPosition",\
"house republican caucus":"domesticPolicy",\
"house version":"domesticPolicy",\
"housing":"economy",\
"hurt business":"economy",\
"hydroelectric":"energy",\
"hyundai motor co":"southKorea",\
"icbm":"northKorea",\
"ice":"immigration",\
"ice agent":"immigration",\
"ice removal authority":"immigration",\
"ieas world energy investment report":"energy",\
"imbalance":"immigration",\
"immigrant legal resource center":"immigration",\
"immigrant work":"immigration",\
"immigration attorney":"immigration",\
"immigration authority":"immigration",\
"immigration barrier":"immigration",\
"immigration deal":"immigration",\
"immigration enforcer":"immigration",\
"immigration hardliner":"immigration",\
"immigration officer":"immigration",\
"immigration order":"immigration",\
"immigration policy":"immigration",\
"immigration reform package":"immigration",\
"immigration reform proposal":"immigration",\
"immigration system":"immigration",\
"immigration tends":"immigration",\
"import restriction":"trade",\
"imprisonment":"russiaElectionHacking",\
"incentive package":"jobs",\
"income tax bracket":"taxes",\
"income tax filing":"taxes",\
"incoming donald trump administration":"trumpAdministration",\
"incoming president":"presidentDonaldTrump",\
"incumbent":"barackObama",\
"independent business":"americanBusiness",\
"india":"india",\
"indiana factory":"americanBusiness",\
"indiana official":"jobs",\
"indiana plant":"jobs",\
"indiana town":"jobs",\
"indictment":"russiaElectionHacking",\
"influence campaign":"russiaElectionHacking",\
"inhabitant":"northKorea",\
"institution stock":"conflict",\
"insurance executive":"healthcare",\
"insurance policy":"healthcare",\
"insurer offering obamacare":"healthcare",\
"intelligence":"russiaElectionHacking",\
"intelligence community finding":"russiaElectionHacking",\
"intelligence community work":"russiaElectionHacking",\
"intelligence officer":"russiaElectionHacking",\
"intelligence official":"russiaElectionHacking",\
"intelligence report":"russiaElectionHacking",\
"intelligence service":"russiaElectionHacking",\
"intelligence service mi6":"russiaElectionHacking",\
"interior department":"energy",\
"interior rule":"energy",\
"international economics":"trade",\
"international energy agency":"energy",\
"international trafficking":"arms",\
"internet meme":"media",\
"interview president donald trump":"russiaElectionHacking",\
"intimidation effect":"trumpCommunication",\
"investigation uncovers":"trade",\
"investment decision":"trade",\
"investment research group":"borderWall",\
"investment tax":"taxes",\
"investor interest":"taxes",\
"investor wilbur ross":"commerceSecretary",\
"iran agreement":"iran",\
"iran deal":"iran",\
"iran economy":"iran",\
"iran foreign ministry":"iran",\
"iran islamic establishment":"iran",\
"iran president":"iran",\
"isi threat":"immigration",\
"islamic revolution":"immigration",\
"islamic state militant":"immigration",\
"islamic terror":"conflict",\
"islandbuilding":"china",\
"itar":"arms",\
"itc commissioner":"trade",\
"jack markell":"democrat",\
"james b comey":"fbiDirector",\
"james comey":"fbiDirector",\
"jared kushner":"trumpAdministration",\
"jeremiad":"trade",\
"jerry brown":"democrat",\
"jim scuitto":"media",\
"job creation agenda":"jobs",\
"job cut":"jobs",\
"job generator":"jobs",\
"job loss":"jobs",\
"job number":"jobs",\
"job opportunity":"jobs",\
"job outflow":"jobs",\
"job retention":"jobs",\
"john boehner":"republican",\
"joint security area":"northKorea",\
"jong un sit":"northKorea",\
"judge confirmation process":"supremeCourtJudge",\
"judge james robart":"supremeCourtJudge",\
"judge robart":"supremeCourtJudge",\
"judiciary":"supremeCourtJudge",\
"justice anthony m kennedy":"supremeCourtJudge",\
"justice antonin scalia":"supremeCourtJudge",\
"justice department investigation":"russiaElectionHacking",\
"justice department veteran":"russiaElectionHacking",\
"justice kennedy":"supremeCourtJudge",\
"justice kennedy president trump":"supremeCourtJudge",\
"justice ruth bader ginsburg":"supremeCourtJudge",\
"justice scalia":"supremeCourtJudge",\
"justice stephen breyer":"supremeCourtJudge",\
"keystone pipeline":"energy",\
"kgb man":"russiaElectionHacking",\
"kkk":"racialProvocation",\
"kim jonghoon":"northKorea",\
"koo zayong":"trade",\
"korea automobile manufacturer association":"trade",\
"korea trade minister":"trade",\
"korean peninsula problem":"southKorea",\
"kremlin":"russiaElectionHacking",\
"kremlin involvement":"russiaElectionHacking",\
"kremlin spokesman dmitr peskov":"russiaElectionHacking",\
"kremlin spokesman dmitry peskov":"russiaElectionHacking",\
"kremlin website":"russiaElectionHacking",\
"kulagin":"russiaElectionHacking",\
"kuwait":"conflict",\
"kuwaiti event":"conflict",\
"kyle pomerleau":"taxes",\
"labor department figure":"economy",\
"labor market":"economy",\
"labor secretary alexander acosta":"economy",\
"labor union":"economy",\
"land force":"military",\
"laredo":"borderWall",\
"latino heavy electorate":"presidentialCampaign",\
"law enforcement":"lawEnforcement",\
"law firm":"courtSystem",\
"lawyer mr trump":"scandal",\
"legislature":"policy",\
"lender economist":"economy",\
"lester holt":"media",\
"leon panetta":"hillaryClinton",\
"leon rodriguez":"immigration",\
"liar":"conflict",\
"hate":"conflict",\
"lightbridge corp":"nuclearPolicy",\
"little havana":"cuba",\
"lobbying ban":"domesticPolicy",\
"lockheed martin":"arms",\
"lowercourt pick":"courtSystem",\
"lt gov":"usPolitician",\
"lu chao":"foreignRelations",\
"lunacy":"conflict",\
"mauricio macri":"southAmericanPolitics",\
"macroeconomics advisor":"economy",\
"magazine":"media",\
"mahmoud ahmadinejad":"middleEasternPolitics",\
"manuel artime theater":"cuba",\
"marcher":"conflict",\
"marcoRubio":"usPolitician",\
"marine":"military",\
"marine one":"transportation",\
"marketing":"media",\
"stock market":"finance",\
"marshall plan":"foreignPolicy",\
"martin luther king jr day weekend":"racialProvocation",\
"mass transit":"domesticPolicy",\
"mcclatchy news website":"media",\
"medicade":"domesticPolicy",\
"medicine":"medical",\
"media":"media",\
"melaniaTrump":"trumpFamily",\
"barack obama":"barackObama",\
"mentalhealth care":"domesticPolicy",\
"merchandise trade deficit":"trade",\
"methane":"environmental",\
"mexico economy ministry":"trade",\
"mexico factory":"trade",\
"mexico pay":"borderWall",\
"mexico regardless":"foreignRelations",\
"michael cohen":"trumpAdministration",\
"michael flynn":"usPolitician",\
"michael short":"trumpAdministration",\
"michigan factory":"economy",\
"mick mulvaney":"usPolitician",\
"middle east":"middleEast",\
"mike lee":"usPolitician",\
"militant":"military",\
"military":"military",\
"mining industry":"economy",\
"minister joo hyunghwan":"southKorea",\
"minority turnout":"racialProvocation",\
"minority voter":"racialProvocation",\
"misdiagnosis":"medical",\
"missile":"northKorea",\
"mitch mcconnell":"usPolitician",\
"model trade agreement":"trade",\
"mohammad javad zarif":"middleEasternPolitics",\
"money laundering":"scandal",\
"monopoly":"business",\
"monster storm":"disaster",\
"mark zandi":"economy",\
"morning intelligence briefing":"government",\
"morning twitter offensive":"communication",\
"fannie mae":"finance",\
"mortgage interest":"finance",\
"moscowdirected hacking":"russiaElectionHacking",\
"jim mattiss":"trumpAdministration",\
"mr obamas cuba policy":"cuba",\
"mr trump campaign":"trumpCampaign",\
"mr trump supreme court nominee":"supremeCourtJudge",\
"mr trump twitter message":"trumpCommunication",\
"msnbc channel":"media",\
"msnbc tv host mika brzezinski":"media",\
"mueller russia probe washington anticipating":"russiaElectionHacking",\
"multinationalization":"foreignPolicy",\
"mumbai":"india",\
"munition":"arms",\
"muslim ban":"immigration",\
"muslim ban a registry":"immigration",\
"muslim country":"immigration",\
"muslim immigrant":"immigration",\
"muslim leader":"immigration",\
"muslim living":"immigration",\
"muslim population":"immigration",\
"nafta pact":"nafta",\
"nancy":"democrat",\
"nancy pelosi":"democrat",\
"naples":"italy",\
"national assembly":"northKorea",\
"national endowment":"budget",\
"national enquirer":"media",\
"national environmental policy act":"environmentalPolicy",\
"national immigration law center":"immigration",\
"national labor relation board":"jobs",\
"national security entryexit program":"immigration",\
"national security official":"russiaElectionHacking",\
"national security policy":"immigration",\
"nato member":"foreignPolicy",\
"natural resource defense council":"environmentalPolicy",\
"naureen shah":"immigration",\
"nazi comparison":"fakeNews",\
"nbc news analyst":"media",\
"negotiation upwards":"taxes",\
"new america foundation":"immigration",\
"new leak":"russiaElectionHacking",\
"new orleans":"usCity",\
"new start treaty":"nuclear",\
"new zealand":"foreignPolicy",\
"news briefing":"media",\
"news coverage":"media",\
"news item":"media",\
"news property":"media",\
"news release":"media",\
"news report":"media",\
"news story":"media",\
"nfl tweet":"trumpCommunication",\
"nicaragua":"immigration",\
"nicaraguan":"immigration",\
"nih":"borderWall",\
"nikki haley":"foreignPolicy",\
"nominee hillary clinton":"hillaryClinton",\
"nondisclosure agreement":"controversy",\
"north ability":"northKorea",\
"north korea expert":"northKorea",\
"north korea launch site":"northKorea",\
"north korea leader":"northKorea",\
"north korea menace":"northKorea",\
"north korea missile":"northKorea",\
"north korea missile launch":"northKorea",\
"north korea policy":"northKorea",\
"north korea problem":"northKorea",\
"north korea situation":"northKorea",\
"nseers program":"immigration",\
"nuclear nonproliferation treaty":"nuclear",\
"nuke":"nuclear",\
"obama administration deferred action":"daca",\
"obama administration policy":"barackObama",\
"obama presidency":"barackObama",\
"obama regulation":"barackObama",\
"obama year":"barackObama",\
"obamacare benchmark plan":"healthcare",\
"obamacare health plan":"healthcare",\
"obamacare protection":"healthcare",\
"obamacare repeal":"healthcare",\
"obamacare requirement":"healthcare",\
"obamacares":"healthcare",\
"obamacares requirement":"healthcare",\
"obamacares washingtondriven":"healthcare",\
"obamaclinton roadblock":"healthcare",\
"obamaera":"barackObama",\
"obamaera climate change regulation":"climate",\
"obamaera policy":"barackObama",\
"obamas choice":"barackObama",\
"obamas clean power plan":"energy",\
"obamas climate policy":"climate",\
"obamas decision":"barackObama",\
"obamas legacy":"barackObama",\
"obamas term":"barackObama",\
"obamas veto":"barackObama",\
"obstruction":"russiaElectionHacking",\
"ocean":"energy",\
"officeofmanagementandbudget":"budget",\
"offshore wind farm":"energy",\
"offshoring act establishes":"environmentalPolicy",\
"oil company":"oil",\
"oil drillers":"oil",\
"oil drilling oil drilling":"oil",\
"oil industry":"oil",\
"oil pipeline":"oil",\
"oil price":"oil",\
"oil reserve":"oil",\
"oil spill":"disaster",\
"oped":"northKorea",\
"opposition agenda":"democrat",\
"oval office meeting":"russiaElectionHacking",\
"oval office time":"russiaElectionHacking",\
"pacific pact":"trade",\
"paris agreementthe accord":"climate",\
"paris climate change agreement":"climate",\
"paris climatechange commitment":"climate",\
"paris withdrawal":"climate",\
"party goal":"healthcare",\
"party member":"healthcare",\
"party organization":"healthcare",\
"party view":"controversy",\
"party voter":"healthcare",\
"partyasorganization":"healthcare",\
"partyasorganization group":"healthcare",\
"pas something":"taxes",\
"passage middle class tax relief":"taxes",\
"patrol agent":"borderWall",\
"paul ryan":"republican",\
"peninsula issue":"northKorea",\
"pentagon strategist":"northKorea",\
"people army":"northKorea",\
"permit application":"energy",\
"peskov":"russiaElectionHacking",\
"plant job":"jobs",\
"playboy centerfold model":"controversy",\
"plentiful job":"jobs",\
"policy address":"foreignPolicy",\
"politico report":"media",\
"politifact":"media",\
"polluter":"environmentalPolicy",\
"postelection rally":"presidentialCampaign",\
"power capacity investment":"environmentalPolicy",\
"power generation":"environmental",\
"power grab":"conflict",\
"power influence":"conflict",\
"power line":"energy",\
"power plant emission limit":"environmentalPolicy",\
"power sector":"energy",\
"power source":"energy",\
"predatory lending practice":"finance",\
"predicament":"conflict",\
"premium increase":"finance",\
"president attack":"controversy",\
"obamacare":"healthcarePolicy",\
"president campaign promise":"presidentialCampaign",\
"president campaign sticker":"presidentialCampaign",\
"president comment":"communication",\
"trumpAdministration":"trumpAdministration",\
"president moon jaein":"southKorea",\
"president park geunhye":"southKorea",\
"president trade vision":"trade",\
"xi jinping":"china",\
"kellyanne conway":"trumpAdministration",\
"press briefing":"communication",\
"press coverage":"media",\
"press report":"media",\
"preventive war":"northKorea",\
"primary":"presidentialElection",\
"prime minister":"foreignRelations",\
"privacy advocate":"technology",\
"privacy framework":"technology",\
"privatesector job":"economy",\
"production worker":"economy",\
"profit margin":"finance",\
"proimmigration policy":"immigration",\
"project capital":"finance",\
"property presidentelect donald trump":"trumpProperty",\
"prosecution":"conflict",\
"public health":"healthcare",\
"public policy":"domesticPolicy",\
"publicsafety threat":"nationalSecurity",\
"puerto rico":"puertoRico",\
"pullout will undermine us":"nafta",\
"ann coulter":"media",\
"vladimir putin":"vladimirPutin",\
"quota restriction":"trade",\
"rachel maddow":"media",\
"racist":"racialProvocation",\
"radio show":"media",\
"rape":"violentCrime",\
"raytheon co":"business",\
"reality star":"media",\
"reality tv star":"media",\
"recepErdogan":"middleEasternPolitics",\
"recovery crew":"disaster",\
"redirects education dollar repeal":"domesticPolicy",\
"redstate senator":"politicalGroup",\
"reelection bid":"presidentialCampaign",\
"refinery":"environmental",\
"refuge":"refugeeCrisis",\
"refusal":"conflict",\
"regulation":"policy",\
"relation war":"conflict",\
"renegade republican":"politicalGroup",\
"renegotiation":"communication",\
"repatriation":"economy",\
"repeal bill":"domesticPolicy",\
"republic":"government",\
"republican ahca bill":"healthcarePolicy",\
"republican bill":"domesticPolicy",\
"republican":"republican",\
"republican health care bill":"healthcarePolicy",\
"republicanleaning mountain town":"presidentialElection",\
"repudiation":"conflict",\
"residency":"immigration",\
"restraining order":"conflict",\
"resurgent authoritarianism":"government",\
"retired united steelworker local":"economy",\
"rex tillerson":"usPolitician",\
"ria news agency":"media",\
"rickScott":"usPolitician",\
"rnc":"presidentialElection",\
"robert dallek":"russiaElectionHacking",\
"rodrigo duterte":"asianPolitician",\
"rogue nation":"conflict",\
"rogue state":"conflict",\
"ronald reagan":"taxes",\
"rossnavarro tax credit":"taxes",\
"phill ruffin":"controversy",\
"rumor":"controversy",\
"russiaElectionHacking":"russiaElectionHacking",\
"borderWall":"borderWall",\
"deanHeller":"republican",\
"genocide":"disaster",\
"hillaryClinton":"hillaryClinton",\
"homeland security secretary elaine duke":"trumpAdministration",\
"homeland security secretary kirstjen nielsen":"trumpAdministration",\
"house freedomcaucus":"healthcare",\
"james robart":"trumpCommunication",\
"medium outlet":"media",\
"medium site":"media",\
"nigel farage":"energy",\
"northKorea":"northKorea",\
"pentagon boost":"budget",\
"salvadoran":"daca",\
"san luis potosi":"trade",\
"sanctuary city":"immigration",\
"saudi campaign":"arms",\
"scalia vacancy":"supremeCourtJudge",\
"scaramuccis appointment":"supremeCourtJudge",\
"scaramuccis view":"supremeCourtJudge",\
"sean hannity":"media",\
"seat for human right":"arms",\
"seattle":"usCity",\
"secret service":"conflict",\
"secret service detail":"conflict",\
"secretary john kelly":"trumpAdministration",\
"secure fence act":"borderWall",\
"security activity":"borderWall",\
"security adviser michael flynn":"trumpAdministration",\
"security assistance officer":"arms",\
"security council":"northKorea",\
"security perspective":"trade",\
"security problem":"northKorea",\
"security secretary john kelly":"trumpAdministration",\
"security service":"cuba",\
"security situation":"climate",\
"security threat":"trade",\
"sen dean heller":"republican",\
"sen marco rubio":"republican",\
"sen ted cruz":"republican",\
"senate fight":"supremeCourtJudge",\
"senate floor procedure":"supremeCourtJudge",\
"senate gop":"republican",\
"senate health bill":"healthcare",\
"senate intelligence committee":"russiaInvestigation",\
"senate majority leader mitch mcconnell land":"republican",\
"senate minority whip dick durbin":"borderWall",\
"senator john mccain":"russiaElectionHacking",\
"senator lindsey graham":"russiaElectionHacking",\
"senator maggie hassan":"offshoreDrilling",\
"senator patrick j leahy":"borderWall",\
"sergey i kislyak":"russiaInvestigation",\
"sergey v lavrov":"russiaInvestigation",\
"shopturnedcapitol hill power broker":"freedomCaucus",\
"showdown":"borderWall",\
"sibur":"conflict",\
"sierra club":"offshoreDrilling",\
"signature border wall":"borderWall",\
"signature campaign promise":"borderWall",\
"singapore":"trade",\
"situation room discussion":"northKorea",\
"skybridge capital":"trumpStaffing",\
"slash tax":"taxes",\
"slavery sits":"controversy",\
"smartassetcom":"taxes",\
"sofla community":"haiti",\
"solarworld":"energy",\
"solicitor gen jeffrey wall":"travelBan",\
"something majority leader mitch mcconnell":"immigration",\
"south asia":"arms",\
"south korea neighbor japan":"southKorea",\
"south korea soldier":"southKorea",\
"south korea trade minister":"southKorea",\
"south korean":"southKorea",\
"soviet republic":"russia",\
"sparring partner":"trumpOpposition",\
"speaker anthony rendon":"trumpOpposition",\
"speaker paul ryan":"republican",\
"speaker ryan":"republican",\
"spending crisis":"americanBusiness",\
"spending package":"budget",\
"spending tap":"americanBusiness",\
"spokesman jason miller":"immigration",\
"spy chief":"russiaelectionHacking",\
"spying organisation":"russiaInvestigation",\
"st petersburg":"russiaInvestigation",\
"staff member":"trumpStaffing",\
"staffing challenge":"trumpStaffing",\
"staffing exodus":"trumpStaffing",\
"standing rock sioux tribe":"oil",\
"standout campaign promise":"borderWall",\
"startups":"americanBusiness",\
"state address":"trumpOpposition",\
"state attorney":"turmpOpposition",\
"state john kerry":"russiaElectionHacking",\
"state legislature":"trumpOpposition",\
"state legislature california":"trumpOpposition",\
"state party email":"trumpOpposition",\
"state rex w tillerson":"republican",\
"state tax break":"taxes",\
"statesman":"northKorea",\
"steel purchase":"borderWall",\
"stephanie clifford":"controversy",\
"stephen a schwarzman":"controversy",\
"stephen curry":"conflict",\
"stephen g breyer":"supremeCourtJudge",\
"stephen k bannon":"northKorea",\
"steveScalise":"supremeCourtJudge",\
"stimson center":"arms",\
"stock gain":"economy",\
"stock market price":"economy",\
"stockmarket rally":"economy",\
"stopgap measure":"disaster",\
"stopping north korea":"northKorea",\
"submarine":"tradeDeficit",\
"subsidy":"energy",\
"sucker game":"economy",\
"suicide":"iranNuclear",\
"suniva":"solar",\
"support majority leader mitch mcconnells bill":"healthcare",\
"support research":"southKorea",\
"supreme court arm":"supremeCourtJudge",\
"supreme court decision":"immigration",\
"supreme court justice":"supremeCourtJudge",\
"supreme court pick":"supremeCourtJudge",\
"supreme court vacancy":"supremeCourtJudge",\
"surveillance":"russiaInvestigation",\
"survey monkey poll":"healthcare",\
"susan e rice":"obamaAdministration",\
"suspension":"travelBan",\
"sykes":"media",\
"tabloid newspaper didnt publish":"media",\
"taiwan amid":"asia",\
"tax benefit":"taxes",\
"tax bill":"taxes",\
"tax code complete":"taxes",\
"tax code cost american million":"taxes",\
"tax deferral":"taxes",\
"tax didnt":"taxes",\
"tax foundation":"taxes",\
"tax incentive":"taxes",\
"tax measure":"taxes",\
"tax policy center":"taxes",\
"tax receipt":"taxes",\
"tax reform blueprint":"taxes",\
"tax reform law":"taxes",\
"tax reform plan":"taxes",\
"tax relief":"taxes",\
"tax return":"taxes",\
"tax system":"taxes",\
"taxpayer buck":"taxes",\
"taxpayer funding":"taxes",\
"tea party":"politicalGroup",\
"tech giant apple":"technology",\
"technology company":"technology",\
"ted cruz":"republican",\
"television today":"media",\
"term limit":"government",\
"terrorism":"violentCrime",\
"threat mount":"nationalSecurity",\
"toll road deal":"economy",\
"tourism industry":"economy",\
"toyota motor corp":"business",\
"tpp":"trade",\
"trade balance":"tradeDeficit",\
"trade case":"trade",\
"trade clinton":"trade",\
"trade conflict":"trade",\
"trade crackdown":"trade",\
"trade decision":"trade",\
"trade expansion act":"trade",\
"trade expert":"trade",\
"trade fight":"trade",\
"trade friction":"trade",\
"trade group":"trade",\
"trade meeting":"trade",\
"trade pact":"trade",\
"trade partner":"trade",\
"trade practice":"trade",\
"trade relation":"trade",\
"trade relationship":"trade",\
"trade surplus":"trade",\
"trade tension":"trade",\
"trading system":"trade",\
"transmission organization":"environmental",\
"trash talk":"communication",\
"travel ban case":"travelBan",\
"treaty":"trade",\
"troop readiness":"military",\
"trooper jay cullen":"police",\
"trump ally":"politicalGroup",\
"trump america first energy plan":"environmentalPolicy",\
"trump campaign infrastructure tax":"presidentialCampaign",\
"trump epa":"environmentalPolicy",\
"trump katrina":"disaster",\
"trump national security council":"nationalSecurity",\
"trump opposition movement":"trumpOpposition",\
"trump paris exit":"environmentalPolicy",\
"trump paris stance":"environmentalPolicy",\
"trump state":"presidentialElection",\
"trump supporters1":"presidentialElection",\
"trump taj mahal casino":"trumpProperty",\
"trump target audience":"presidentialCampaign",\
"trump tower buenos aire":"trumpProperty",\
"trump university":"controversy",\
"trump vineyard estate":"trumpProperty",\
"trump win":"presidentialElection",\
"trumpera energy framework":"environmentalPolicy",\
"tulane university":"education",\
"twitter":"communication",\
"u policy towards north korea":"northKorea",\
"u presidency":"government",\
"u supreme court":"supremeCourtJudge",\
"u taxpayer":"taxes",\
"u troop":"military",\
"uc berkeley goldman school":"education",\
"un climate change program":"environmentalPolicy",\
"un climate process":"environmentalPolicy",\
"united nations":"foreignRelations",\
"unemployment":"economy",\
"unfccc":"environmentalPolicy",\
"united state economy":"economy",\
"united state exit":"policy",\
"united state position":"foreignRelations",\
"united state tax":"taxes",\
"uprising":"conflict",\
"uranium":"nuclear",\
"us ally":"foreignRelations",\
"us arm":"arms",\
"us arm sale":"arms",\
"us auto industry job":"economy",\
"us car":"economy",\
"us census bureau":"usGovernment",\
"us china":"foreignPolicy",\
"us corporation":"business",\
"us credibility":"foreignRelations",\
"us defense security cooperation agency":"nationalSecurity",\
"us dollar":"finance",\
"us election":"presidentialElection",\
"us embassy":"usGovernment",\
"us emission target":"environmentalPolicy",\
"us environmental protection agency":"environmental",\
"us auto industry":"economy",\
"us house":"usGovernment",\
"us influence":"foreignRelations",\
"us infrastructure spending":"economy",\
"us international trade commission":"trade",\
"us manufacturing":"economy",\
"us misunderstanding":"conflict",\
"us policy":"policy",\
"us power":"foreignRelations",\
"us relationship":"foreignRelations",\
"us sanction":"trade",\
"us special envoy":"foreignRelations",\
"us state department":"usGovernment",\
"us supreme court":"supremeCourtJudge",\
"us trade":"trade",\
"us trade deficit decline":"tradeDeficit",\
"us trade gap":"tradeDeficit",\
"us trade law":"trade",\
"us trading partner":"trade",\
"us weapon industry":"arms",\
"us wind power industry":"environmental",\
"usborn":"immigration",\
"usc":"education",\
"uschina relationship":"china",\
"uschina strategic":"china",\
"vehicle barrier":"violentCrime",\
"veteran":"military",\
"victim":"violentCrime",\
"victoria university":"education",\
"video":"communication",\
"violation":"conflict",\
"virginia state trooper":"police",\
"vpn":"technology",\
"visa program":"immigration",\
"voter":"presidentialElection",\
"voicemail":"communication",\
"vulgar word choice":"controversy",\
"wa trump paris exit good politics":"environmentalPolicy",\
"wall street":"finance",\
"warhead stockpile":"nuclearPolicy",\
"warship":"military",\
"washingtonDC":"government",\
"wastewater":"environmental",\
"watchdog group":"conflict",\
"water quality":"environmental",\
"wealthy":"finance",\
"weapons":"arms",\
"web site":"technology",\
"week news":"media",\
"welfare":"economy",\
"whirlpool":"business",\
"white house aide":"governmentPosition",\
"white house budget director":"governmentPosition",\
"white house communication director":"governmentPosition",\
"white house communication staff":"governmentPosition",\
"white house email":"communication",\
"white house ethic lawyer":"governmentPosition",\
"white house insider":"governmentPosition",\
"white house intern":"governmentPosition",\
"white house job":"governmentPosition",\
"white house national trade council":"trade",\
"white house official announcement":"communication",\
"white house press":"communication",\
"white house spokeswoman":"governmentPosition",\
"white house trade official":"trade",\
"wind power":"energy",\
"wmaq":"media",\
"work authorization":"immigration",\
"work force":"economy",\
"world affair":"foreignRelations",\
"world bank":"finance",\
"world trade organization":"trade",\
"year budget resolution":"finance",\
"year outer continental shelf oil":"oil",\
"year term":"government",\
"yonsei university graduate school":"education",\
"acosta":"fakeNews",\
"adversary":"foreignPolicy",\
"affidavit":"russiaInvestigation",\
"africa":"racialProvocation",\
"ahca":"healthcare",\
"alliance":"energy",\
"aluminum import":"trade",\
"amendment":"budget",\
"america first":"budget",\
"american president":"foreignPolicy",\
"appropriation":"budget",\
"appropriation bill":"budget",\
"arctic":"energy",\
"arrest":"immigration",\
"asheville":"trumpOpposition",\
"assange":"russiaElectionHacking",\
"associated press":"media",\
"auto industry":"trade",\
"benefitcost ratio":"americanBusiness",\
"bigotry":"racialProvocation",\
"bitch":"racialProvocation",\
"blair":"media",\
"blasio":"trumpOpposition",\
"blowback":"trade",\
"bombast":"trumpCommunication",\
"bond":"racialProvocation",\
"book tour":"media",\
"budget blueprint":"budget",\
"budget committee":"budget",\
"bureaucracy":"nuclear",\
"business confidence":"economy",\
"cabinet secretary":"trumpAdministration",\
"carbon dioxide":"energy",\
"caucus":"trumpOpposition",\
"central america":"daca",\
"certificate":"conflict",\
"chamber rule":"supremeCourtJudge",\
"charter school":"education",\
"chiefofstaff john kelly":"trumpStaff",\
"climate action":"climate",\
"climate hero":"climate",\
"coal miner":"climate",\
"cohn":"trade",\
"commerce department report":"tradeGap",\
"computer server":"russiaElectionHacking",\
"condemnation":"racialProvocation",\
"connecticut":"trumpOpposition",\
"consistency":"northKorea",\
"constituent":"healthcare",\
"contractor":"borderWall",\
"country very carefully":"travelBan",\
"crude oil":"oil",\
"curry":"racialProvocation",\
"cyberthreats":"russiaInvestigation",\
"database":"immigration",\
"defense jim mattis":"northKorea",\
"delay":"russiaElectionHacking",\
"delury":"northKorea",\
"dershowitz":"russiaInvestigation",\
"deutsche bank":"conflict",\
"divestiture":"conflict",\
"dnc":"democrat",\
"earthquake":"disaster",\
"electricity":"energy",\
"eminent domain":"borderWall",\
"energy independence":"energy",\
"energy industry":"energy",\
"energy market":"energy",\
"environmentalist":"environmentalPolicy",\
"espionage":"russiaElectionHacking",\
"facebook":"media",\
"fbi director":"fbiDirector",\
"fbiDirector":"fbiDirector",\
"fcc rule":"trumpCommunication",\
"filibuster":"supremeCourtJudge",\
"first amendment":"racialProvocation",\
"fivethirtyeight":"media",\
"flooding":"disaster",\
"ford motor co":"trade",\
"fortMeyers":"disaster",\
"fuel supply":"nuclearPower",\
"g20":"foreignRelations",\
"gas production":"oil",\
"georgeBush":"georgeBush",\
"gop":"republican",\
"gop bill":"policy",\
"greenhouse gas emission":"environmental",\
"haiti":"haiti",\
"health care cost":"healthcarePolicy",\
"holiday shopping season":"economy",\
"houseAppropriationCommittee":"politicalGroup",\
"hurricane harvey":"disaster",\
"hurricane irma":"disaster",\
"iraq":"middleEast",\
"israel":"middleEast",\
"intervention":"conflict",\
"intrusion":"conflict",\
"intelligence briefing":"communication",\
"import quota":"trade",\
"income inequality":"economy",\
"jobs":"economy",\
"john mccain":"usPolitician",\
"judge neil gorsuch":"supremeCourtJudge",\
"jurist":"courtSystem",\
"jury":"courtSystem",\
"justice anthony kennedy":"supremeCourtJudge",\
"killchain":"conflict",\
"kim jongun":"northKorea",\
"lady melania trump":"trumpFamily",\
"lawEnforcement":"lawEnforcement",\
"layoff":"economy",\
"libya":"africa",\
"make america great again":"presidentialCampaign",\
"marcoRubio":"usPolitician",\
"meddling":"conflict",\
"muslim":"muslimCountry",\
"nancyPelosi":"usPolitican",\
"nbc":"media",\
"negotiator":"policy",\
"new york city":"usCity",\
"news outlet":"media",\
"nfl":"athlete",\
"nlrb":"economy",\
"north carolina":"usState",\
"north dakota":"usState",\
"norway":"europeanCountry",\
"ohio":"usState",\
"oil drilling":"oil",\
"oregon":"usState",\
"otto warmbier":"northKorea",\
"paris climate accord":"environmentalPolicy",\
"party line":"government",\
"paycheck":"economy",\
"peace":"conflict",\
"poland":"europeanCountry",\
"police":"police",\
"policy":"policy",\
"pope":"religion",\
"president order":"policy",\
"press secretary":"trumpAdministration",\
"reince priebus":"usPolitician",\
"shinzo abe":"asianPolitician",\
"prison":"conflict",\
"propaganda":"conflict",\
"punishment":"conflict",\
"quota":"trade",\
"racism":"racialProvocation",\
"recovery effort":"disaster",\
"reelection race":"presidentialElection",\
"refugee policy":"refugeeCrisis",\
"religion":"religion",\
"reporting":"media",\
"rickPerry":"usPolitician",\
"rickScott":"usPolitician",\
"rio grande valley":"geography",\
"robert mueller":"fbiDirector",\
"russia probe":"russiaElectionHacking",\
"san francisco":"usCity",\
"sean spicer":"trumpAdministration",\
"secret":"scandal",\
"security concern":"nationalSecurity",\
"sen jeff flake":"usPolitician",\
"senate armed service committee":"military",\
"shell company":"economy",\
"solar":"solar",\
"somalia":"africa",\
"south sudan":"africa",\
"spending program":"economy",\
"steve bannon":"trumpAdministration",\
"stormy daniel":"controversy",\
"stronghold":"trumpOpposition",\
"supremacist":"racialProvocation",\
"surplus":"trade",\
"suspends immigration":"immigration",\
"tax burden":"taxes",\
"tax obligation":"taxes",\
"tax overhaul":"taxes",\
"tax plan":"taxes",\
"tax record":"taxes",\
"tax revenue":"taxes",\
"taxpayer money":"taxes",\
"tehran":"nuclear",\
"terrorist":"immigration",\
"thaad":"northKorea",\
"thaad system":"northKorea",\
"tower":"trumpProperty",\
"trade action":"trade",\
"trade agenda":"trade",\
"trade gap":"tradeGap",\
"trade negotiation":"trade",\
"trade step":"trade",\
"trading abuse":"trumpPlan",\
"trading volume":"southKorea",\
"transcript":"russiaInvestigation",\
"travel":"cuba",\
"traveler":"travelBan",\
"trump administration official":"trumpAdministration",\
"trump adviser":"trade",\
"trump campaign adviser":"tradeGap",\
"trump effect":"economy",\
"trump speaking":"trumpCommunication",\
"trustee":"conflict",\
"turkey":"conflict",\
"tweet saturday morning":"trumpTweet",\
"u citizenship":"daca",\
"u intelligence":"russiaElectionHacking",\
"u leadership":"foreignPolicy",\
"u virgin island":"disaster",\
"united technology":"jobs",\
"us defense contractor":"arms",\
"us delegation":"climate",\
"us job":"jobs",\
"us taxpayer":"taxes",\
"us trade data":"trade",\
"us trade representative":"trade",\
"venezuela":"foreignPolicy",\
"vice presidentelect mike penny":"trumpAdministration",\
"villaraigosa":"trumpOpposition",\
"visa":"travelBan",\
"visa lottery system":"immigration",\
"warhead":"arms",\
"wealth effect":"economy",\
"withdrawal":"climate",\
"world trade":"trade",\
"worldwide review":"travelBan",\
"adjudication":"travelBan",\
"agent":"russiaInvestigation",\
"american energy independence":"energy",\
"arm race":"arms",\
"assumption":"northKorea",\
"atlantic coast":"energy",\
"attache":"arms",\
"automaker":"southKorea",\
"barackObama":"barackObama",\
"billClinton":"billClinton",\
"bomb":"northKorea",\
"business tax rate":"americanBusiness",\
"cabinet":"conflict",\
"cadre":"conflict",\
"cadre stake":"conflict",\
"cap":"daca",\
"charity":"trumpFoundation",\
"charlottesville":"racialProvocation",\
"childhood arrival":"daca",\
"circuit court":"travelBan",\
"cold war":"foreignPolicy",\
"commissioner":"trade",\
"contradiction":"climate",\
"customer":"business",\
"cyber attack":"russiaElectionHacking",\
"daca recipient":"daca",\
"danger":"conflict",\
"dealmaker":"negotiation",\
"debt":"finance",\
"defender":"conflict",\
"deregulation":"policy",\
"deterrent":"conflict",\
"disgrace":"scandal",\
"disparagement":"scandal",\
"dispute":"conflict",\
"drone":"military",\
"dubai":"middleEast",\
"employer":"economy",\
"energy production":"environmental",\
"envoy":"negotiation",\
"estate tax":"wealth",\
"wealth":"wealth",\
"evil":"conflict",\
"fcc":"media",\
"fireandfury":"controversy",\
"gap":"tradeGap",\
"georgia":"usState",\
"genius":"controversy",\
"hawaii":"usState",\
"headline":"media",\
"health care reform":"healthcarePolicy",\
"hope hick":"trumpAdministration",\
"institue of energy research":"energy",\
"inauguration":"presidentialElection",\
"income tax rate":"economy",\
"infrastructure bank":"finance",\
"investigator":"scandal",\
"irs":"taxes",\
"job creation":"economy",\
"journalism":"media",\
"korea":"koreanConflict",\
"law enforcement agency":"police",\
"leak":"scandal",\
"loser":"conflict",\
"manufacturer":"economy",\
"maryland":"usState",\
"memo":"communication",\
"memorandum":"communication",\
"minister":"religion",\
"msnbc":"media",\
"newspaper":"media",\
"nomination":"government",\
"objection":"conflict",\
"pentagon":"governmentLocation",\
"peter navarro":"trumpAdministration",\
"pipeline":"oil",\
"planet":"environmental",\
"policy objective":"policy",\
"recepErdogan":"middleEasternPolitics",\
"repeal":"policy",\
"san diego":"usCity",\
"shutdown":"conflict",\
"skepticism":"conflict",\
"south china sea":"china",\
"soviet union":"russia",\
"steven mnuchin":"trumpAdministration",\
"stock":"finance",\
"taiwan":"asia",\
"taxpayer dollar":"taxes",\
"testimony":"scandal",\
"trump election":"presidentialElection",\
"trump tower":"trumpProperty",\
"trump tweet":"communication",\
"trumpism":"communication",\
"truth":"conflict",\
"u economy":"economy",\
"u official":"usGovernment",\
"union":"economy",\
"us company":"economy",\
"us official":"usGovernment",\
"us trade deficit":"tradeDeficit",\
"us worker":"economy",\
"uscis":"immigration",\
"video":"media",\
"wage":"jobs",\
"weapon sale":"arms",\
"white house chiefofstaff":"governmentPosition",\
"white house communication":"communication",\
"wikileaks":"controversy",\
"witch hunt":"controversy",\
"yemen":"middleEast",\
"affair":"scandal",\
"american energy":"energy",\
"american health care act":"healthcare",\
"carbon emission":"energy",\
"chiefofstaff":"trumpStaff",\
"childhood arrival program":"daca",\
"coal industry":"coal",\
"commerce":"commerce",\
"development":"foreignPolicy",\
"disclosure":"russiaInvestigation",\
"disrespect":"racialProvocation",\
"document request":"russiaInvestigation",\
"presidentDonaldTrump":"presidentDonaldTrump",\


#===============end pasted section=================================


}

#index keys are case sensitive, let's use all lower() to ensure success in match
concept_dict = {key.lower(): value for key, value in concept_dict.items()}
#Note: I keep values as-is, to improve readability (even if it creates matching headaches for index look-ups)

#todo: build case-insensitive matching, and replace all .lower() calls

pickle.dump(concept_dict, open(pickle_path + 'concept_dict.p', 'wb'))
