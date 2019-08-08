#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import tkinter as tk
from tkinter import Scrollbar

saved_web_url=None
def url_del(url):
    global saved_web_url
    if url.find("http") == -1:
        if start_interface_1.var_http.get() != '':
            url=start_interface_1.var_http.get()+url
        else:
            url=None
    saved_web_url=url
    return url

saved_web_object=None
def get_web_object(input_url):
    global saved_web_object
    try:
        #print(bool(start_interface_1.var_verify.get()))
        print(saved_web_object)
        resp=requests.get(input_url,verify=bool(start_interface_1.var_verify.get()))
        status_code = resp.status_code
        if status_code != 200:
            raise Exception("反饋異常"+str(status_code))
            start_interface_1.var_status.set("反饋異常"+str(status_code))
        print(input_url,status_code)
        web_object = resp.text
    except Exception as e:
        print("無法訪問，",repr(e))
        start_interface_1.var_status.set("無法訪問，"+str(repr(e)))
        web_object=None
    saved_web_object=web_object
#print(saved_web_object)
    return web_object

class code_interface(tk.Frame):
    def __init__(self,x_size,y_size,master=None):
        tk.Frame.__init__(self,master)
        self.pack()

        #print(saved_web_object)
        
        
        self.var_web_object = tk.StringVar()
        self.var_web_object.set(saved_web_object)
        self.per_word_size_2 = 700/77
        self.web_object_x=78
        self.web_object_y=27
        self.sb = Scrollbar(master)
        self.sb.pack(side="right",fill="y")
        #self.web_object = tk.Label(master, wraplength = self.per_word_size_2*(self.web_object_x),textvariable=self.var_web_object, bg='green', width=self.web_object_x, height=self.web_object_y)
        self.web_object = tk.Text(master, bg='green', width=self.web_object_x, height=self.web_object_y,font=('Arial', 25),yscrollcommand=self.sb.set)
        self.web_object.insert("end",self.var_web_object.get())
        #self.web_object = scrolledtext.ScrolledText(master, wrap=tk.WORD, bg='green', width=self.web_object_x, height=self.web_object_y)
        self.web_object.pack()
        self.sb.config(command=self.web_object.yview)
        self.web_object.place(x=0, y=30, anchor='nw')

selected_mode = 0
class start_interface(tk.Frame):
    def __init__(self,x_size,y_size,master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        
        per_word_size=250/19
        per_entry_size=250/30

        self.title1_x=20
        self.title1_y=2
        self.title1 = tk.Label(master, text='自動化爬蟲工具', bg='green', font=('Arial', 24), width=self.title1_x, height=self.title1_y)
        self.title1.pack()
        self.title1.place(x=(x_size/2)-(per_word_size*(self.title1_x/2)), y=10, anchor='nw')

        self.url_entry_x=40
        self.url_entry = tk.Entry(master,show=None, font=('Arial', 14),width=self.url_entry_x)  # 顯示成明文形式
        self.url_entry.pack()
        self.url_entry.place(x=(x_size/2)-(per_entry_size*(self.url_entry_x/2))-40, y=110, anchor='nw')

        self.button_html_x=8
        self.button_html_y=1
        self.var_http = tk.StringVar()
        self.var_http.set("https://")
        self.button_http = tk.Radiobutton(master, text='http', variable=self.var_http, value='http://',bg='blue')
        self.button_http.pack()
        self.button_https = tk.Radiobutton(master, text='https', variable=self.var_http, value='https://',bg='blue')
        self.button_https.pack()
        self.button_http.place(x=((x_size/4)*3)-(per_word_size*(self.button_html_x/2))+70, y=100, anchor='nw')
        self.button_https.place(x=((x_size/4)*3)-(per_word_size*(self.button_html_x/2))+70, y=130, anchor='nw')

        self.button_verify_x=8
        self.button_verify_y=1
        self.var_verify = tk.BooleanVar()
        self.var_verify.set(True)
        self.button_verify = tk.Radiobutton(master, text='Ignore SSL Verify', variable=self.var_verify, value=False,bg='red')
        self.button_verify.pack()
        self.button_verify.place(x=((x_size/4)*3)-(per_word_size*(self.button_verify_x/2))+70, y=70, anchor='nw')
        
        self.button_browse_x=7
        self.button_browse_y=1
        self.button_browse = tk.Button(master, text='瀏覽模式',font=('Arial', 24),command=self.browse_mode,highlightbackground='#3E4149',width=self.button_browse_x,height=self.button_browse_y)
        self.button_browse.pack()
        self.button_browse.place(x=(x_size/4)-(per_word_size*(self.button_browse_x/2))-40, y=200, anchor='nw')

        self.button_code_x=9
        self.button_code_y=1
        self.button_code = tk.Button(master, text='原始碼模式',font=('Arial', 24),command=self.code_mode,highlightbackground='#3E4149',width=self.button_code_x,height=self.button_code_y)
        self.button_code.pack()
        self.button_code.place(x=((x_size/4)*2)-(per_word_size*(self.button_browse_x/2))-35, y=200, anchor='nw')

        self.button_password_x=8
        self.button_password_y=1
        self.button_password = tk.Button(master, text='登入模式',font=('Arial', 24),command=self.password_mode,highlightbackground='#3E4149',width=self.button_password_x,height=self.button_password_y)
        self.button_password.pack()
        self.button_password.place(x=((x_size/4)*3)-(per_word_size*(self.button_password_x/2)), y=200, anchor='nw')
    
        self.var_status = tk.StringVar()
        self.var_status.set("等待輸入")
        self.per_word_size_2 = 700/77
        self.status_block_x=60
        self.status_block_y=7
        self.title1 = tk.Label(master, wraplength = self.per_word_size_2*(self.status_block_x),textvariable=self.var_status, bg='green', width=self.status_block_x, height=self.status_block_y)
        self.title1.pack()
        self.title1.place(x=(x_size/2)-(self.per_word_size_2*(self.status_block_x/2)), y=250, anchor='nw')

    def quit(self):
        self.master.destroy()

    def browse_mode(self):
        global selected_mode
        selected_mode=1
        input_url = url_del(self.url_entry.get())
        if input_url == None:
            print("請確認輸入！")
            return 0
        web_object = get_web_object(input_url)
        #print(web_object)
        if web_object != None:
            self.quit()

    def code_mode(self):
        global selected_mode
        selected_mode=2
        input_url = url_del(self.url_entry.get())
        if input_url == None:
            print("請確認輸入！")
            return 0
        web_object = get_web_object(input_url)
        #print(web_object)
        if web_object != None:
            self.quit()

    def password_mode(self):
        global selected_mode
        selected_mode=3
        input_url = url_del(self.url_entry.get())
        if input_url == None:
            print("請確認輸入！")
            return 0
        web_object = get_web_object(input_url)
        #print(web_object)
        if web_object != None:
            self.quit()

start_window = tk.Tk()
x_size=700
y_size=400
start_window.title('Start Interface')
start_window.geometry(str(x_size)+'x'+str(y_size))
start_interface_1 = start_interface(x_size,y_size,start_window)
start_window.mainloop()

#print(saved_web_object)
if selected_mode==0:
    exit()
elif selected_mode == 1:
    pass
elif selected_mode == 2:
    code_window = tk.Tk()
    x_size=1280
    y_size=800
    code_window.title('Code Interface')
    code_window.geometry(str(x_size)+'x'+str(y_size))
    code_interface_1 = code_interface(x_size,y_size,code_window)
    code_window.mainloop()
elif selected_mode == 3:
    pass
