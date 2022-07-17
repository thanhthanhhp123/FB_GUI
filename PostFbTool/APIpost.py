from http.cookies import SimpleCookie
from bs4 import BeautifulSoup as BS
import requests
import time

def cut_string(string,key,choice):
	index = string.find(key)
	if choice:
		string = string[index+len(key):]
	else:
		string = string[0:index]
	return string


def get_fb_dtsg(cookies):
	try:
		gets = requests.get("https://www.facebook.com",cookies = cookies)
		soup = BS(gets.content, "html.parser")
		gets = str(gets.text)
		gets = cut_string(gets,'["DTSGInitialData",[],{"token":"',True)
		gets = cut_string(gets,'"',False)
		return gets
	except:
		return None

def convert_cookie_to_json(string_cookie):
	temp= string_cookie.replace(" ", "")
	temp = temp.split(";")
	listKey = ["sb","datr","c_user","xs","fr"]
	listCookies = []
	for i in temp:
		key = i.split("=")[0]
		if key in listKey:
			listCookies.append(i)
	string_cookie=";".join(listCookies)
	try:
		cookie = SimpleCookie()
		cookie.load(string_cookie)
		cookies = {}
		for key, morsel in cookie.items():
		    cookies[key] = morsel.value
		return cookies
	except:
		return ""

def autoPostStatus(content,fb_dtsg,cookies):
	myID = cookies['c_user']
	url = "https://m.facebook.com/composer/mbasic/?av="+myID
	data = {
		'fb_dtsg': fb_dtsg,
		'privacyx': '300645083384735',
		'target': myID,
		'c_src': 'feed',
		'referrer': 'feed',
		'xc_message': content,
		'view_post': 'Đăng',
	}
	requests.post(url,cookies =cookies,data = data)

cookies = "sb=32h2YpGZHN0H8jqsrQPEWvoC;datr=32h2Ylbwnubnj0KaDi6cMwsj;dpr=2;locale=vi_VN;c_user=100083190725406;wd=429x667;xs=26%3AXX47YMeEMVwsIQ%3A2%3A1657108623%3A-1%3A-1%3A%3AAcUQmLKJhcqFFWwZc1xR1Tw6onAIdchsz6eywO6brw;fr=0uLoxFDrX6C3N4i65.AWVuPzKzo5-3sCFugFtnZJLMa5E.BixcnT.bO.AAA.0.0.BixcnT.AWXg4nU5sRI;"
c_json=convert_cookie_to_json(cookies)
fb_dtsg = get_fb_dtsg(c_json)

autoPostStatus('Thanhdz1', fb_dtsg, c_json)
