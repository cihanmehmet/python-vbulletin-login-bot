
import urllib, hashlib,urllib2
import re
from bs4 import BeautifulSoup
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler,urlopen
import cookielib,requests
def login(url, uname, passwd):
        loginurl = url + '/login.php?do=login'
        md5 = hashlib.md5(passwd);md5 = md5.hexdigest()
        cj = cookielib.CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())
        req = Request(url)
        f = opener.open(req)

        html = f.read()
        global headers
        headers = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
              }
        opts = {
        'vb_login_username':uname,
        'vb_login_password':passwd,
        's': '',
        'securitytoken':'guest',
        'do': 'login',
        'vb_login_md5password': md5,
        'vb_login_md5password_utf': md5
        }
        data = urllib.urlencode(opts)
        jar = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

        opener.addheader = headers
        """
        #opener.open(loginurl, data)
        response = opener.open(loginurl, data)
        #print response.read()

        response2 = opener.open(url, str(cj).strip('[]'))
        #print response2.read() """

##########################################################
def linkal(domain, link_listesi):

    i=0
    r = requests.get(domain)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a',id=True):
        if(link.string):
            print(link.get('href'))
            link_listesi.append(link.get('href'))
            i += 1
    return i
i=0
src = 'NULL'
liste=[]
domain ="http://www.forumsokagi.com" #str(raw_input('Forum Sitesinin Adresini yaziniz : '))
uname ="cihan"#str(raw_input('Kullanici Adini Giriniz: '))
passwd ="12345678" #str(raw_input('Sifrenizi Giriniz: '))
login(domain,uname,passwd)
girilecekYersayisi = linkal(domain,liste)

i = 0
print(str(girilecekYersayisi)+" kadar sayfayi denetleyecegim!")
for i in range(girilecekYersayisi):
    linkal(liste[i],liste)
print("####################################################################################################")
print len(liste)
for link in liste.findAll('a',href=True):
        if re.search("thread_title",str(link)):
            print link.get_text()
            link.append(liste)

