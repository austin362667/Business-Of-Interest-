#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import tkinter as tk
from tkinter import Scrollbar
from bs4 import BeautifulSoup
import sys
sys.setrecursionlimit(9000000)

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
del_saved_object=None
def get_web_object(input_url):
    global saved_web_object
    global del_saved_object
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
    if saved_web_object != None:
        del_saved_object = saved_web_object.replace(">",">\n")
#print(saved_web_object)
    return web_object

class getoutofloop(Exception): pass
class ErrorTags(Exception): pass

class code_interface(tk.Frame):
    def __init__(self,x_size,y_size,master=None):
        tk.Frame.__init__(self,master)
        self.pack()

        #print(saved_web_object)
        self.final_tag=None
        self.final_attr=None
        self.soup=None
        self.bs4_web_object = self.html_parse()
        
        self.var_web_object = tk.StringVar()
        self.var_web_object.set(self.bs4_web_object)
        self.per_word_size_2 = 700/77
        self.web_object_x=78
        self.web_object_y=24
        self.sb = Scrollbar(master)
        self.sb.pack(side="right",fill="y")
        self.per_word_size=250/19
        self.per_entry_size=250/30
        
        #self.web_object = tk.Label(master, wraplength = self.per_word_size_2*(self.web_object_x),textvariable=self.var_web_object, bg='green', width=self.web_object_x, height=self.web_object_y)
        self.web_object = tk.Text(master, bg='#66FF66', width=self.web_object_x, height=self.web_object_y,font=('Arial', 25),yscrollcommand=self.sb.set)
        self.web_object.insert("end",self.var_web_object.get())
        #self.web_object = scrolledtext.ScrolledText(master, wrap=tk.WORD, bg='green', width=self.web_object_x, height=self.web_object_y)
        self.web_object.pack()
        self.sb.config(command=self.web_object.yview)
        self.web_object.place(x=0, y=30, anchor='nw')
        
        self.var_show = tk.StringVar()
        self.var_show.set("等待操作")
        self.web_resp_x=78
        self.web_resp_y=3
        self.web_resp = tk.Text(master, bg='#33FFFF', width=self.web_resp_x, height=self.web_resp_y,font=('Arial', 25),yscrollcommand=self.sb.set)
        self.web_resp.insert("end",self.var_show.get())
        #self.web_object = scrolledtext.ScrolledText(master, wrap=tk.WORD, bg='green', width=self.web_object_x, height=self.web_object_y)
        self.web_resp.pack()
        self.sb.config(command=self.web_object.yview)
        self.web_resp.place(x=0, y=710, anchor='nw')
        
        self.title2_x=20
        self.title2_y=0
        self.title2 = tk.Label(master, text=saved_web_url, font=('Arial', 21), width=self.title2_x, height=self.title2_y)
        self.title2.pack()
        self.title2.place(x=10, y=0, anchor='nw')

        self.button_browse_x=7
        self.button_browse_y=1
        self.button_browse = tk.Button(master, text='瀏覽模式',font=('Arial', 24),command=self.browse_mode,highlightbackground='#3E4149',width=self.button_browse_x,height=self.button_browse_y)
        self.button_browse.pack()
        self.button_browse.place(x=1120, y=30, anchor='nw')
        
        self.button_code_x=9
        self.button_code_y=1
        self.button_code = tk.Button(master, text='原始碼模式',font=('Arial', 24),command=self.code_mode,highlightbackground='#3E4149',width=self.button_code_x,height=self.button_code_y)
        self.button_code.pack()
        self.button_code.place(x=1110, y=73, anchor='nw')
        
        self.button_password_x=8
        self.button_password_y=1
        self.button_password = tk.Button(master, text='登入模式',font=('Arial', 24),command=self.password_mode,highlightbackground='#3E4149',width=self.button_password_x,height=self.button_password_y)
        self.button_password.pack()
        self.button_password.place(x=1118, y=116, anchor='nw')

        self.trace_entry_1_x=16
        self.trace_entry_1 = tk.Entry(master,show=None, font=('Arial', 14),width=self.trace_entry_1_x)  # 顯示成明文形式
        self.trace_entry_1.pack()
        self.trace_entry_1.place(x=1118, y=170, anchor='nw')

        self.trace_entry_2_x=16
        self.trace_entry_2 = tk.Entry(master,show=None, font=('Arial', 14),width=self.trace_entry_2_x)  # 顯示成明文形式
        self.trace_entry_2.pack()
        self.trace_entry_2.place(x=1118, y=195, anchor='nw')

        self.trace_entry_3_x=16
        self.trace_entry_3 = tk.Entry(master,show=None, font=('Arial', 14),width=self.trace_entry_3_x)  # 顯示成明文形式
        self.trace_entry_3.pack()
        self.trace_entry_3.place(x=1118, y=220, anchor='nw')

        self.button_trace_x=8
        self.button_trace_y=1
        self.button_trace = tk.Button(master, text='追蹤目標',font=('Arial', 24),command=self.trace_func,highlightbackground='#3E4149',width=self.button_trace_x,height=self.button_trace_y)
        self.button_trace.pack()
        self.button_trace.place(x=1118, y=250, anchor='nw')
    
        self.button_get_out_x=8
        self.button_get_out_y=1
        self.button_get_out = tk.Button(master, text='開始擷取',font=('Arial', 24),command=self.get_out_func,highlightbackground='#3E4149',width=self.button_get_out_x,height=self.button_get_out_y)
        self.button_get_out.pack()
        self.button_get_out.place(x=1118, y=750, anchor='nw')
            
    def browse_mode(self):
        pass
    def code_mode(self):
        pass
    def password_mode(self):
        pass
    def html_parse(self):
        self.soup = BeautifulSoup(saved_web_object,"html.parser")
        #get_tags = soup.find_all("a")
        #for item in get_tags:
        #   print(item.text)
        return self.soup.prettify()
    def get_out_func(self):
        if self.final_tag!=None and self.final_attr!=None:
            try:
                get_tags = self.soup.find_all(self.final_tag)
                if len(get_tags)==0:
                    raise ErrorTags()
                get_list=[]
                mes=""
                for item in get_tags:
                    get_list.append(item[self.final_attr])
                    mes+=(item[self.final_attr]+"\n")
            except KeyError:
                mes="attr參數錯誤，請嘗試其他搜尋工具"
            except ErrorTags:
                mes="tag參數錯誤，請嘗試其他搜尋工具"
        else:
            mes="請先完成搜尋，再進行擷取！！！"
        self.var_show.set(mes)
        self.web_resp.delete('1.0', "end")
        self.web_resp.insert("end",self.var_show.get())
    def trace_func(self):
        str1=self.trace_entry_1.get()
        str2=self.trace_entry_2.get()
        str3=self.trace_entry_3.get()
        if str1=="" or str2=="" or str3=="":
            mes="請確認輸入！！！"
            self.var_show.set(mes)
            self.web_resp.delete('1.0', "end")
            self.web_resp.insert("end",self.var_show.get())
            return 0
        i1_list=[-1]
        i1_tags=[]
        i1_attr=[]
        i2_list=[-1]
        i2_attr=[]
        i2_tags=[]
        i3_list=[-1]
        i3_attr=[]
        i3_tags=[]
        while True:
            i1=self.bs4_web_object.find(str1,i1_list[-1]+1)
            #print(i1)
            if i1==-1:
                break
            else:
                i1_list.append(i1)
                catch = -1
                for j in range(i1,0,-1):
                    if catch != -1:
                        if self.bs4_web_object[j] == "<":
                            i1_tags.append(self.bs4_web_object[j+1:catch])
                            #print("---",self.bs4_web_object[j+1:catch])
                            break
                        elif self.bs4_web_object[j] == " ":
                            catch = j
                    elif self.bs4_web_object[j] == " ":
                        catch = j
                catch = -1
                for j in range(i1,0,-1):
                    if catch != -1:
                        if self.bs4_web_object[j] == " ":
                            i1_attr.append(self.bs4_web_object[j+1:catch])
                            break
                    elif self.bs4_web_object[j] == "=":
                        catch = j
                    elif self.bs4_web_object[j] == ">":
                        index = i1+len(str1)+1
                        while self.bs4_web_object[index] == " ":
                            index+=1
                        #print(self.bs4_web_object[index])
                        if self.bs4_web_object[index] == "<":
                            i1_attr.append("html_text")
                            break
        while True:
            i2=self.bs4_web_object.find(str2,i2_list[-1]+1)
            #print(i2)
            if i2==-1:
                break
            else:
                i2_list.append(i2)
                catch = -1
                for j in range(i2,0,-1):
                    if catch != -1:
                        if self.bs4_web_object[j] == "<":
                            i2_tags.append(self.bs4_web_object[j+1:catch])
                            break
                        elif self.bs4_web_object[j] == " ":
                            catch = j
                    elif self.bs4_web_object[j] == " ":
                        catch = j
                catch = -1
                for j in range(i2,0,-1):
                    if catch != -1:
                        if self.bs4_web_object[j] == " ":
                            i2_attr.append(self.bs4_web_object[j+1:catch])
                            break
                    elif self.bs4_web_object[j] == "=":
                        catch = j
                    elif self.bs4_web_object[j] == ">":
                        index = i2+len(str2)+1
                        while self.bs4_web_object[index] == " ":
                            index+=1
                        print(self.bs4_web_object[index])
                        if self.bs4_web_object[index] == "<":
                            i2_attr.append("html_text")
                            break
        while True:
            i3=self.bs4_web_object.find(str3,i3_list[-1]+1)
            #print(i3)
            if i3==-1:
                break
            else:
                i3_list.append(i3)
                catch = -1
                for j in range(i3,0,-1):
                    if catch != -1:
                        if self.bs4_web_object[j] == "<":
                            i3_tags.append(self.bs4_web_object[j+1:catch])
                            break
                        elif self.bs4_web_object[j] == " ":
                            catch = j
                    elif self.bs4_web_object[j] == " ":
                        catch = j
                catch = -1
                for j in range(i3,0,-1):
                    if catch != -1:
                        if self.bs4_web_object[j] == " ":
                            i3_attr.append(self.bs4_web_object[j+1:catch])
                            break
                    elif self.bs4_web_object[j] == "=":
                        catch = j
                    elif self.bs4_web_object[j] == ">":
                        index = i3+len(str3)+1
                        while self.bs4_web_object[index] == " ":
                            index+=1
                        print(self.bs4_web_object[index])
                        if self.bs4_web_object[index] == "<":
                            i3_attr.append("html_text")
                            break
    
        try:
            for tag1 in i1_tags:
                for tag2 in i2_tags:
                    for tag3 in i3_tags:
                        if tag1==tag2 and tag2==tag3:
                            self.final_tag=tag1
                            raise getoutofloop()
        except getoutofloop:
            pass
        try:
            for attr1 in i1_attr:
                for attr2 in i2_attr:
                    for attr3 in i3_attr:
                        if attr1==attr2 and attr2==attr3:
                            self.final_attr=attr1
                            raise getoutofloop()
        except getoutofloop:
            pass
        if self.final_tag!=None and self.final_attr!=None:
            mes="驗證完成，可以截取！"+"\n"+"1.tag = "+str(i1_tags)+" 1.attr = "+str(i1_attr)+"\n"+"2.tag = "+str(i2_tags)+" 2.attr = "+str(i2_attr)+"\n"+"3.tag = "+str(i3_tags)+" 3.attr = "+str(i3_attr)
        else:
            mes="驗證失敗，無法擷取，請確認輸入資料是否規律！！！"+"\n"+"1.tag = "+str(i1_tags)+" 1.attr = "+str(i1_attr)+"\n"+"2.tag = "+str(i2_tags)+" 2.attr = "+str(i2_attr)+"\n"+"3.tag = "+str(i3_tags)+" 3.attr = "+str(i3_attr)
        self.var_show.set(mes)
        self.web_resp.delete('1.0', "end")
        self.web_resp.insert("end",self.var_show.get())

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
        self.url_entry.insert("end","www.google.com")
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
