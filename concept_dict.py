import pickle
pickle_path = "C:/Users/adams/OneDrive/Documents/Northwestern/453 - Text/pickle/" #where do you want to read / write the phrase list / filters, etc.

concept_dict = {
"bloodbath":"violentCrime",\
"congresss approval":"energy",\
"congresss budget process":"budget",\
"africa":"racialProvocation",\
"libya":"travelBan",\
"somalia":"travelBan",\
"south sudan":"immigration",\
"sudan":"travelBan",\
"agriculture":"budget",\
"agriculture something":"domestic policy",\
"corn":"trade",\
"farmer":"foreignPolicy",\
"benefitcost ratio":"americanBusiness",\
"business leader":"americanBusiness",\
"business tax rate":"americanBusiness",\
"carrier":"americanBusiness",\
"company":"americanBusiness",\
"confidence index":"americanBusiness",\
"culinary worker union":"americanBusiness",\
"ford ceo mark field":"americanBusiness",\
"ford decision":"americanBusiness",\
"general dynamic corp":"americanBusiness",\
"general electric":"americanBusiness",\
"general mcmaster line":"americanBusiness",\
"general motor co":"americanBusiness",\
"government participation":"americanBusiness",\
"harvard business school":"americanBusiness",\
"independent business":"americanBusiness",\
"indiana factory":"americanBusiness",\
"infrastructure":"americanBusiness",\
"infrastructure spending":"americanBusiness",\
"jones":"americanBusiness",\
"mark fields":"americanBusiness",\
"quality":"americanBusiness",\
"spending crisis":"americanBusiness",\
"spending tap":"americanBusiness",\
"startups":"americanBusiness",\
"aluminum case":"arms",\
"america defense":"arms",\
"ammunition":"arms",\
"arm":"arms",\
"arm control advocate":"arms",\
"arm control advocate":"arms",\
"arm control association":"arms",\
"arm deal":"arms",\
"arm export":"arms",\
"arm export":"arms",\
"arm export policy":"arms",\
"arm export policy":"arms",\
"arm maker":"arms",\
"arm maker":"arms",\
"arm proliferation":"arms",\
"arm race":"arms",\
"arm regulation":"arms",\
"arm regulation besides":"arms",\
"arm sale":"arms",\
"arm sale decision":"arms",\
"arm sale decision":"arms",\
"arm supplier":"arms",\
"arms control association":"arms",\
"arms regulations":"arms",\
"arms regulations besides":"arms",\
"arsenal":"arms",\
"artillery":"arms",\
"assault rifle":"arms",\
"assault rifle":"arms",\
"attache":"arms",\
"barrage":"arms",\
"daryl kimball":"arms",\
"government approach":"arms",\
"government source":"arms",\
"gun maker":"arms",\
"international trafficking":"arms",\
"itar":"arms",\
"lockheed martin":"arms",\
"missile program":"arms",\
"munition":"arms",\
"saudi campaign":"arms",\
"seat for human right":"arms",\
"security assistance officer":"arms",\
"south asia":"arms",\
"stimson center":"arms",\
"u.s. weapon":"arms",\
"us arm":"arms",\
"us arm sale":"arms",\
"us defense contractor":"arms",\
"us weapon":"arms",\
"us weapon industry":"arms",\
"warhead":"arms",\
"weapon":"arms",\
"weapon program":"arms",\
"weapon sale":"arms",\
"weapons":"arms",\
"bali":"asianNations",\
"taiwan":"asianNations",\
"taiwan amid":"asianNations",\
"chinas president xi jinping":"asianPolitician",\
"chinese official":"asianPolitician",\
"duterte":"asianPolitician",\
"foreign minister yun byungse":"asianPolitician",\
"rodrigo duterte":"asianPolitician",\
"shinzo abe":"asianPolitician",\
"force":"foreignPolicy",\
"chris warren":"energy",\
"nfl":"racialProvocation",\
"ambivalence":"trait",\
"michael wolff":"media",\
"barack obama":"barackObama",\
"barack obamas government":"barackObama",\
"barack obamas presidency":"barackObama",\
"barack obamas work":"barackObama",\
"barackObama":"barackObama",\
"incumbent":"barackObama",\
"obama":"barackObama",\
"obama administration":"barackObama",\
"obama administration policy":"barackObama",\
"obama presidency":"barackObama",\
"obama regulation":"barackObama",\
"obama year":"barackObama",\
"obamaera":"barackObama",\
"obamaera policy":"barackObama",\
"obamas choice":"barackObama",\
"obamas decision":"barackObama",\
"obamas legacy":"barackObama",\
"obamas term":"barackObama",\
"obamas veto":"barackObama",\
"president barack obama":"barackObama",\
"president obama":"barackObama",\
"barrier":"borderSecurity",\
"border":"borderSecurity",\
"border protection":"borderSecurity",\
"border security":"borderSecurity",\
"border security budget document":"borderSecurity",\
"border security issue":"borderSecurity",\
"cut regulation":"borderSecurity",\
"flake spokesman jason samuel":"borderSecurity",\
"homeland security":"borderSecurity",\
"security":"borderSecurity",\
"southern border":"borderSecurity",\
"u.s.-mexico border":"borderSecurity",\
"usmexico border":"borderSecurity",\
"appropriation committee":"borderWall",\
"border barrier":"borderWall",\
"border wall":"borderWall",\
"border wall prototype":"borderWall",\
"borderWall":"borderWall",\
"contractor":"borderWall",\
"delegation":"borderWall",\
"dhs spokeswoman":"borderWall",\
"eminent domain":"borderWall",\
"fence":"borderWall",\
"fencing":"borderWall",\
"funding need":"borderWall",\
"funding request":"borderWall",\
"government accountability office":"borderWall",\
"government funding":"borderWall",\
"government funding bill":"borderWall",\
"great wall":"borderWall",\
"investment research group":"borderWall",\
"laredo":"borderWall",\
"mexico pay":"borderWall",\
"nih":"borderWall",\
"patrol agent":"borderWall",\
"phase":"borderWall",\
"secure fence act":"borderWall",\
"security activity":"borderWall",\
"senate minority whip dick durbin":"borderWall",\
"senator patrick j leahy":"borderWall",\
"showdown":"borderWall",\
"signature border wall":"borderWall",\
"signature campaign promise":"borderWall",\
"spending bill":"borderWall",\
"standout campaign promise":"borderWall",\
"steel purchase":"borderWall",\
"wall":"borderWall",\
"wall":"borderWall",\
"amendment":"budget",\
"america first":"budget",\
"appropriation":"budget",\
"appropriation bill":"budget",\
"budget":"budget",\
"budget blueprint":"budget",\
"budget committee":"budget",\
"congress budget process":"budget",\
"funding package":"budget",\
"national endowment":"budget",\
"officeofmanagementandbudget":"budget",\
"pentagon boost":"budget",\
"reconciliation":"budget",\
"spending package":"budget",\
"aapl":"business",\
"acquisition":"business",\
"affiliate kia motors corp":"business",\
"agricultural bank":"business",\
"auto industry account":"business",\
"auto industry committee":"business",\
"auto maker":"business",\
"automation":"business",\
"automation plan":"business",\
"automobile":"business",\
"bearing factory":"business",\
"bernstein research":"business",\
"bfps ventures":"business",\
"billionaire developer":"business",\
"boeing":"business",\
"boeing co":"business",\
"bp":"business",\
"bruce kasman":"business",\
"business":"business",\
"business":"business",\
"business associate":"business",\
"business concern":"business",\
"business dealing area":"business",\
"business economics":"business",\
"business equipment":"business",\
"business holding":"business",\
"business insider":"business",\
"business intersects":"business",\
"business model":"business",\
"business owner":"business",\
"business partner":"business",\
"business partners":"business",\
"business people":"business",\
"business person":"business",\
"business professor":"business",\
"business sense":"business",\
"business setback":"business",\
"business trip":"business",\
"businessman":"business",\
"businesspeople":"business",\
"buyer":"business",\
"cameco corp":"business",\
"car dealership":"business",\
"car maker":"business",\
"career":"business",\
"casino":"business",\
"coal":"business",\
"comcast":"business",\
"comms team":"business",\
"companies resulting":"business",\
"company investment":"business",\
"company share":"business",\
"corporation":"business",\
"customer":"business",\
"defense contractor":"business",\
"defense industry official":"business",\
"edelman trust barometer":"business",\
"euphoria":"business",\
"fiat chrysler automobiles nv":"business",\
"ford":"business",\
"ford ceo mark fields":"business",\
"ford executive":"business",\
"gas":"business",\
"industry":"business",\
"monopoly":"business",\
"raytheon co":"business",\
"steel":"business",\
"toyota motor corp":"business",\
"us corporation":"business",\
"whirlpool":"business",\
"advantage china":"china",\
"beijing":"china",\
"china":"china",\
"china president xi jinping":"china",\
"china role":"china",\
"china steadfastness":"china",\
"china willingness":"china",\
"chinese":"china",\
"communist party congress":"china",\
"geng shuang":"china",\
"islandbuilding":"china",\
"south china sea":"china",\
"uschina relationship":"china",\
"uschina strategic":"china",\
"xi jinping":"china",\
"al gore":"climateChange",\
"america void":"climateChange",\
"climate":"climateChange",\
"climate action":"climateChange",\
"climate change":"climateChange",\
"climate hero":"climateChange",\
"coal miner":"climateChange",\
"contradiction":"climateChange",\
"emission":"climateChange",\
"emissionsreduction target priority":"climateChange",\
"framework convention":"climateChange",\
"government intrusion":"climateChange",\
"green supply chain":"climateChange",\
"greenhouse emission":"climateChange",\
"greenhouse gas emitter":"climateChange",\
"greenpeace china":"climateChange",\
"greenpeace usa":"climateChange",\
"grenada":"climateChange",\
"group earthjustice":"climateChange",\
"harvard school":"climateChange",\
"harvard university robert stavins":"climateChange",\
"obamaera climate change regulation":"climateChange",\
"obamas climate policy":"climateChange",\
"paris agreement":"climateChange",\
"paris agreementthe accord":"climateChange",\
"paris climate change agreement":"climateChange",\
"paris climatechange commitment":"climateChange",\
"paris withdrawal":"climateChange",\
"security situation":"climateChange",\
"us delegation":"climateChange",\
"warming":"climateChange",\
"withdrawal":"climateChange",\
"coal industry":"energy",\
"air conditioning":"naturalDisaster",\
"commerce":"business",\
"commerce department":"secretary",\
"commerce department highlight sheet":"secretary",\
"commerce department inspector general":"secretary",\
"commerce secretary":"secretary",\
"investor wilbur ross":"secretary",\
"wilburRoss":"secretary",\
"bipartisanship":"communication",\
"body language":"communication",\
"briefer side":"communication",\
"briefing":"communication",\
"communication method":"communication",\
"community perspective":"communication",\
"community relation":"communication",\
"curry tweet":"communication",\
"dcalif":"communication",\
"deliberate":"communication",\
"divestiture":"communication",\
"intelligence briefing":"communication",\
"memo":"communication",\
"memorandum":"communication",\
"morning twitter offensive":"communication",\
"president comment":"communication",\
"press briefing":"communication",\
"renegotiation":"communication",\
"trash talk":"communication",\
"trump tweet":"communication",\
"trumpism":"communication",\
"twitter":"communication",\
"video":"communication",\
"voicemail":"communication",\
"white house communication":"communication",\
"white house email":"communication",\
"white house official announcement":"communication",\
"white house press":"communication",\
"activist":"conflict",\
"adversary":"conflict",\
"agitator":"conflict",\
"amnesty":"conflict",\
"amnesty don":"conflict",\
"amnesty international":"conflict",\
"annexation":"conflict",\
"antidefamation league":"conflict",\
"antius credential":"conflict",\
"argument":"conflict",\
"backlash":"conflict",\
"backlash online":"conflict",\
"bald threat":"conflict",\
"bigotry strike":"conflict",\
"blackmail":"conflict",\
"blindtrust issue a number":"conflict",\
"brand terrorist":"conflict",\
"cadre":"conflict",\
"cadre stake":"conflict",\
"ceo credibility":"conflict",\
"challenge senator":"conflict",\
"challenger":"conflict",\
"community grapple":"conflict",\
"confirmation fight":"conflict",\
"conflict":"conflict",\
"damage":"conflict",\
"danger":"conflict",\
"defiance":"conflict",\
"demonstrator":"conflict",\
"deterrent":"conflict",\
"discrepancy":"conflict",\
"disdain":"conflict",\
"dispute":"conflict",\
"dissent":"conflict",\
"diverse":"conflict",\
"emolument clause":"conflict",\
"evil":"conflict",\
"failure":"conflict",\
"fight":"conflict",\
"gary kalman":"conflict",\
"georgetown":"conflict",\
"government general service administration":"conflict",\
"government responsibility":"conflict",\
"hate":"conflict",\
"hate group":"conflict",\
"holding":"conflict",\
"intervention":"conflict",\
"intrusion":"conflict",\
"islamic terror":"conflict",\
"killchain":"conflict",\
"kuwaiti event":"conflict",\
"liar":"conflict",\
"loser":"conflict",\
"lunacy":"conflict",\
"marcher":"conflict",\
"meddling":"conflict",\
"objection":"conflict",\
"power grab":"conflict",\
"power influence":"conflict",\
"predicament":"conflict",\
"prison":"conflict",\
"propaganda":"conflict",\
"prosecution":"conflict",\
"protest":"conflict",\
"punishment":"conflict",\
"refusal":"conflict",\
"relation war":"conflict",\
"repudiation":"conflict",\
"restraining order":"conflict",\
"rogue nation":"conflict",\
"rogue state":"conflict",\
"shutdown":"conflict",\
"sibur":"conflict",\
"skepticism":"conflict",\
"tension":"conflict",\
"uprising":"conflict",\
"us misunderstanding":"conflict",\
"violation":"conflict",\
"watchdog group":"conflict",\
"congress":"government",\
"allegation":"controversy",\
"cnn identifies sajwani":"controversy",\
"collusion":"controversy",\
"djt foundation":"controversy",\
"emoluments clause":"controversy",\
"employee interest":"controversy",\
"equity giant blackstone":"controversy",\
"exxon mobil chief":"controversy",\
"faceoff":"controversy",\
"fact coalition":"controversy",\
"fake news mainstream media":"controversy",\
"fake news media":"controversy",\
"fake news networks":"controversy",\
"feud":"controversy",\
"fireandfury":"controversy",\
"fired":"controversy",\
"foreclosure machine":"controversy",\
"genius":"controversy",\
"golden state warrior":"controversy",\
"nondisclosure agreement":"controversy",\
"party view":"controversy",\
"phill ruffin":"controversy",\
"playboy centerfold model":"controversy",\
"president attack":"controversy",\
"rumor":"controversy",\
"slavery sits":"controversy",\
"stephanie clifford":"controversy",\
"stephen a schwarzman":"controversy",\
"stormy daniel":"controversy",\
"trump university":"controversy",\
"vulgar word choice":"controversy",\
"wikileaks":"controversy",\
"witch hunt":"controversy",\
"appeal court":"supremeCourt",\
"appeal court judge":"supremeCourt",\
"circuit decision":"supremeCourt",\
"circuit ruling":"supremeCourt",\
"columbia circuit":"supremeCourt",\
"court decision":"supremeCourt",\
"court nominee":"supremeCourt",\
"court ruling":"supremeCourt",\
"criminal defense attorney alan dershowitz":"supremeCourt",\
"dc court":"supremeCourt",\
"defense attorney":"supremeCourt",\
"diane sykes":"supremeCourt",\
"end filibuster":"supremeCourt",\
"federalist society":"supremeCourt",\
"hearing":"supremeCourt",\
"jurist":"supremeCourt",\
"jury":"supremeCourt",\
"law firm":"supremeCourt",\
"lowercourt pick":"supremeCourt",\
"cuba":"centralAmericanNations",\
"havana":"centralAmericanNations",\
"little havana":"centralAmericanNations",\
"manuel artime theater":"centralAmericanNations",\
"mr obamas cuba policy":"centralAmericanNations",\
"security service":"centralAmericanNations",\
"travel":"centralAmericanNations",\
"american progress":"daca",\
"cap":"daca",\
"central america":"daca",\
"childhood arrival":"daca",\
"childhood arrival program":"daca",\
"daca":"daca",\
"daca recipient":"daca",\
"deferred action":"daca",\
"enterprise":"daca",\
"gang ms13":"daca",\
"obama administration deferred action":"daca",\
"salvadoran":"daca",\
"u citizenship":"daca",\
"alabama u senate":"democrat",\
"california democrat":"democrat",\
"clubforgrowthandheritage":"democrat",\
"cruz":"democrat",\
"democrat":"democrat",\
"dianneFienstein":"democrat",\
"dmassachusetts":"democrat",\
"dnc":"democrat",\
"dnew york":"democrat",\
"former clinton administration treasury secretary lawrence summer":"democrat",\
"gavin newsom":"democrat",\
"gore":"democrat",\
"governor mansion":"democrat",\
"governor race":"democrat",\
"governor responsibility":"democrat",\
"jack markell":"democrat",\
"jerry brown":"democrat",\
"nancy":"democrat",\
"nancy pelosi":"democrat",\
"opposition agenda":"democrat",\
"armageddon":"naturalDisaster",\
"catastrophe":"naturalDisaster",\
"cellphone service":"naturalDisaster",\
"debris":"naturalDisaster",\
"debris block road":"naturalDisaster",\
"disaster":"naturalDisaster",\
"disaster":"naturalDisaster",\
"disaster relief funding":"naturalDisaster",\
"disaster relief official":"naturalDisaster",\
"disaster zone":"naturalDisaster",\
"earthquake":"naturalDisaster",\
"federal emergency management agency":"naturalDisaster",\
"fema":"naturalDisaster",\
"flooding":"naturalDisaster",\
"fort myers":"naturalDisaster",\
"fortMeyers":"naturalDisaster",\
"genocide":"naturalDisaster",\
"harvey":"naturalDisaster",\
"hurricane":"naturalDisaster",\
"hurricane harvey":"naturalDisaster",\
"hurricane irma":"naturalDisaster",\
"maria":"naturalDisaster",\
"monster storm":"naturalDisaster",\
"oil spill":"naturalDisaster",\
"recovery crew":"naturalDisaster",\
"recovery effort":"naturalDisaster",\
"relief effort":"naturalDisaster",\
"stopgap measure":"naturalDisaster",\
"storm":"naturalDisaster",\
"storm":"naturalDisaster",\
"trump katrina":"naturalDisaster",\
"u virgin island":"naturalDisaster",\
"aclu":"domesticPolicy",\
"affordable care act isnt exploding":"domesticPolicy",\
"cost restoring community safety act":"domesticPolicy",\
"defense agreement":"domesticPolicy",\
"domesticPolicy":"domesticPolicy",\
"eldercare act":"domesticPolicy",\
"electronic frontier foundation":"domesticPolicy",\
"establishment republicans":"domesticPolicy",\
"exchange commission":"domesticPolicy",\
"federal communication commission":"domesticPolicy",\
"federal communications commission":"domesticPolicy",\
"george washington university law school":"domesticPolicy",\
"heating assistance":"domesticPolicy",\
"highway bill":"domesticPolicy",\
"house freedom caucus":"domesticPolicy",\
"house gop conference":"domesticPolicy",\
"house republican caucus":"domesticPolicy",\
"house version":"domesticPolicy",\
"lobbying ban":"domesticPolicy",\
"mass transit":"domesticPolicy",\
"medicade":"domesticPolicy",\
"mentalhealth care":"domesticPolicy",\
"public policy":"domesticPolicy",\
"redirects education dollar repeal":"domesticPolicy",\
"repeal bill":"domesticPolicy",\
"republican bill":"domesticPolicy",\
"realdonaldtrump":"presidentDonaldTrump",\
"europeanUnion":"economy",\
"globalization":"economy",\
"american household income":"economy",\
"antiunion consulting firm":"economy",\
"bonus check":"economy",\
"budget deficit":"economy",\
"budget document":"economy",\
"budget process":"economy",\
"budget resolution":"economy",\
"budget resolution deadline":"economy",\
"budget year":"economy",\
"business confidence":"economy",\
"buy american plan":"economy",\
"carrier corp":"economy",\
"carrier corp factory":"economy",\
"carrier deal":"economy",\
"carrier job cut":"economy",\
"carrier official":"economy",\
"carrier worker":"economy",\
"communication job":"economy",\
"community development grant":"economy",\
"construction equipment":"economy",\
"construction job":"economy",\
"consumer behavior":"economy",\
"consumer permission":"economy",\
"consumer right":"economy",\
"control panel factory":"economy",\
"create job":"economy",\
"culinary workers union":"economy",\
"debt ceiling":"economy",\
"debt ceiling deal":"economy",\
"debt limit":"economy",\
"doddfrank act":"economy",\
"douglas harris":"economy",\
"economic cooperation network":"economy",\
"economic dialogue":"economy",\
"economic theory":"economy",\
"economics department":"economy",\
"economics section":"economy",\
"economist":"economy",\
"economy":"economy",\
"economy but":"economy",\
"employer":"economy",\
"engineering job":"economy",\
"financial time":"economy",\
"freddie investment":"economy",\
"freddie mac":"economy",\
"gdp":"economy",\
"gunman":"economy",\
"highpaying job":"economy",\
"hiring process":"economy",\
"holiday shopping season":"economy",\
"housing":"economy",\
"hurt business":"economy",\
"income inequality":"economy",\
"income tax rate":"economy",\
"job creation":"economy",\
"jobs":"economy",\
"labor department figure":"economy",\
"labor market":"economy",\
"labor secretary alexander acosta":"economy",\
"labor union":"economy",\
"layoff":"economy",\
"lender economist":"economy",\
"macroeconomics advisor":"economy",\
"manufacturer":"economy",\
"mark zandi":"economy",\
"michigan factory":"economy",\
"mining industry":"economy",\
"nlrb":"economy",\
"paycheck":"economy",\
"privatesector job":"economy",\
"production worker":"economy",\
"repatriation":"economy",\
"retired united steelworker local":"economy",\
"sandp500":"economy",\
"sector":"economy",\
"shell company":"economy",\
"spending program":"economy",\
"stock gain":"economy",\
"stock market price":"economy",\
"stockmarket rally":"economy",\
"sucker game":"economy",\
"toll road deal":"economy",\
"tourism industry":"economy",\
"trump effect":"economy",\
"u economy":"economy",\
"unemployment":"economy",\
"union":"economy",\
"united state economy":"economy",\
"us auto industry":"economy",\
"us auto industry job":"economy",\
"us car":"economy",\
"us company":"economy",\
"us economy":"economy",\
"us economy":"economy",\
"us infrastructure spending":"economy",\
"us manufacturing":"economy",\
"us worker":"economy",\
"wealth effect":"economy",\
"welfare":"economy",\
"work force":"economy",\
"asan institute":"education",\
"associate professor":"education",\
"bob fleisher":"education",\
"bruce cain":"education",\
"bucknell university":"education",\
"calculus":"education",\
"charter school":"education",\
"cheng xiaohe":"education",\
"college degree":"education",\
"college student":"education",\
"columbia journalism review":"education",\
"columbia universitys center":"education",\
"competitive enterprise institutes center":"education",\
"cooperative congressional election study":"education",\
"cox media institute":"education",\
"dean":"education",\
"ed wasserman":"education",\
"education":"education",\
"education opportunity act":"education",\
"educator":"education",\
"government fund":"education",\
"harvard law school":"education",\
"hofstra university":"education",\
"professor":"education",\
"school":"education",\
"school choice":"education",\
"tulane university":"education",\
"uc berkeley goldman school":"education",\
"university":"education",\
"usc":"education",\
"victoria university":"education",\
"yonsei university graduate school":"education",\
"child care":"jobs",\
"childcare":"jobs",\
"advocacy organization":"energy",\
"alliance":"energy",\
"america energy problem":"energy",\
"american energy":"energy",\
"american energy independence":"energy",\
"arctic":"energy",\
"atlantic coast":"energy",\
"carbon dioxide":"energy",\
"carbon emission":"energy",\
"comment periodwhich":"energy",\
"competitive enterprise institute center":"energy",\
"concerned scientist":"energy",\
"congress approval":"energy",\
"donald trump energy plan":"energy",\
"electricity":"energy",\
"energy":"energy",\
"energy commissioner miguel aria canete":"energy",\
"energy independence":"energy",\
"energy industry":"energy",\
"energy market":"energy",\
"energyand":"energy",\
"epa":"energy",\
"epa clean power plan":"energy",\
"ferc":"energy",\
"fuel":"energy",\
"global energy policy":"energy",\
"government agency":"energy",\
"government regulation":"energy",\
"groundwater":"energy",\
"gulf coast":"energy",\
"gulf state":"energy",\
"habitat":"energy",\
"hydroelectric":"energy",\
"ieas world energy investment report":"energy",\
"institue of energy research":"energy",\
"interior department":"energy",\
"interior rule":"energy",\
"international energy agency":"energy",\
"keystone pipeline":"energy",\
"nigel farage":"energy",\
"obamas clean power plan":"energy",\
"ocean":"energy",\
"offshore wind farm":"energy",\
"permit application":"energy",\
"power line":"energy",\
"power sector":"energy",\
"power source":"energy",\
"solarworld":"energy",\
"subsidy":"energy",\
"wind":"energy",\
"wind power":"energy",\
"anthony scaramucci":"americanBusiness",\
"carl c icahn":"americanBusiness",\
"casino magnate phil ruffin":"americanBusiness",\
"ceo mark zuckerberg":"americanBusiness",\
"christopher steele":"americanBusiness",\
"david koch":"americanBusiness",\
"albertas oil":"environmental",\
"biological diversity":"environmental",\
"brian segee":"environmental",\
"c40 conference":"environmental",\
"carbon emitter":"environmental",\
"carbon trading":"environmental",\
"chemical":"environmental",\
"clean":"environmental",\
"coal lease":"environmental",\
"coal mine":"environmental",\
"coal mining":"environmental",\
"coal mining job":"environmental",\
"coal power":"environmental",\
"coal power coal":"environmental",\
"coal power plant":"environmental",\
"coal production":"environmental",\
"coal shipment":"environmental",\
"concerned scientists":"environmental",\
"dakota access pipeline":"environmental",\
"david sandalow":"environmental",\
"deepwater horizon oil rig disaster":"environmental",\
"dozen coal miner":"environmental",\
"drilling plan":"environmental",\
"drilling zone":"environmental",\
"earth":"environmental",\
"emission":"environmental",\
"emission limit":"environmental",\
"emissions reduction target priority":"environmental",\
"energy clean technology solar":"environmental",\
"energy company":"environmental",\
"energy flourish":"environmental",\
"energy job":"environmental",\
"energy production":"environmental",\
"energy source":"environmental",\
"greenhouse gas emission":"environmental",\
"methane":"environmental",\
"planet":"environmental",\
"power generation":"environmental",\
"refinery":"environmental",\
"transmission organization":"environmental",\
"us environmental protection agency":"environmental",\
"us wind power industry":"environmental",\
"wastewater":"environmental",\
"water quality":"environmental",\
"activist group nextgen climate":"environmentalPolicy",\
"activist tom steyer":"environmentalPolicy",\
"america water":"environmentalPolicy",\
"americafirst energy policy":"environmentalPolicy",\
"american conservative union":"environmentalPolicy",\
"american energy alliance":"environmentalPolicy",\
"american energy reserve":"environmentalPolicy",\
"americas energy problem":"environmentalPolicy",\
"americas water":"environmentalPolicy",\
"americorps":"environmentalPolicy",\
"annie leonard":"environmentalPolicy",\
"arias canete":"environmentalPolicy",\
"billionaire environmentalist tom steyer":"environmentalPolicy",\
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
"conservation voter":"environmentalPolicy",\
"donald trumps energy plan":"environmentalPolicy",\
"eagle protection act":"environmentalPolicy",\
"energy agency":"environmentalPolicy",\
"energy analyst":"environmentalPolicy",\
"energy and":"environmentalPolicy",\
"energy commission":"environmentalPolicy",\
"energy department report":"environmentalPolicy",\
"energy development":"environmentalPolicy",\
"energy developmentall action":"environmentalPolicy",\
"energy dominance":"environmentalPolicy",\
"energy efficiency equipment online":"environmentalPolicy",\
"energy governance system":"environmentalPolicy",\
"energy incentive":"environmentalPolicy",\
"energy infrastructure project":"environmentalPolicy",\
"energy issue":"environmentalPolicy",\
"energy panel":"environmentalPolicy",\
"energy policy":"environmentalPolicy",\
"energy price":"environmentalPolicy",\
"energy provider":"environmentalPolicy",\
"energy regulation":"environmentalPolicy",\
"energy research":"environmentalPolicy",\
"energy show":"environmentalPolicy",\
"energy study":"environmentalPolicy",\
"energy superpower":"environmentalPolicy",\
"energy technology":"environmentalPolicy",\
"energy weakness":"environmentalPolicy",\
"energy worker":"environmentalPolicy",\
"environmentalist":"environmentalPolicy",\
"envoy xie yesterday":"environmentalPolicy",\
"fact iea energy head dave turk":"environmentalPolicy",\
"federal energy regulatory commission":"environmentalPolicy",\
"federal water pollution control act":"environmentalPolicy",\
"national environmental policy act":"environmentalPolicy",\
"natural resource defense council":"environmentalPolicy",\
"offshoring act establishes":"environmentalPolicy",\
"paris climate accord":"environmentalPolicy",\
"polluter":"environmentalPolicy",\
"power capacity investment":"environmentalPolicy",\
"power plant emission limit":"environmentalPolicy",\
"trump america first energy plan":"environmentalPolicy",\
"trump epa":"environmentalPolicy",\
"trump paris exit":"environmentalPolicy",\
"trump paris stance":"environmentalPolicy",\
"trumpera energy framework":"environmentalPolicy",\
"un climate change program":"environmentalPolicy",\
"un climate process":"environmentalPolicy",\
"unfccc":"environmentalPolicy",\
"us emission target":"environmentalPolicy",\
"us fish and wildlife service":"environmentalPolicy",\
"usEnvironmentalProtectionAgency":"environmentalPolicy",\
"wa trump paris exit good politics":"environmentalPolicy",\
"europe":"europeanNation",\
"germany":"europeanNation",\
"aberdeen":"europeanNation",\
"copenhagen":"europeanNation",\
"britain":"europeanNation",\
"denmark":"europeanNation",\
"europe":"europeanNation",\
"norway":"europeanNation",\
"poland":"europeanNation",\
"crimea":"europeanNation",\
"chancellor angela merkel":"europeanNation",\
"dmitry peskov":"europeanNation",\
"action may be taken":"russiaElectionHacking",\
"audience wider":"foreignPolicy",\
"breach":"northsouthkorea",\
"comey firing":"fbi",\
"cornyn spoke":"immigration",\
"debate begin tuesday":"supremecourtjudge",\
"december meeting":"russiaelectionHacking",\
"decree":"climatechange",\
"deliberation":"arms",\
"acosta":"controversy",\
"circulation":"controversy",\
"cox medium institute":"controversy",\
"fake news mainstream medium":"controversy",\
"fake news medium":"controversy",\
"fake news network":"controversy",\
"godwins law":"controversy",\
"nazi comparison":"controversy",\
"fbi":"fbi",\
"fbi director":"fbi",\
"fbiDirector":"fbi",\
"james b comey":"fbi",\
"james comey":"fbi",\
"jamesComey":"fbi",\
"mr comey":"fbi",\
"mr comeys":"fbi",\
"mr mueller":"fbi",\
"office of special counsel":"fbi",\
"robert mueller":"fbi",\
"robertMueller":"fbi",\
"7th circuit":"supremeCourt",\
"abc":"finance",\
"administration budget":"finance",\
"administration budget isnt":"finance",\
"allocation":"finance",\
"asia development bank":"finance",\
"bank":"finance",\
"bank building":"finance",\
"banker":"finance",\
"banking":"finance",\
"bankruptcy":"finance",\
"bankruptcy law":"finance",\
"benefitcost analysis":"finance",\
"blind trust issue a number":"finance",\
"bond holder":"finance",\
"bottom line":"finance",\
"bracket":"finance",\
"business bankruptcy":"finance",\
"cayman":"finance",\
"cayman island":"finance",\
"cayman islands":"finance",\
"cbo score":"finance",\
"cheapest":"finance",\
"china development bank":"finance",\
"cost estimate":"finance",\
"credit scenario":"finance",\
"currency":"finance",\
"debt":"finance",\
"deutsche bank":"finance",\
"deutsche bank debt":"finance",\
"dow jones":"finance",\
"earnings":"finance",\
"fannie mae":"finance",\
"finance unit":"finance",\
"goldman sachs":"finance",\
"infrastructure bank":"finance",\
"mortgage interest":"finance",\
"predatory lending practice":"finance",\
"premium increase":"finance",\
"profit margin":"finance",\
"project capital":"finance",\
"stock":"finance",\
"stock market":"finance",\
"us dollar":"finance",\
"wall street":"finance",\
"wealthy":"finance",\
"world bank":"finance",\
"year budget resolution":"finance",\
"accord":"foreignPolicy",\
"ally japan":"foreignPolicy",\
"american president":"foreignPolicy",\
"asylum claim":"foreignPolicy",\
"biggest foreign policy headache":"foreignPolicy",\
"brexit vote":"foreignPolicy",\
"broad restriction":"foreignPolicy",\
"china delivers":"foreignPolicy",\
"china expert":"foreignPolicy",\
"china gain credibility":"foreignPolicy",\
"china hawk":"foreignPolicy",\
"china militarism mean":"foreignPolicy",\
"chinas militarism means":"foreignPolicy",\
"chinas role":"foreignPolicy",\
"chinas steadfastness":"foreignPolicy",\
"chinas willingness":"foreignPolicy",\
"cold war":"foreignPolicy",\
"common wealth":"foreignPolicy",\
"communist china":"foreignPolicy",\
"communist partys congress":"foreignPolicy",\
"country independence":"foreignPolicy",\
"country mexico":"foreignPolicy",\
"country were":"foreignPolicy",\
"country withdrawal":"foreignPolicy",\
"defense department asia specialist":"foreignPolicy",\
"democracy promotion":"foreignPolicy",\
"development":"foreignPolicy",\
"diplomacy":"foreignPolicy",\
"diplomacy fails":"foreignPolicy",\
"diplomat":"foreignPolicy",\
"dozen pacific rim nation":"foreignPolicy",\
"dutertes affinity":"foreignPolicy",\
"effigy":"foreignPolicy",\
"embarrassment":"foreignPolicy",\
"embassy":"foreignPolicy",\
"encroachment":"foreignPolicy",\
"epicenter":"foreignPolicy",\
"european":"foreignPolicy",\
"european court":"foreignPolicy",\
"europeans court":"foreignPolicy",\
"foreign affair committee":"foreignPolicy",\
"foreign relation":"foreignPolicy",\
"foreigner":"foreignPolicy",\
"foreignPolicy":"foreignPolicy",\
"g20 summit":"foreignPolicy",\
"g20 summit confront":"foreignPolicy",\
"government leader":"foreignPolicy",\
"hamburg police":"foreignPolicy",\
"marshall plan":"foreignPolicy",\
"multinationalization":"foreignPolicy",\
"nato member":"foreignPolicy",\
"new zealand":"foreignPolicy",\
"nikki haley":"foreignPolicy",\
"policy address":"foreignPolicy",\
"u leadership":"foreignPolicy",\
"unitedNations":"foreignPolicy",\
"us china":"foreignPolicy",\
"venezuela":"foreignPolicy",\
"vision":"foreignPolicy",\
"world":"foreignPolicy",\
"farflung province":"foreignPolicy",\
"foreign relations":"foreignPolicy",\
"g20":"foreignPolicy",\
"lu chao":"foreignPolicy",\
"mexico regardless":"foreignPolicy",\
"prime minister":"foreignPolicy",\
"united nations":"foreignPolicy",\
"united state position":"foreignPolicy",\
"us ally":"foreignPolicy",\
"us credibility":"foreignPolicy",\
"us influence":"foreignPolicy",\
"us power":"foreignPolicy",\
"us relationship":"foreignPolicy",\
"us special envoy":"foreignPolicy",\
"world affair":"foreignPolicy",\
"shopturnedcapitol hill power broker":"trumpOpposition",\
"fuel capability":"energy",\
"fuel industry stooge":"energy",\
"fuel production":"energy",\
"fuel source":"energy",\
"fuel technology company":"energy",\
"gasoline price":"energy",\
"appalachian":"energy",\
"atlantic":"energy",\
"atlantic ocean":"energy",\
"big bend":"borderWall",\
"east asia":"asianNations",\
"rio grande valley":"borderWall",\
"angela merkel":"europeanNation",\
"attorney general":"government",\
"authoritarianism":"government",\
"defense minister":"government",\
"demagogue":"government",\
"dictator":"government",\
"ethic reform":"government",\
"fbi headquarters":"government",\
"floor adviser":"government",\
"government employee":"government",\
"government ethic":"government",\
"government ethic form":"government",\
"government ethic office":"government",\
"government ethic rule":"government",\
"governor":"government",\
"hegemony":"government",\
"justice department":"government",\
"mayor":"government",\
"morning intelligence briefing":"government",\
"nomination":"government",\
"party line":"government",\
"paul ryan":"government",\
"politician":"government",\
"republic":"government",\
"resurgent authoritarianism":"government",\
"term limit":"government",\
"u presidency":"government",\
"washingtonDC":"government",\
"year term":"government",\
"camp david meeting":"government",\
"consulate":"government",\
"control center":"government",\
"donald trump resistance":"government",\
"pentagon":"government",\
"house leader":"trumpAdministration",\
"white house aide":"trumpAdministration",\
"white house budget director":"trumpAdministration",\
"white house chiefofstaff":"trumpAdministration",\
"white house communication director":"trumpAdministration",\
"white house communication staff":"trumpAdministration",\
"white house ethic lawyer":"trumpAdministration",\
"white house insider":"trumpAdministration",\
"white house intern":"trumpAdministration",\
"white house job":"trumpAdministration",\
"white house spokeswoman":"trumpAdministration",\
"haiti":"centralAmericanNations",\
"sofla community":"centralAmericanNations",\
"affordable care act":"healthcare",\
"ahca":"healthcare",\
"american health care act":"healthcare",\
"broken system":"healthcare",\
"constituent":"healthcare",\
"health benefit":"healthcare",\
"health bill":"healthcare",\
"health care":"healthcare",\
"health care act":"healthcare",\
"health care bill":"healthcare",\
"health care bill":"healthcare",\
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
"house freedomcaucus":"healthcare",\
"insurance executive":"healthcare",\
"insurance policy":"healthcare",\
"insurer offering obamacare":"healthcare",\
"johnson":"healthcare",\
"lee":"healthcare",\
"medicaid":"healthcare",\
"medicare":"healthcare",\
"obamacare benchmark plan":"healthcare",\
"obamacare health plan":"healthcare",\
"obamacare protection":"healthcare",\
"obamacare repeal":"healthcare",\
"obamacare requirement":"healthcare",\
"obamacares":"healthcare",\
"obamacares requirement":"healthcare",\
"obamacares washingtondriven":"healthcare",\
"obamaclinton roadblock":"healthcare",\
"party goal":"healthcare",\
"party member":"healthcare",\
"party organization":"healthcare",\
"party voter":"healthcare",\
"partyasorganization":"healthcare",\
"partyasorganization group":"healthcare",\
"public health":"healthcare",\
"senate health bill":"healthcare",\
"support majority leader mitch mcconnells bill":"healthcare",\
"survey monkey poll":"healthcare",\
"aca":"healthcare",\
"health care cost":"healthcare",\
"health care reform":"healthcare",\
"obamacare":"healthcare",\
"republican ahca bill":"healthcare",\
"republican health care bill":"healthcare",\
"anticlinton":"hillaryClinton",\
"clinton":"hillaryClinton",\
"clinton administration":"hillaryClinton",\
"clinton campaign":"hillaryClinton",\
"clinton extremist agenda":"hillaryClinton",\
"clinton plan":"hillaryClinton",\
"clinton voter":"hillaryClinton",\
"clintons extremist agenda":"hillaryClinton",\
"crooked hillary":"hillaryClinton",\
"crooked hillary clinton":"hillaryClinton",\
"hillary":"hillaryClinton",\
"hillary clinton":"hillaryClinton",\
"hillaryClinton":"hillaryClinton",\
"leon panetta":"hillaryClinton",\
"nominee hillary clinton":"hillaryClinton",\
"alien":"immigration",\
"arrest":"immigration",\
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
"burden sharing":"immigration",\
"catos brannon":"immigration",\
"cbp proposal":"immigration",\
"citizen":"immigration",\
"cuban":"immigration",\
"cuban americans":"immigration",\
"cuban exile community":"immigration",\
"cubanamericans":"immigration",\
"customs enforcement":"immigration",\
"daca cover":"immigration",\
"daca permit":"immigration",\
"database":"immigration",\
"deportation":"immigration",\
"deportation":"immigration",\
"deportation proceeding":"immigration",\
"dire strait":"immigration",\
"diversity visa lottery":"immigration",\
"doublelayer fencing":"immigration",\
"dream":"immigration",\
"dreamer":"immigration",\
"drop":"immigration",\
"efren c olivares":"immigration",\
"end illegal immigration act":"immigration",\
"end illegal immigration act fully funds":"immigration",\
"end illegal immigration act fullyfunds":"immigration",\
"examine visa program":"immigration",\
"expiration deadline":"immigration",\
"felony conviction":"immigration",\
"guatemala":"immigration",\
"hawaii attorney general":"immigration",\
"honduran":"immigration",\
"ice":"immigration",\
"ice agent":"immigration",\
"ice removal authority":"immigration",\
"imbalance":"immigration",\
"immigrant":"immigration",\
"immigrant legal resource center":"immigration",\
"immigrant work":"immigration",\
"immigration":"immigration",\
"immigration attorney":"immigration",\
"immigration authority":"immigration",\
"immigration barrier":"immigration",\
"immigration deal":"immigration",\
"immigration enforcer":"immigration",\
"immigration hardliner":"immigration",\
"immigration law":"immigration",\
"immigration officer":"immigration",\
"immigration order":"immigration",\
"immigration policy":"immigration",\
"immigration reform package":"immigration",\
"immigration reform proposal":"immigration",\
"immigration system":"immigration",\
"immigration tends":"immigration",\
"immigrationAndNationalityAct":"immigration",\
"isi threat":"immigration",\
"islamic revolution":"immigration",\
"islamic state militant":"immigration",\
"leon rodriguez":"immigration",\
"muslim ban":"immigration",\
"muslim ban a registry":"immigration",\
"muslim country":"immigration",\
"muslim immigrant":"immigration",\
"muslim leader":"immigration",\
"muslim living":"immigration",\
"muslim population":"immigration",\
"national immigration law center":"immigration",\
"national security entryexit program":"immigration",\
"national security policy":"immigration",\
"naureen shah":"immigration",\
"new america foundation":"immigration",\
"nicaragua":"immigration",\
"nicaraguan":"immigration",\
"nseers program":"immigration",\
"proimmigration policy":"immigration",\
"residency":"immigration",\
"sanctuary city":"immigration",\
"something majority leader mitch mcconnell":"immigration",\
"spokesman jason miller":"immigration",\
"supreme court decision":"immigration",\
"suspends immigration":"immigration",\
"terrorist":"immigration",\
"usborn":"immigration",\
"uscis":"immigration",\
"visa lottery system":"immigration",\
"visa program":"immigration",\
"work authorization":"immigration",\
"india":"asianNations",\
"mumbai":"asianNations",\
"hamidreza taraghi":"middleEasternNations",\
"hassan rouhani":"middleEasternNations",\
"iran":"middleEasternNations",\
"iran agreement":"middleEasternNations",\
"iran deal":"middleEasternNations",\
"iran economy":"middleEasternNations",\
"iran foreign ministry":"middleEasternNations",\
"iran islamic establishment":"middleEasternNations",\
"iran president":"middleEasternNations",\
"suicide":"nuclear",\
"naples":"europeanNation",\
"japan":"asianNations",\
"coalmining job":"jobs",\
"countrywere":"jobs",\
"dependability":"jobs",\
"distribute largesse":"jobs",\
"fiat chrysler automobile nv":"jobs",\
"fleming experience":"jobs",\
"furnace production job":"jobs",\
"government oversight":"jobs",\
"incentive package":"jobs",\
"indiana official":"jobs",\
"indiana plant":"jobs",\
"indiana town":"jobs",\
"job":"jobs",\
"job creation agenda":"jobs",\
"job cut":"jobs",\
"job generator":"jobs",\
"job loss":"jobs",\
"job number":"jobs",\
"job opportunity":"jobs",\
"job outflow":"jobs",\
"job retention":"jobs",\
"national labor relation board":"jobs",\
"plant job":"jobs",\
"plentiful job":"jobs",\
"terryFlemings":"jobs",\
"united technology":"jobs",\
"us job":"jobs",\
"wage":"jobs",\
"worker":"jobs",\
"korea":"northSouthKorea",\
"law enforcement":"domesticPolicy",\
"lawEnforcement":"trumpBusiness",\
"abc good morning america":"media",\
"abcs good morning america":"media",\
"ad":"media",\
"advertisement":"media",\
"advertiser":"media",\
"afternoon broadcast fox news shep smith":"media",\
"ann coulter":"media",\
"assertion":"media",\
"associated press":"media",\
"author michael wolff":"media",\
"author mike godwin":"media",\
"axios":"media",\
"bbc":"media",\
"bestseller list":"media",\
"bill kristol":"media",\
"blair":"media",\
"bloomberg":"media",\
"bloomberg news":"media",\
"book tour":"media",\
"breitbart news":"media",\
"broadcast":"media",\
"bruce bennett":"media",\
"burton":"media",\
"buzzfeed":"media",\
"cable news":"media",\
"cable news network":"media",\
"californiaberkeley":"media",\
"cbs":"media",\
"charles sykes":"media",\
"christiane amanpour":"media",\
"cnbc":"media",\
"cnn analyst":"media",\
"cnn reporter jim acosta":"media",\
"cnn review":"media",\
"cnns":"media",\
"cnns report":"media",\
"correspondent":"media",\
"coverage":"media",\
"david sanger":"media",\
"dc insider":"media",\
"director christopher wray":"media",\
"disclosure form":"media",\
"drutman":"media",\
"eandenews":"media",\
"economist mark zandi":"media",\
"edward luce":"media",\
"facebook":"media",\
"fcc":"media",\
"financial times":"media",\
"fivethirtyeight":"media",\
"flake spokesman jason samuels":"media",\
"fox news":"media",\
"fox news executive bill shine":"media",\
"fox news sunday":"media",\
"fraud":"media",\
"grady newsource":"media",\
"gwenda blair":"media",\
"hannity":"media",\
"headline":"media",\
"headline trump":"media",\
"internet meme":"media",\
"jim scuitto":"media",\
"journalism":"media",\
"journalist":"media",\
"lester holt":"media",\
"magazine":"media",\
"marketing":"media",\
"mcclatchy news website":"media",\
"media":"media",\
"medium outlet":"media",\
"medium site":"media",\
"msnbc":"media",\
"msnbc channel":"media",\
"msnbc tv host mika brzezinski":"media",\
"national enquirer":"media",\
"nbc":"media",\
"nbc news":"media",\
"nbc news analyst":"media",\
"news":"media",\
"news briefing":"media",\
"news conference":"media",\
"news coverage":"media",\
"news item":"media",\
"news outlet":"media",\
"news property":"media",\
"news release":"media",\
"news report":"media",\
"news story":"media",\
"newspaper":"media",\
"politico":"media",\
"politico report":"media",\
"politifact":"media",\
"press":"media",\
"press conference":"media",\
"press coverage":"media",\
"press report":"media",\
"rachel maddow":"media",\
"radio show":"media",\
"reality star":"media",\
"reality tv star":"media",\
"reporter":"media",\
"reporting":"media",\
"reuters":"media",\
"ria news agency":"media",\
"sean hannity":"media",\
"sykes":"media",\
"tabloid newspaper didnt publish":"media",\
"television today":"media",\
"video":"media",\
"wall street journal":"media",\
"washington post":"media",\
"week news":"media",\
"wmaq":"media",\
"alzheimer":"healthcare",\
"american medical association":"healthcare",\
"cancer":"healthcare",\
"care physician":"healthcare",\
"doctor":"healthcare",\
"dr joseph mason":"healthcare",\
"drug":"healthcare",\
"hospital":"healthcare",\
"medicine":"healthcare",\
"misdiagnosis":"healthcare",\
"mexico":"centralAmericanNations",\
"bahrain":"middleEasternNations",\
"dubai":"middleEasternNations",\
"iraq":"middleEasternNations",\
"israel":"middleEasternNations",\
"middle east":"middleEasternNations",\
"saudi arabia":"middleEasternNations",\
"syria":"middleEasternNations",\
"yemen":"middleEasternNations",\
"kuwait":"middleEasternNations",\
"abbasi":"middleEasternNations",\
"ali larijani":"middleEasternNations",\
"ayatollah sadegh amolilarijani":"middleEasternNations",\
"mahmoud ahmadinejad":"middleEasternNations",\
"mohammad javad zarif":"middleEasternNations",\
"recepErdogan":"middleEasternNations",\
"recepErdogan":"middleEasternNations",\
"emirati business partner hussain sajwani":"middleEasternNations",\
"emirati businessman":"middleEasternNations",\
"air force":"military",\
"army":"military",\
"atlantic reserve":"military",\
"brave soldier":"military",\
"counterstrike":"military",\
"destroyer":"military",\
"drone":"military",\
"government spending":"military",\
"land force":"military",\
"marine":"military",\
"militant":"military",\
"military":"military",\
"senate armed service committee":"military",\
"troop readiness":"military",\
"u troop":"military",\
"veteran":"military",\
"warship":"military",\
"afghanistan all muslim majority nation":"religion",\
"afghanistanall muslimmajority nation":"religion",\
"muslim":"religion",\
"fta":"trade",\
"fta outright":"trade",\
"nafta":"trade",\
"nafta pact":"trade",\
"pullout will undermine us":"trade",\
"americas defense":"nationalSecurity",\
"defense program":"nationalSecurity",\
"foreign terrorist entry into":"nationalSecurity",\
"homeland security discretion":"nationalSecurity",\
"homeland security travel ban":"nationalSecurity",\
"publicsafety threat":"nationalSecurity",\
"security concern":"nationalSecurity",\
"threat mount":"nationalSecurity",\
"trump national security council":"nationalSecurity",\
"us defense security cooperation agency":"nationalSecurity",\
"gas company":"energy",\
"gas exploration":"energy",\
"gas leasing program":"energy",\
"gas power plant":"energy",\
"turkey":"middleEasternNations",\
"agreement mr trump":"communication",\
"dealmaker":"communication",\
"envoy":"communication",\
"actionsspeaklouderthanwords":"northSouthKorea",\
"assumption":"northSouthKorea",\
"bomb":"northSouthKorea",\
"consistency":"northSouthKorea",\
"defense jim mattis":"northSouthKorea",\
"delury":"northSouthKorea",\
"deterrence capability":"northSouthKorea",\
"dozen u official":"northSouthKorea",\
"enemy relationship":"northSouthKorea",\
"george f kennan":"northSouthKorea",\
"guam":"northSouthKorea",\
"icbm":"northSouthKorea",\
"inhabitant":"northSouthKorea",\
"joint security area":"northSouthKorea",\
"jong un sit":"northSouthKorea",\
"kim":"northSouthKorea",\
"kim jong un":"northSouthKorea",\
"kim jong un":"northSouthKorea",\
"kim jonghoon":"northSouthKorea",\
"kim jongun":"northSouthKorea",\
"missile":"northSouthKorea",\
"national assembly":"northSouthKorea",\
"north ability":"northSouthKorea",\
"north korea":"northSouthKorea",\
"north korea expert":"northSouthKorea",\
"north korea launch site":"northSouthKorea",\
"north korea leader":"northSouthKorea",\
"north korea menace":"northSouthKorea",\
"north korea missile":"northSouthKorea",\
"north korea missile launch":"northSouthKorea",\
"north korea policy":"northSouthKorea",\
"north korea problem":"northSouthKorea",\
"north korea situation":"northSouthKorea",\
"northKorea":"northSouthKorea",\
"oped":"northSouthKorea",\
"otto warmbier":"northSouthKorea",\
"peninsula issue":"northSouthKorea",\
"pentagon strategist":"northSouthKorea",\
"people army":"northSouthKorea",\
"preventive war":"northSouthKorea",\
"pyongyang":"northSouthKorea",\
"pyongyang":"northSouthKorea",\
"regime":"northSouthKorea",\
"security council":"northSouthKorea",\
"security problem":"northSouthKorea",\
"situation room discussion":"northSouthKorea",\
"statesman":"northSouthKorea",\
"stephen k bannon":"northSouthKorea",\
"stopping north korea":"northSouthKorea",\
"strike":"northSouthKorea",\
"thaad":"northSouthKorea",\
"thaad system":"northSouthKorea",\
"u policy towards north korea":"northSouthKorea",\
"bureaucracy":"nuclear",\
"new start treaty":"nuclear",\
"nuclear nonproliferation treaty":"nuclear",\
"nuke":"nuclear",\
"tehran":"nuclear",\
"uranium":"nuclear",\
"denuclearization":"nuclear",\
"lightbridge corp":"nuclear",\
"warhead stockpile":"nuclear",\
"fuel supply":"energy",\
"joe biden":"barackObama",\
"susan e rice":"barackObama",\
"damage settlement":"environmental",\
"senator maggie hassan":"environmental",\
"sierra club":"environmental",\
"alberta oil":"energy",\
"crude oil":"energy",\
"drilling":"energy",\
"fracking":"energy",\
"gas production":"energy",\
"keystone xl pipeline":"energy",\
"oil":"energy",\
"oil company":"energy",\
"oil drillers":"energy",\
"oil drilling":"energy",\
"oil drilling oil drilling":"energy",\
"oil industry":"energy",\
"oil pipeline":"energy",\
"oil price":"energy",\
"oil reserve":"energy",\
"pipeline":"energy",\
"standing rock sioux tribe":"energy",\
"year outer continental shelf oil":"energy",\
"commander":"military",\
"law enforcement agency":"lawEnforcement",\
"police":"lawEnforcement",\
"trooper jay cullen":"lawEnforcement",\
"virginia state trooper":"lawEnforcement",\
"deregulation":"policy",\
"developing policy":"policy",\
"gop bill":"policy",\
"heritage foundation":"policy",\
"legislature":"policy",\
"lobbyist":"policy",\
"negotiator":"policy",\
"policy":"policy",\
"policy":"policy",\
"policy objective":"policy",\
"president order":"policy",\
"regulation":"policy",\
"regulation":"policy",\
"repeal":"policy",\
"united state exit":"policy",\
"us policy":"policy",\
"florida republicans":"government",\
"hill member":"government",\
"house appropriation committee":"government",\
"houseAppropriationCommittee":"government",\
"redstate senator":"government",\
"renegade republican":"government",\
"tea party":"government",\
"trump ally":"government",\
"fundraising operation":"presidentialCampaign",\
"donald j trump":"presidentDonaldTrump",\
"executive order":"presidentdonaldTrump",\
"executive power":"presidentDonaldTrump",\
"incoming president":"presidentDonaldTrump",\
"presidentDonaldTrump":"presidentDonaldTrump",\
"presidentDonaldTrump":"presidentDonaldTrump",\
"presidentElectDonaldTrump":"presidentdonaldTrump",\
"secret service":"presidentDonaldTrump",\
"secret service detail":"presidentDonaldTrump",\
"trump presidency":"presidentDonaldTrump",\
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
"candidacy":"presidentialCampaign",\
"candidate hillary clinton":"presidentialCampaign",\
"contribution thousand":"presidentialCampaign",\
"convince voter":"presidentialCampaign",\
"core trump supporter":"presidentialCampaign",\
"election campaign":"presidentialCampaign",\
"election campaign mr trump":"presidentialCampaign",\
"election campaign promise":"presidentialCampaign",\
"election contest":"presidentialCampaign",\
"election operation":"presidentialCampaign",\
"election result":"presidentialCampaign",\
"election voter":"presidentialCampaign",\
"election win":"presidentialCampaign",\
"electoral college":"presidentialCampaign",\
"fundraising activity":"presidentialCampaign",\
"latino heavy electorate":"presidentialCampaign",\
"make america great again":"presidentialCampaign",\
"postelection rally":"presidentialCampaign",\
"president campaign promise":"presidentialCampaign",\
"president campaign sticker":"presidentialCampaign",\
"reelection bid":"presidentialCampaign",\
"trump campaign infrastructure tax":"presidentialCampaign",\
"trump target audience":"presidentialCampaign",\
"candidate":"presidentialElection",\
"election":"presidentialElection",\
"election day":"presidentialElection",\
"gallup":"presidentialElection",\
"gallup poll":"presidentialElection",\
"inauguration":"presidentialElection",\
"presidentialElection":"presidentialElection",\
"primary":"presidentialElection",\
"reelection race":"presidentialElection",\
"republicanleaning mountain town":"presidentialElection",\
"rnc":"presidentialElection",\
"trump election":"presidentialElection",\
"trump state":"presidentialElection",\
"trump supporters1":"presidentialElection",\
"trump win":"presidentialElection",\
"us election":"presidentialElection",\
"vote":"presidentialElection",\
"voter":"presidentialElection",\
"puerto rico":"centralAmericanNations",\
"bigotry":"racialProvocation",\
"bitch":"racialProvocation",\
"bond":"racialProvocation",\
"charlottesville":"racialProvocation",\
"civil right":"racialProvocation",\
"condemnation":"racialProvocation",\
"curry":"racialProvocation",\
"death fill":"racialProvocation",\
"discrimination":"racialProvocation",\
"disrespect":"racialProvocation",\
"fallen americans":"racialProvocation",\
"first amendment":"racialProvocation",\
"kkk":"racialProvocation",\
"martin luther king jr day weekend":"racialProvocation",\
"minority turnout":"racialProvocation",\
"minority voter":"racialProvocation",\
"racism":"racialProvocation",\
"racist":"racialProvocation",\
"supremacist":"racialProvocation",\
"refugee":"controversy",\
"refuge":"controversy",\
"refugee policy":"controversy",\
"almighty god":"religion",\
"minister":"religion",\
"pope":"religion",\
"religion":"religion",\
"hindu temple":"religion",\
"alabama sen jeff session":"republican",\
"alaska lisa murkowski":"republican",\
"attorney general jeff session":"republican",\
"chuck grassley":"republican",\
"deanHeller":"republican",\
"economic adviser chairman kevin hassett":"republican",\
"florida republican":"republican",\
"gop":"republican",\
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
"house republican":"republican",\
"john boehner":"republican",\
"paul ryan":"republican",\
"republican":"republican",\
"republican":"republican",\
"sen dean heller":"republican",\
"sen marco rubio":"republican",\
"sen ted cruz":"republican",\
"senate gop":"republican",\
"senate majority leader mitch mcconnell land":"republican",\
"speaker paul ryan":"republican",\
"speaker ryan":"republican",\
"state rex w tillerson":"republican",\
"ted cruz":"republican",\
"kalugin":"europeanNation",\
"moscow":"europeanNation",\
"putin":"europeanNation",\
"russia":"europeanNation",\
"russian":"europeanNation",\
"soviet republic":"europeanNation",\
"soviet union":"europeanNation",\
"assange":"russiaElectionHacking",\
"computer server":"russiaElectionHacking",\
"cyber attack":"russiaElectionHacking",\
"delay":"russiaElectionHacking",\
"document dump":"russiaElectionHacking",\
"election interference":"russiaElectionHacking",\
"election issue":"russiaElectionHacking",\
"espionage":"russiaElectionHacking",\
"evidence russia":"russiaElectionHacking",\
"facebook ad":"russiaElectionHacking",\
"fbi investigator":"russiaElectionHacking",\
"foreign affairs committee":"russiaElectionHacking",\
"friday sanction":"russiaElectionHacking",\
"fsb diplomatic spat":"russiaElectionHacking",\
"gamesmanship":"russiaElectionHacking",\
"glenn simpson":"russiaElectionHacking",\
"government operative":"russiaElectionHacking",\
"grassley beforehand":"russiaElectionHacking",\
"hack":"russiaElectionHacking",\
"hacking":"russiaelectionHacking",\
"hacking allegation":"russiaElectionHacking",\
"hacking tool":"russiaElectionHacking",\
"house intelligence committee":"russiaElectionHacking",\
"imprisonment":"russiaElectionHacking",\
"indictment":"russiaElectionHacking",\
"influence campaign":"russiaElectionHacking",\
"intelligence":"russiaElectionHacking",\
"intelligence community finding":"russiaElectionHacking",\
"intelligence community work":"russiaElectionHacking",\
"intelligence officer":"russiaElectionHacking",\
"intelligence official":"russiaElectionHacking",\
"intelligence report":"russiaElectionHacking",\
"intelligence service":"russiaElectionHacking",\
"intelligence service mi6":"russiaElectionHacking",\
"interview president donald trump":"russiaElectionHacking",\
"john kirby":"russiaelectionHacking",\
"julian assange":"russiaElectionHacking",\
"justice department investigation":"russiaElectionHacking",\
"justice department veteran":"russiaElectionHacking",\
"kgb man":"russiaElectionHacking",\
"kremlin":"russiaElectionHacking",\
"kremlin involvement":"russiaElectionHacking",\
"kremlin spokesman dmitr peskov":"russiaElectionHacking",\
"kremlin spokesman dmitry peskov":"russiaElectionHacking",\
"kremlin website":"russiaElectionHacking",\
"kulagin":"russiaElectionHacking",\
"moscowdirected hacking":"russiaElectionHacking",\
"mueller russia probe washington anticipating":"russiaElectionHacking",\
"national security official":"russiaElectionHacking",\
"new leak":"russiaElectionHacking",\
"obstruction":"russiaElectionHacking",\
"oval office meeting":"russiaElectionHacking",\
"oval office time":"russiaElectionHacking",\
"peskov":"russiaElectionHacking",\
"robert dallek":"russiaElectionHacking",\
"russia probe":"russiaElectionHacking",\
"russiaElectionHacking":"russiaElectionHacking",\
"senator john mccain":"russiaElectionHacking",\
"senator lindsey graham":"russiaElectionHacking",\
"spy chief":"russiaelectionHacking",\
"state john kerry":"russiaElectionHacking",\
"u intelligence":"russiaElectionHacking",\
"affidavit":"russiaElectionHacking",\
"agent":"russiaElectionHacking",\
"collusion":"russiaElectionHacking",\
"cyberthreats":"russiaElectionHacking",\
"dershowitz":"russiaElectionHacking",\
"disclosure":"russiaElectionHacking",\
"document request":"russiaElectionHacking",\
"dossier":"russiaElectionHacking",\
"firing":"russiaElectionHacking",\
"intelligence agency":"russiaElectionHacking",\
"intelligence community":"russiaElectionHacking",\
"intelligenceAgency":"russiaElectionHacking",\
"interference":"russiaElectionHacking",\
"investigation":"russiaElectionHacking",\
"mr flynn":"russiaElectionHacking",\
"probe":"russiaElectionHacking",\
"russia investigation":"russiaElectionHacking",\
"senate intelligence committee":"russiaElectionHacking",\
"sergey i kislyak":"russiaElectionHacking",\
"sergey v lavrov":"russiaElectionHacking",\
"spying organisation":"russiaElectionHacking",\
"st petersburg":"russiaElectionHacking",\
"surveillance":"russiaElectionHacking",\
"transcript":"russiaElectionHacking",\
"u intelligence community":"russiaElectionHacking",\
"aleksey pushkov":"europeanNation",\
"affair":"controversy",\
"anticorruption group":"controversy",\
"business trump":"controversy",\
"clapper laid bare":"controversy",\
"disgrace":"controversy",\
"disparagement":"controversy",\
"encounter":"controversy",\
"fitness column":"controversy",\
"investigator":"controversy",\
"lawyer mr trump":"controversy",\
"leak":"controversy",\
"money laundering":"controversy",\
"ms clifford":"controversy",\
"secret":"controversy",\
"testimony":"controversy",\
"solar":"energy",\
"suniva":"energy",\
"el salvador":"southAmericanNations",\
"honduras":"southAmericanNations",\
"buenos aire":"southAmericanNations",\
"buenos aires":"southAmericanNations",\
"argentine counterpart mauricio macri":"southAmericanNations",\
"argentine journalist jorge lanata":"southAmericanNations",\
"christiana figueres":"southAmericanNations",\
"fidel castro":"southAmericanNations",\
"mauricio macri":"southAmericanNations",\
"automaker":"northSouthKorea",\
"away south korea":"northSouthKorea",\
"ben forney":"northSouthKorea",\
"hyundai motor co":"northSouthKorea",\
"korean peninsula problem":"northSouthKorea",\
"minister joo hyunghwan":"northSouthKorea",\
"president moon jaein":"northSouthKorea",\
"president park geunhye":"northSouthKorea",\
"seoul":"northSouthKorea",\
"seoul":"northSouthKorea",\
"south korea neighbor japan":"northSouthKorea",\
"south korea soldier":"northSouthKorea",\
"south korea trade minister":"northSouthKorea",\
"south korean":"northSouthKorea",\
"southKorea":"northSouthKorea",\
"support research":"northSouthKorea",\
"trading volume":"northSouthKorea",\
"actions speak louder than words realm":"communication",\
"antonin scalia":"supremeCourtJudge",\
"appointee":"supremecourtjudge",\
"chamber rule":"supremeCourtJudge",\
"confirmation vote":"supremeCourtJudge",\
"filibuster":"supremeCourtJudge",\
"gorsuch":"supremeCourtJudge",\
"gorsuchs":"supremeCourtJudge",\
"gorsuchs ability":"supremeCourtJudge",\
"gorsuchs confirmation hearing":"supremeCourtJudge",\
"gorsuchs nomination":"supremeCourtJudge",\
"judge confirmation process":"supremeCourtJudge",\
"judge james robart":"supremeCourtJudge",\
"judge neil gorsuch":"supremeCourtJudge",\
"judge robart":"supremeCourtJudge",\
"judiciary":"supremeCourtJudge",\
"justice":"supremeCourtJudge",\
"justice anthony kennedy":"supremeCourtJudge",\
"justice anthony m kennedy":"supremeCourtJudge",\
"justice antonin scalia":"supremeCourtJudge",\
"justice kennedy":"supremeCourtJudge",\
"justice kennedy president trump":"supremeCourtJudge",\
"justice ruth bader ginsburg":"supremeCourtJudge",\
"justice scalia":"supremeCourtJudge",\
"justice stephen breyer":"supremeCourtJudge",\
"kennedy":"supremeCourtJudge",\
"mr trump supreme court nominee":"supremeCourtJudge",\
"nominee":"supremecourtjudge",\
"scalia vacancy":"supremeCourtJudge",\
"scaramuccis appointment":"supremeCourtJudge",\
"scaramuccis view":"supremeCourtJudge",\
"senate fight":"supremeCourtJudge",\
"senate floor procedure":"supremeCourtJudge",\
"stephen g breyer":"supremeCourtJudge",\
"steveScalise":"supremeCourtJudge",\
"supreme court":"supremeCourtJudge",\
"supreme court arm":"supremeCourtJudge",\
"supreme court justice":"supremeCourtJudge",\
"supreme court pick":"supremeCourtJudge",\
"supreme court vacancy":"supremeCourtJudge",\
"u supreme court":"supremeCourtJudge",\
"us supreme court":"supremeCourtJudge",\
"business tax cut":"taxes",\
"capital gain tax":"taxes",\
"century tax code":"taxes",\
"deficit hardliner":"taxes",\
"deficit hawk":"taxes",\
"estate tax repeal":"taxes",\
"exemption":"taxes",\
"gain tax":"taxes",\
"greg valliere":"taxes",\
"hardworking american":"taxes",\
"house plan":"taxes",\
"income tax bracket":"taxes",\
"income tax filing":"taxes",\
"investment tax":"taxes",\
"investor interest":"taxes",\
"irs":"taxes",\
"kyle pomerleau":"taxes",\
"negotiation upwards":"taxes",\
"pas something":"taxes",\
"passage middle class tax relief":"taxes",\
"ronald reagan":"taxes",\
"rossnavarro tax credit":"taxes",\
"slash tax":"taxes",\
"smartassetcom":"taxes",\
"state tax break":"taxes",\
"tax":"taxes",\
"tax benefit":"taxes",\
"tax bill":"taxes",\
"tax break":"taxes",\
"tax burden":"taxes",\
"tax code":"taxes",\
"tax code complete":"taxes",\
"tax code cost american million":"taxes",\
"tax credit":"taxes",\
"tax credit":"taxes",\
"tax cut":"taxes",\
"tax cut":"taxes",\
"tax deferral":"taxes",\
"tax didnt":"taxes",\
"tax foundation":"taxes",\
"tax incentive":"taxes",\
"tax measure":"taxes",\
"tax obligation":"taxes",\
"tax overhaul":"taxes",\
"tax plan":"taxes",\
"tax policy center":"taxes",\
"tax rate":"taxes",\
"tax receipt":"taxes",\
"tax record":"taxes",\
"tax reform":"taxes",\
"tax reform blueprint":"taxes",\
"tax reform law":"taxes",\
"tax reform plan":"taxes",\
"tax relief":"taxes",\
"tax return":"taxes",\
"tax revenue":"taxes",\
"tax system":"taxes",\
"taxes":"taxes",\
"taxpayer":"taxes",\
"taxpayer buck":"taxes",\
"taxpayer dollar":"taxes",\
"taxpayer funding":"taxes",\
"taxpayer money":"taxes",\
"trillion":"taxes",\
"u taxpayer":"taxes",\
"united state tax":"taxes",\
"us taxpayer":"taxes",\
"computer simulation":"technology",\
"computer system":"technology",\
"cyber capability":"technology",\
"cyber domain":"technology",\
"cyber hacking":"technology",\
"cyberattacks trump":"technology",\
"cyberreview team":"technology",\
"cybersabotage":"technology",\
"cyberthreats thursday":"technology",\
"data":"technology",\
"emmett okeefe":"technology",\
"estate technology startup":"technology",\
"government technology":"technology",\
"privacy advocate":"technology",\
"privacy framework":"technology",\
"tech giant apple":"technology",\
"technology":"technology",\
"technology company":"technology",\
"vpn":"technology",\
"web site":"technology",\
"affiliate kia motor corp":"trade",\
"aluminum import":"trade",\
"auto industry":"trade",\
"blowback":"trade",\
"china trade policy":"trade",\
"chinas trade policy":"trade",\
"cohn":"trade",\
"commissioner":"trade",\
"companiesresulting":"trade",\
"custom enforcement":"trade",\
"damage lighthizer uncovers":"trade",\
"disarray":"trade",\
"economybut":"trade",\
"export":"trade",\
"export good":"trade",\
"export restriction":"trade",\
"export rule":"trade",\
"ford motor co":"trade",\
"fords decision":"trade",\
"gdp":"trade",\
"global affair":"trade",\
"good deficit":"trade",\
"government official":"trade",\
"growth strategy":"trade",\
"import":"trade",\
"import quota":"trade",\
"import restriction":"trade",\
"international economics":"trade",\
"investigation uncovers":"trade",\
"investment decision":"trade",\
"itc commissioner":"trade",\
"jeremiad":"trade",\
"koo zayong":"trade",\
"korea automobile manufacturer association":"trade",\
"korea trade minister":"trade",\
"merchandise trade deficit":"trade",\
"mexico economy ministry":"trade",\
"mexico factory":"trade",\
"model trade agreement":"trade",\
"pacific pact":"trade",\
"president trade vision":"trade",\
"quota":"trade",\
"quota restriction":"trade",\
"robert lighthizer":"trade",\
"san luis potosi":"trade",\
"sanction":"trade",\
"security perspective":"trade",\
"security threat":"trade",\
"singapore":"trade",\
"surplus":"trade",\
"tpp":"trade",\
"trade":"trade",\
"trade action":"trade",\
"trade agenda":"trade",\
"trade agreement":"trade",\
"trade case":"trade",\
"trade clinton":"trade",\
"trade conflict":"trade",\
"trade crackdown":"trade",\
"trade deal":"trade",\
"trade decision":"trade",\
"trade expansion act":"trade",\
"trade expert":"trade",\
"trade fight":"trade",\
"trade friction":"trade",\
"trade group":"trade",\
"trade meeting":"trade",\
"trade negotiation":"trade",\
"trade pact":"trade",\
"trade partner":"trade",\
"trade policy":"trade",\
"trade practice":"trade",\
"trade relation":"trade",\
"trade relationship":"trade",\
"trade step":"trade",\
"trade surplus":"trade",\
"trade tension":"trade",\
"trade war":"trade",\
"trading partner":"trade",\
"trading system":"trade",\
"treaty":"trade",\
"trump adviser":"trade",\
"us export":"trade",\
"us international trade commission":"trade",\
"us sanction":"trade",\
"us trade":"trade",\
"us trade data":"trade",\
"us trade law":"trade",\
"us trade representative":"trade",\
"us trading partner":"trade",\
"white house national trade council":"trade",\
"white house trade official":"trade",\
"world trade":"trade",\
"world trade organization":"trade",\
"wto":"trade",\
"deficit":"trade",\
"submarine":"trade",\
"trade balance":"trade",\
"trade deficit":"trade",\
"us trade deficit":"trade",\
"us trade deficit decline":"trade",\
"us trade gap":"trade",\
"commerce department report":"trade",\
"gap":"trade",\
"trade gap":"trade",\
"trump campaign adviser":"trade",\
"tariff":"trade",\
"characteristic":"trait",\
"competence":"trait",\
"confidence":"trait",\
"dominance":"trait",\
"fitness":"trait",\
"stability":"trait",\
"adjudication":"travelBan",\
"ban":"travelBan",\
"bar ten":"travelBan",\
"circuit court":"travelBan",\
"country very carefully":"travelBan",\
"solicitor gen jeffrey wall":"travelBan",\
"suspension":"travelBan",\
"travel ban":"travelBan",\
"travel ban case":"travelBan",\
"traveler":"travelBan",\
"visa":"travelBan",\
"worldwide review":"travelBan",\
"additional aide":"trumpAdministration",\
"administration":"trumpAdministration",\
"administration hasnt":"trumpAdministration",\
"administration intensifies negotiation":"trumpAdministration",\
"administration lawyer":"trumpAdministration",\
"administration official":"trumpAdministration",\
"administration policy":"trumpAdministration",\
"administration preparation":"trumpAdministration",\
"administration response":"trumpAdministration",\
"administration tuesday night":"trumpAdministration",\
"administrator trump":"trumpAdministration",\
"adviser":"trumpAdministration",\
"aide":"trumpAdministration",\
"aide briefed":"trumpAdministration",\
"aide meeting":"trumpAdministration",\
"attorney general":"trumpAdministration",\
"cabinet":"trumpAdministration",\
"cabinet member":"trumpAdministration",\
"cabinet official":"trumpAdministration",\
"cabinet pick":"trumpAdministration",\
"cabinet secretary":"trumpAdministration",\
"fatigue":"trumpAdministration",\
"general mcmaster":"trumpAdministration",\
"george papadopoulos":"trumpAdministration",\
"homeland security secretary elaine duke":"trumpAdministration",\
"homeland security secretary kirstjen nielsen":"trumpAdministration",\
"hope hick":"trumpAdministration",\
"incoming donald trump administration":"trumpAdministration",\
"jared kushner":"trumpAdministration",\
"jim mattiss":"trumpAdministration",\
"kellyanne conway":"trumpAdministration",\
"michael cohen":"trumpAdministration",\
"michael short":"trumpAdministration",\
"mike pence":"trumpAdministration",\
"mr cohen":"trumpAdministration",\
"mr kushner":"trumpAdministration",\
"peter navarro":"trumpAdministration",\
"press secretary":"trumpAdministration",\
"priebus":"trumpAdministration",\
"raj shah":"trumpAdministration",\
"ryan zinke":"trumpAdministration",\
"scaramucci":"trumpAdministration",\
"sean spicer":"trumpAdministration",\
"secretary john kelly":"trumpAdministration",\
"security adviser michael flynn":"trumpAdministration",\
"security secretary john kelly":"trumpAdministration",\
"spicer":"trumpAdministration",\
"steve bannon":"trumpAdministration",\
"steven mnuchin":"trumpAdministration",\
"tillerson":"trumpAdministration",\
"trump administration official":"trumpAdministration",\
"trumpAdministration":"trumpAdministration",\
"trumpAdministration":"trumpAdministration",\
"vice president":"trumpAdministration",\
"vice presidentelect mike penny":"trumpAdministration",\
"west wing":"trumpAdministration",\
"white house":"trumpAdministration",\
"white house official":"trumpAdministration",\
"trump organization":"trumpBusiness",\
"campaign":"presidentialCampaign",\
"mr trump campaign":"presidentialCampaign",\
"sarah huckabee sanders":"presidentialCampaign",\
"trump campaign":"presidentialCampaign",\
"blunt tweet":"trumpCommunication",\
"bombast":"trumpCommunication",\
"communication":"trumpCommunication",\
"fcc rule":"trumpCommunication",\
"intimidation effect":"trumpCommunication",\
"james robart":"trumpCommunication",\
"mr trump twitter message":"trumpCommunication",\
"nfl tweet":"trumpCommunication",\
"rhetoric":"trumpCommunication",\
"speech":"trumpCommunication",\
"trump speaking":"trumpCommunication",\
"charity":"trumpBusiness",\
"foundation":"trumpBusiness",\
"trump foundation":"trumpBusiness",\
"advocacy group":"trumpOpposition",\
"antitrump":"trumpOpposition",\
"asheville":"trumpOpposition",\
"blasio":"trumpOpposition",\
"caucus":"trumpOpposition",\
"connecticut":"trumpOpposition",\
"eric holder":"trumpOpposition",\
"freedomcaucus":"trumpOpposition",\
"opposition":"trumpOpposition",\
"sparring partner":"trumpOpposition",\
"speaker anthony rendon":"trumpOpposition",\
"state address":"trumpOpposition",\
"state attorney":"trumpOpposition",\
"state legislature":"trumpOpposition",\
"state legislature california":"trumpOpposition",\
"state party email":"trumpOpposition",\
"stronghold":"trumpOpposition",\
"trump opposition movement":"trumpOpposition",\
"villaraigosa":"trumpOpposition",\
"trading abuse":"trumpBusiness",\
"florida estate":"trumpBusiness",\
"hotel":"trumpBusiness",\
"property presidentelect donald trump":"trumpBusiness",\
"tower":"trumpBusiness",\
"trump international hotel":"trumpBusiness",\
"trump taj mahal casino":"trumpBusiness",\
"trump tower":"trumpBusiness",\
"trump tower buenos aire":"trumpBusiness",\
"trump vineyard estate":"trumpBusiness",\
"chiefofstaff":"trumpAdministration",\
"chiefofstaff john kelly":"trumpAdministration",\
"rob porter":"trumpAdministration",\
"confirmation process":"trumpAdministration",\
"skybridge capital":"trumpAdministration",\
"staff member":"trumpAdministration",\
"staffing challenge":"trumpAdministration",\
"staffing exodus":"trumpAdministration",\
"tweet":"trumpCommunication",\
"tweet saturday morning":"trumpCommunication",\
"tweeting":"trumpCommunication",\
"unitedStates":"unitedStates",\
"arizona capital":"unitedStates",\
"atlantic city":"unitedStates",\
"calexico":"unitedStates",\
"california berkeley":"unitedStates",\
"city":"unitedStates",\
"columbia":"unitedStates",\
"dearborn":"unitedStates",\
"new orleans":"unitedStates",\
"new york city":"unitedStates",\
"phoenix":"unitedStates",\
"san diego":"unitedStates",\
"san francisco":"unitedStates",\
"seattle":"unitedStates",\
"policy bank":"government",\
"appeal":"supremeCourt",\
"court":"supremeCourt",\
"judge":"supremeCourt",\
"ruling":"supremeCourt",\
"alabama us senate":"government",\
"american federalist system":"government",\
"appropriations committee":"government",\
"california democrats":"government",\
"chicago council":"government",\
"cia":"government",\
"civic committee":"government",\
"commerce department official":"government",\
"commerce departments inspector general":"government",\
"communication director":"government",\
"congressional budget office":"government",\
"congressional hispanic caucus":"government",\
"conservation voters":"government",\
"department authority":"government",\
"justice department":"government",\
"u official":"government",\
"us census bureau":"government",\
"us embassy":"government",\
"us house":"government",\
"us official":"government",\
"us state department":"government",\
"agriculture secretary sonny perdue":"usPolitician",\
"alabama sen jeff sessions":"usPolitician",\
"alaskas lisa murkowski":"usPolitician",\
"amy spitalnick":"usPolitician",\
"andrew cuomo":"usPolitician",\
"antonio villaraigosa":"usPolitician",\
"attorney general jeff sessions":"usPolitician",\
"becerra":"usPolitician",\
"betsy devos":"usPolitician",\
"bigcity mayor":"usPolitician",\
"bill frist":"usPolitician",\
"billionaire education secretary":"usPolitician",\
"boehner":"usPolitician",\
"carmen yulin cruz":"usPolitician",\
"carter page":"usPolitician",\
"chris collins":"usPolitician",\
"chuck":"usPolitician",\
"chuck rosenberg":"usPolitician",\
"congressional official":"usPolitician",\
"congressman mike capuano":"usPolitician",\
"connecticut democrat":"usPolitician",\
"connecticut gov":"usPolitician",\
"cornyn":"usPolitician",\
"cuomo":"usPolitician",\
"d massachusetts":"usPolitician",\
"d new york":"usPolitician",\
"dannel malloy":"usPolitician",\
"dean heller":"usPolitician",\
"delaware gov":"usPolitician",\
"dhs inspector general":"usPolitician",\
"dozen lawmaker":"usPolitician",\
"dozen us official":"usPolitician",\
"durbin":"usPolitician",\
"economic advisers chairman kevin hassett":"usPolitician",\
"education betsy devos":"usPolitician",\
"eric cantor":"usPolitician",\
"eric schneiderman":"usPolitician",\
"former clinton administration treasury secretary lawrence summers":"usPolitician",\
"governor":"usPolitician",\
"heath shuler":"usPolitician",\
"john mccain":"usPolitician",\
"lt gov":"usPolitician",\
"Marco Rubio":"usPolitician",\
"marcoRubio":"usPolitician",\
"marcoRubio":"usPolitician",\
"mayor":"usPolitician",\
"mcconnell":"usPolitician",\
"michael flynn":"usPolitician",\
"mick mulvaney":"usPolitician",\
"mike lee":"usPolitician",\
"mitch mcconnell":"usPolitician",\
"nancyPelosi":"usPolitician",\
"panetta":"usPolitician",\
"politician":"usPolitician",\
"reince priebus":"usPolitician",\
"representative":"usPolitician",\
"rex tillerson":"usPolitician",\
"richard blumenthal":"usPolitician",\
"rick perry":"usPolitician",\
"rick scott":"usPolitician",\
"rickPerry":"usPolitician",\
"rickScott":"usPolitician",\
"rickScott":"usPolitician",\
"ryan":"usPolitician",\
"sen jeff flake":"usPolitician",\
"senate majority leader mitch mcconnell":"usPolitician",\
"senate minority leader chuck schumer":"usPolitician",\
"senator":"usPolitician",\
"us president":"usPolitician",\
"usPolitician":"usPolitician",\
"alaska":"unitedStates",\
"arizonas capital":"unitedStates",\
"california":"unitedStates",\
"delaware":"unitedStates",\
"florida":"unitedStates",\
"georgia":"unitedStates",\
"hawaii":"unitedStates",\
"maryland":"unitedStates",\
"new york":"unitedStates",\
"new york time":"unitedStates",\
"north carolina":"unitedStates",\
"north dakota":"unitedStates",\
"ohio":"unitedStates",\
"oregon":"unitedStates",\
"state":"unitedStates",\
"texas":"unitedStates",\
"virginia":"unitedStates",\
"washington":"unitedStates",\
"berke bates":"violentCrime",\
"bomber":"violentCrime",\
"car attack":"violentCrime",\
"heather heyer":"violentCrime",\
"rape":"violentCrime",\
"terrorism":"violentCrime",\
"vehicle barrier":"violentCrime",\
"victim":"violentCrime",\
"violence":"violentCrime",\
"vladimir putin":"russiaElectionHacking",\
"estate tax":"taxes",\
"wealth":"taxes",\
"residence":"government",\
"ron johnson":"healthcare",\
"government":"government",\
"anthony kennedy":"supremecourtjudge",\
"chuck schumer":"democrat",\
"courtSystem":"travelBan",\
"president":"presidentDonaldTrump",\


}

#index keys are case sensitive, let's use all lower() to ensure success in match
concept_dict = {key.lower(): value for key, value in concept_dict.items()}
#todo: build case-insensitive matching

pickle.dump(concept_dict, open(pickle_path + 'concept_dict.p', 'wb'))
