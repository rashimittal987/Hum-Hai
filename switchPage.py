import tkinter as tk

root=tk.Tk()
root.geometry('1925x1500')
root.title('Tkinter Hub')

def home_page():
    home_frame=tk.Frame(main_frame)
    lb=tk.Label(home_frame,text='Home Page\n\nPage:2',font=('Bold',30))
    lb.pack()
    home_frame.pack(pady=20)
def contact_us_page():
    contact_us_frame=tk.Frame(main_frame)
    lb=tk.Label(contact_us_frame,text='Home Page\n\nPage:7',font=('Bold',30))
    lb.pack()
    contact_us_frame.pack(pady=20)
def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    contact_us_indicate.config(bg='#c3c3c3')
    About_indicate.config(bg='#c3c3c3')
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
def About_page():
    About_frame=tk.Frame(main_frame)
    lb=tk.Label(About_frame,text='Home Page\n\nPage:8',font=('Bold',30))
    lb.pack()
    About_frame.pack(pady=20)
def indicate(lb,page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()
option_frame=tk.Frame(root,bg='#c3c3c3')
home_btn=tk.Button(option_frame,text='Home',font=('Bold',15),fg='#158aff',bd=0,bg='#c3c3c3',command=lambda:indicate(home_indicate,home_page))
home_btn.place(x=10,y=50)

home_indicate=tk.Label(option_frame,text='',bg='#c3c3c3')
home_indicate.place(x=3,y=50,width=5,height=40)

contact_us_btn=tk.Button(option_frame,text='Contact Us',font=('Bold',15),fg='#158aff',bd=0,bg='#c3c3c3',command=lambda:indicate(contact_us_indicate,contact_us_page))
contact_us_btn.place(x=10,y=100)
contact_us_indicate=tk.Label(option_frame,text='',bg='#c3c3c3')
contact_us_indicate.place(x=3,y=100,width=5,height=40)
About_btn=tk.Button(option_frame,text='About',font=('Bold',15),fg='#158aff',bd=0,bg='#c3c3c3',command=lambda:indicate(About_indicate,About_page))
About_btn.place(x=10,y=150)
About_indicate=tk.Label(option_frame,text='',bg='#c3c3c3')
About_indicate.place(x=3,y=150,width=5,height=40)
option_frame.pack(side=tk.LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=125,height=400)

main_frame=tk.Frame(root,highlightbackground='black',highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400,width=500)
root.mainloop()