#import pickle
#if __name__ == '__main__':
#    pickle_path = "C:/temp/NU/453/pickle/" #where do you want to read / write the phrase list / filters, etc.

concept_dict = {

#===================Begin pasted section from excel generator=============
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
"anthony scaramucci":"americanBusiness",\
"carl c icahn":"americanBusiness",\
"casino magnate phil ruffin":"americanBusiness",\
"ceo mark zuckerberg":"americanBusiness",\
"christopher steele":"americanBusiness",\
"david koch":"americanBusiness",\
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
"deliberation":"arms",\
"comment period":"arms",\
"bali":"asianNations",\
"taiwan":"asianNations",\
"taiwan amid":"asianNations",\
"chinas president xi jinping":"asianNations",\
"chinese official":"asianNations",\
"duterte":"asianNations",\
"foreign minister yun byungse":"asianNations",\
"rodrigo duterte":"asianNations",\
"shinzo abe":"asianNations",\
"east asia":"asianNations",\
"india":"asianNations",\
"mumbai":"asianNations",\
"japan":"asianNations",\
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
"joe biden":"barackObama",\
"susan e rice":"barackObama",\
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
"border security budget document":"borderSecurity",\
"border security issue":"borderSecurity",\
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
"big bend":"borderWall",\
"rio grande valley":"borderWall",\
"border wall prototype":"borderWall",\
"congresss budget process":"budget",\
"agriculture":"budget",\
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
"commerce":"business",\
"cuba":"centralAmericanNations",\
"havana":"centralAmericanNations",\
"little havana":"centralAmericanNations",\
"manuel artime theater":"centralAmericanNations",\
"mr obamas cuba policy":"centralAmericanNations",\
"security service":"centralAmericanNations",\
"travel":"centralAmericanNations",\
"haiti":"centralAmericanNations",\
"sofla community":"centralAmericanNations",\
"mexico":"centralAmericanNations",\
"puerto rico":"centralAmericanNations",\
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
"crouching tiger":"china",\
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
"emission":"climateChange",\
"decree":"climatechange",\
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
"video":"communication",\
"agreement mr trump":"communication",\
"dealmaker":"communication",\
"envoy":"communication",\
"actions speak louder than words realm":"communication",\
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
"acosta":"controversy",\
"circulation":"controversy",\
"cox medium institute":"controversy",\
"fake news mainstream medium":"controversy",\
"fake news medium":"controversy",\
"fake news network":"controversy",\
"godwins law":"controversy",\
"nazi comparison":"controversy",\
"refugee":"controversy",\
"refuge":"controversy",\
"refugee policy":"controversy",\
"collusion":"controversy",\
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
"opposition agenda":"democrat",\
"nancyPelosi":"democrat",\
"chuck schumer":"democrat",\
"agriculture something":"domesticPolicy",\
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
"law enforcement":"domesticPolicy",\
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
"gdp":"economy",\
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
"congresss approval":"energy",\
"chris warren":"energy",\
"coal industry":"energy",\
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
"fuel capability":"energy",\
"fuel industry stooge":"energy",\
"fuel production":"energy",\
"fuel source":"energy",\
"fuel technology company":"energy",\
"gasoline price":"energy",\
"appalachian":"energy",\
"atlantic":"energy",\
"atlantic ocean":"energy",\
"gas company":"energy",\
"gas exploration":"energy",\
"gas leasing program":"energy",\
"gas power plant":"energy",\
"fuel supply":"energy",\
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
"solar":"energy",\
"suniva":"energy",\
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
"damage settlement":"environmental",\
"senator maggie hassan":"environmental",\
"sierra club":"environmental",\
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
"angela merkel":"europeanNation",\
"naples":"europeanNation",\
"kalugin":"europeanNation",\
"moscow":"europeanNation",\
"putin":"europeanNation",\
"russia":"europeanNation",\
"russian":"europeanNation",\
"soviet republic":"europeanNation",\
"soviet union":"europeanNation",\
"aleksey pushkov":"europeanNation",\
"discussion grows":"fakeNews",\
"comey firing":"fbi",\
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
"farmer":"foreignPolicy",\
"force":"foreignPolicy",\
"audience wider":"foreignPolicy",\
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
"congress":"government",\
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
"florida republicans":"government",\
"hill member":"government",\
"house appropriation committee":"government",\
"houseAppropriationCommittee":"government",\
"redstate senator":"government",\
"renegade republican":"government",\
"tea party":"government",\
"trump ally":"government",\
"paul ryan":"government",\
"attorney general":"government",\
"policy bank":"government",\
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
"governor":"government",\
"mayor":"government",\
"politician":"government",\
"residence":"government",\
"government":"government",\
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
"alzheimer":"healthcare",\
"american medical association":"healthcare",\
"cancer":"healthcare",\
"care physician":"healthcare",\
"doctor":"healthcare",\
"dr joseph mason":"healthcare",\
"drug":"healthcare",\


#===============end pasted section=================================


}

#index keys are case sensitive, let's use all lower() to ensure success in match
concept_dict = {key.lower(): value for key, value in concept_dict.items()}
#Note: I keep values as-is, to improve readability (even if it creates matching headaches for index look-ups)

#todo: build case-insensitive matching, and replace all .lower() calls

#pickle.dump(concept_dict, open(pickle_path + 'concept_dict.p', 'wb'))
