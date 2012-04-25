#!/usr/bin/python
import urllib
import urllib2
 
def login():
    url = "https://login.keycom.co.uk:8090/goform/HtmlLoginRequest"
    
    opts = {
    'username': 'trolol',#insert your username here
    'password': 'nva955',#and your password here
    'original_url': 'https://mail.google.com',
    'login': 'Sign in'
    }
 
    data = urllib.urlencode(opts)
 
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12',
    'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
    'Accept-Language': 'en-gb,en;q=0.5',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    'Connection': 'keep-alive',
    'Origin': "https://login.keycom.co.uk:8090",
    'Referer': 'https://login.keycom.co.uk:8090/index.asp'
    }
 
    req = urllib2.Request(url, data, headers)
 
    response = urllib2.urlopen(req)
    return response.read()

if __name__ == '__main__':
    login()

#alternative using curl - curl -d "username= &password= &login=Sign in" https://login.keycom.co.uk:8090/goform/HtmlLoginRequest

