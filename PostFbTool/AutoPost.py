from tkinter import *
from time import sleep as sl
import requests
import processingAPI as pa

window = Tk()
window.title('Facebook Tools')
window.geometry('500x500')
icon = PhotoImage(file = 'fb1.png')
img = PhotoImage(file="fb.png")
label = Label(
    window,
    image=img
)
label.place(x = 0, y = 0)
notification = Label(window, text = 'Choose only 1 function', font=("Arial Bold", 30)).pack()


def Post():
	autoPost = Tk()
	autoPost.title('Post Status')

	cookie_label = Label(autoPost, text = 'Enter your cookie: ')
	cookie_label.pack()
	cookie = Entry(autoPost, width = 50)
	# cookie.insert(0, 'Enter the cookie: ')
	cookie.pack()


	content_label = Label(autoPost, text = 'Enter the content: ')
	content_label.pack()
	content = Entry(autoPost, width = 50)
	# content.insert(0, 'Enter the content: ')
	content.pack()

	quantity_label = Label(autoPost, text = 'Enter the quantity: ').pack()
	quantity = Entry(autoPost, width = 50)
	quantity.pack()
	

	def autoPostStatus():
		_content = content.get()
		_cookie = cookie.get()
		c_json = pa.convert_cookie_to_json(_cookie)
		fb_dtsg = pa.get_fb_dtsg(c_json)
		myID = c_json['c_user']
		url = "https://m.facebook.com/composer/mbasic/?av="+myID
		s = "."
		for i in range(int(quantity.get())):
			s += "."
			data = {
			'fb_dtsg': fb_dtsg,
			'privacyx': '300645083384735',
			'target': myID,
			'c_src': 'feed',
			'referrer': 'feed',
			'xc_message': _content+s,
			'view_post': 'Đăng',
			}
			requests.post(url,cookies =c_json,data = data)
			sl(1)
	try:		
		button = Button(autoPost, text = 'Post', command = autoPostStatus)
		button.pack()
	except:
		pass
	autoPost.mainloop()
def Send():
	autoSend = Tk()
	autoSend.title('Auto post Status Facebook')

	cookie_label = Label(autoSend, text = 'Enter your cookie: ')
	cookie_label.pack()
	cookie = Entry(autoSend, width = 50)
	# cookie.insert(0, 'Enter the cookie: ')
	cookie.pack()


	content_label = Label(autoSend, text = 'Enter the content: ')
	content_label.pack()
	content = Entry(autoSend, width = 50)
	# content.insert(0, 'Enter the content: ')
	content.pack()

	quantity_label = Label(autoSend, text = 'Enter the quantity: ').pack()
	quantity = Entry(autoSend, width = 50)
	quantity.pack()

	id_label = Label(autoSend, text = 'Enter the id facebook of friend: ').pack()
	idfb = Entry(autoSend, width = 50)
	idfb.pack()

	def sendMess1():
		_content = content.get()
		_cookie = cookie.get()
		c_json = pa.convert_cookie_to_json(_cookie)
		fb_dtsg = pa.get_fb_dtsg(c_json)
		myID = c_json['c_user']
		idSend = idfb.get()
		url = "https://mbasic.facebook.com/messages/send/?icm=1&refid=12"
		data = {
			'fb_dtsg': fb_dtsg,
			'body': _content,
			'wwwupp': 'C3',
			'ids['+idSend+']': idSend,
			'referrer': '',
			'ctype': '',
			'cver': 'legacy'
		}
		for i in range(int(quantity.get())):
			requests.post(url,cookies = c_json,data = data)
			sl(0.2)

	button = Button(autoSend, text = 'Send', command = sendMess1)
	button.pack()
	
button_post = Button(window, text = 'Post Status', command = Post).pack()
button_send = Button(window, text = 'Send Massage', command = Send).pack()
author = Label(window, text = 'Created by thayThanhdeeptry', font = ("Andale Mono", 20)).pack()
window.mainloop()