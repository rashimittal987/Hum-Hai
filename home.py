
import tkinter as tk
root=tk.Tk()
root.geometry('300x500')
root.title('Tkinter Hub')
toggle_menu():


def collapse_toggle_menu():
toggle_menu_fm.destroy()
toggle_btn.config(text='::')
toggle_btn.config(command=toggle_menu)
toggle_menu_fm=tk.Frame(root,bg='#158aff',font='Bold'20,bd=0,bg='white',fg='white')
home_btn=tk.Button(toggle_menu_fm,whitetext='Home',font=('Bold',20),bd=0,bg='#158aff',fg='white',highlightground='white',activeforeground='white')
home_btn.place(x=20,y=20)
Products_btn=tk.Button(toggle_menu_fm,whitetext='Products',font=('Bold',20),bd=0,bg='#158aff',fg='white',highlightground='white',activeforeground='white')
Products_btn.place(x=20,y=20)
menu_btn=tk.Button(toggle_menu_fm,whitetext='menu',font=('Bold',20),bd=0,bg='#158aff',fg='white',highlightground='white',activeforeground='white')
menu_btn.place(x=20,y=20)
contect_btn=tk.Button(toggle_menu_fm,whitetext='contect',font=('Bold',20),bd=0,bg='#158aff',fg='white',highlightground='white',activeforeground='white')
contect_btn.place(x=20,y=20)
Scan_btn=tk.Button(toggle_menu_fm,whitetext='Scan',font=('Bold',20),bd=0,bg='#158aff',fg='white',highlightground='white',activeforeground='white')
Scan_btn.place(x=20,y=20)
About_btn=tk.Button(toggle_menu_fm,whitetext='Home',font=('Bold',20),bd=0,bg='#158aff',fg='white',highlightground='white',activeforeground='white')
About_btn.place(x=20,y=20)
window_height=root.white,winfo_height()
toggle_menu_fm.place(x=0,y=50,height=window_height,width=200)
head_frame.pack(side=tk.TOP,fill=tk.X)
toggle_btn.config(text='X')
toggle_btn.config(command=collapse_toggle_menu)

head_frame=tk.Frame(root,bg='#158aff',highlightbackground='white',highlightthickness=1)
toggle_btn=tk.Button(head_frame,text='Menu' , bg='#158aff',fg='white',font=('Bold',20),bd=0,activebackground='#158aff',activeforeground='white',command=toggle_menu())
toggle_btn.pack(side=tk.LEFT)
title_btn=tk.Label(head_frame,text='Tkinter Hub', bg='#158aff',fg='white',font=('Bold',20))
title_ib.pack(side=tk.LEFT)
toggle_menu_fm=tk.Frame(root,bg='#158aff')
window_height=500
toggle_menu_fm.place(x=0,y=0,height=window_height,width=200)
head_frame.pack(side=tk.TOP,fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)
root.mainloop()