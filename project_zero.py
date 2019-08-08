#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import tkinter as tk

def url_del(url):
    if url.find("http") == -1:
        if start_interface_1.var_http.get() != '':
            url=start_interface_1.var_http.get()+url
        else:
            url=None
    return url

def get_web_object(input_url):
    try:
        #print(bool(start_interface_1.var_verify.get()))
        resp=requests.get(input_url,verify=bool(start_interface_1.var_verify.get()))
        status_code = resp.status_code
        if status_code != 200:
            raise Exception("反饋異常"+str(status_code))
        print(input_url,status_code)
        web_object = resp.text
        
    except Exception as e:
        print("無法訪問，",repr(e))
        web_object=None
    return web_object

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
    
        self.status_block_x=200
        self.status_block_y=6
        self.title1 = tk.Label(master, text='等待輸入', bg='green', font=('Arial', 15), width=self.status_block_x, height=self.status_block_y)
        self.title1.pack()
        self.title1.place(x=(x_size/2)-(per_word_size*(self.status_block_x/2)), y=250, anchor='nw')

    def quit(self):
        self.master.destroy()

    def browse_mode(self):
        input_url = url_del(self.url_entry.get())
        if input_url == None:
            print("請確認輸入！")
            return 0
        web_object = get_web_object(input_url)
        #print(web_object)
        if web_object != None:
            self.quit()

    def code_mode(self):
        input_url = url_del(self.url_entry.get())
        if input_url == None:
            print("請確認輸入！")
            return 0
        web_object = get_web_object(input_url)
        #print(web_object)

    def password_mode(self):
        input_url = url_del(self.url_entry.get())
        if input_url == None:
            print("請確認輸入！")
            return 0
        web_object = get_web_object(input_url)
        #print(web_object)


start_window = tk.Tk()
x_size=700
y_size=400
start_window.title('Start Interface')
start_window.geometry(str(x_size)+'x'+str(y_size))
start_interface_1 = start_interface(x_size,y_size,start_window)
start_window.mainloop()