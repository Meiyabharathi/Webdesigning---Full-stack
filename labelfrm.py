import tkinter as tk
from tkinter import messagebox
import mysql.connector as arivu
import os
from twilio.rest import Client

# ================= MYSQL CONNECTION =================

mydb=arivu.connect(host="localhost",user="root",password="1234",database="market",auth_plugin='mysql_native_password')

mycursor=mydb.cursor()

account_sid = "AC72fa8643592f9f38754abfb8fbdfdb28"
auth_token = "1df8a4d106b24d071a2771f639725970"
twilio_number = "+16076227861"   # Your Twilio number

client = Client(account_sid, auth_token)
# Folder path
folder_path=r"D:\\Python\\New folder"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)


# ================= LOGIN WINDOW =================

def check_login():

    if username.get()=="admin" and password.get()=="1234":

        login.destroy()
        open_billing()

    else:
        messagebox.showerror("Error","Wrong Username or Password")


login=tk.Tk()
login.title("Login Window")
login.geometry("300x200")

username=tk.StringVar()
password=tk.StringVar()

tk.Label(login,text="LOGIN",
font=("Arial",16,"bold")).pack(pady=10)

tk.Label(login,text="Username").pack()
tk.Entry(login,textvariable=username).pack()

tk.Label(login,text="Password").pack()
tk.Entry(login,textvariable=password,show="*").pack()

tk.Button(login,
text="Login",
bg="green",
fg="white",
command=check_login).pack(pady=10)



# ================= BILLING SOFTWARE =================

def open_billing():

    root=tk.Tk()
    root.title("Billing Software")
    root.geometry("1400x700")

    # CUSTOMER

    frame1=tk.LabelFrame(root,
    text="Billing Software",
    fg="blue",
    font=("Arial",10,"bold"),
    bd=10)

    frame1.place(x=0,y=0,width=1400,height=100)

    global customername,customermobile

    customername=tk.StringVar()
    customermobile=tk.StringVar()

    tk.Label(frame1,text="Customer Name").place(x=20,y=20)
    tk.Entry(frame1,textvariable=customername,width=25).place(x=150,y=20)

    tk.Label(frame1,text="Customer Mobile").place(x=400,y=20)
    tk.Entry(frame1,textvariable=customermobile,width=25).place(x=550,y=20)


    # ================= GROCERIES =================

    frame2=tk.LabelFrame(root,
    text="Groceries",
    fg="blue",
    font=("Arial",10,"bold"),
    bd=10)

    frame2.place(x=0,y=100,width=400,height=500)

    global soap,oil,paste,Daal,Wheat,Sugar
    global Vegetables,Biscuits,Rusk,Banana,Mango

    soap=tk.StringVar()
    oil=tk.StringVar()
    paste=tk.StringVar()
    Daal=tk.StringVar()
    Wheat=tk.StringVar()
    Sugar=tk.StringVar()
    Vegetables=tk.StringVar()
    Biscuits=tk.StringVar()
    Rusk=tk.StringVar()
    Banana=tk.StringVar()
    Mango=tk.StringVar()

    groceries=[

    ("Soap",soap),
    ("Oil",oil),
    ("Paste",paste),
    ("Daal",Daal),
    ("Wheat",Wheat),
    ("Sugar",Sugar),
    ("Vegetables",Vegetables),
    ("Biscuits",Biscuits),
    ("Rusk",Rusk),
    ("Banana",Banana),
    ("Mango",Mango)

    ]

    y=10

    for item,var in groceries:

        tk.Label(frame2,text=item).place(x=10,y=y)

        tk.Entry(frame2,
        textvariable=var,
        width=20).place(x=150,y=y)

        y+=40


    # ================= COSMETICS =================

    frame3=tk.LabelFrame(root,
    text="Cosmetics",
    fg="blue",
    font=("Arial",10,"bold"),
    bd=10)

    frame3.place(x=400,y=100,width=400,height=500)

    global Bathsoap,Facewash,Facecream,Lippalm
    global vaseline,Ponds,Fairandlovely
    global Sunscreen,Moisturizer,Bodyspray
    global Lipstick,Axe

    Bathsoap=tk.StringVar()
    Facewash=tk.StringVar()
    Facecream=tk.StringVar()
    Lippalm=tk.StringVar()
    vaseline=tk.StringVar()
    Ponds=tk.StringVar()
    Fairandlovely=tk.StringVar()
    Sunscreen=tk.StringVar()
    Moisturizer=tk.StringVar()
    Bodyspray=tk.StringVar()
    Lipstick=tk.StringVar()
    Axe=tk.StringVar()

    cosmetics=[

    ("Bathsoap",Bathsoap),
    ("Facewash",Facewash),
    ("Facecream",Facecream),
    ("Lippalm",Lippalm),
    ("Vaseline",vaseline),
    ("Ponds",Ponds),
    ("Fairandlovely",Fairandlovely),
    ("Sunscreen",Sunscreen),
    ("Moisturizer",Moisturizer),
    ("Bodyspray",Bodyspray),
    ("Lipstick",Lipstick),
    ("Axe",Axe)

    ]

    y=10

    for item,var in cosmetics:

        tk.Label(frame3,text=item).place(x=10,y=y)

        tk.Entry(frame3,
        textvariable=var,
        width=20).place(x=150,y=y)

        y+=40


    # ================= BILL AREA =================

    frame4=tk.LabelFrame(root,
    text="Bill Area",
    fg="blue",
    font=("Arial",10,"bold"),
    bd=10)

    frame4.place(x=800,y=100,width=500,height=500)

    global bill_text

    bill_text=tk.Text(frame4,width=60,height=25)

    bill_text.place(x=5,y=5)



    # ================= GENERATE BILL =================

    def generate_bill():

        bill_text.delete('1.0',tk.END)

        grand_total=0

        filename=folder_path+"\\"+customername.get()+".txt"

        file=open(filename,"w")

        title="        BILL RECEIPT\n"
        line="===============================\n"

        bill_text.insert(tk.END,title)
        bill_text.insert(tk.END,line)

        file.write(title)
        file.write(line)

        name="Name : "+customername.get()+"\n"
        mobile="Mobile : "+customermobile.get()+"\n"

        bill_text.insert(tk.END,name)
        bill_text.insert(tk.END,mobile)

        file.write(name)
        file.write(mobile)

        bill_text.insert(tk.END,line)
        file.write(line)

        products={

        "Soap":soap.get(),
        "Oil":oil.get(),
        "Paste":paste.get(),
        "Daal":Daal.get(),
        "Wheat":Wheat.get(),
        "Sugar":Sugar.get(),
        "Vegetables":Vegetables.get(),
        "Biscuits":Biscuits.get(),
        "Rusk":Rusk.get(),
        "Banana":Banana.get(),
        "Mango":Mango.get(),

        "Bathsoap":Bathsoap.get(),
        "Facewash":Facewash.get(),
        "Facecream":Facecream.get(),
        "Lippalm":Lippalm.get(),
        "vaseline":vaseline.get(),
        "Ponds":Ponds.get(),
        "Fairandlovely":Fairandlovely.get(),
        "Sunscreen":Sunscreen.get(),
        "Moisturizer":Moisturizer.get(),
        "Bodyspray":Bodyspray.get(),
        "Lipstick":Lipstick.get(),
        "Axe":Axe.get()

        }


        prices={

        "Soap":20,"Oil":120,"Paste":50,"Daal":80,
        "Wheat":60,"Sugar":45,"Vegetables":40,
        "Biscuits":10,"Rusk":30,"Banana":5,"Mango":20,

        "Bathsoap":35,"Facewash":90,"Facecream":120,
        "Lippalm":60,"vaseline":70,"Ponds":110,
        "Fairandlovely":150,"Sunscreen":200,
        "Moisturizer":180,"Bodyspray":250,
        "Lipstick":120,"Axe":300

        }


        for item in products:

            qty_str=products[item]

            if qty_str!="":

                qty=int(qty_str)

                price=prices[item]

                total=qty*price

                grand_total+=total

                text=f"{item}   {qty}   {price}   {total}\n"

                bill_text.insert(tk.END,text)
                file.write(text)


                sql="INSERT INTO super(customername,customermobile,productname,quantity,total) VALUES(%s,%s,%s,%s,%s)"

                val=(customername.get(),
                customermobile.get(),
                item,
                qty,
                total)

                mycursor.execute(sql,val)
                mydb.commit()


        total_line="===============================\nGrand Total = "+str(grand_total)

        bill_text.insert(tk.END,total_line)
        file.write(total_line)

        file.close()
        try:
            message = client.messages.create(
                body=f"Hello {customername.get()}, Your Bill Total is Rs {grand_total}. Thank you for shopping!",
                from_=twilio_number,
                to="+91"+customermobile.get())

            messagebox.showinfo("Success", "Bill Saved & SMS Sent")

        except Exception as e:
            messagebox.showerror("SMS Error", str(e))
            print(str(e))

        

        messagebox.showinfo("Saved","Bill Saved in D Drive")


    # ================= CLEAR =================

    def clear_data():

        customername.set("")
        customermobile.set("")

        for var in [soap,oil,paste,Daal,Wheat,Sugar,
        Vegetables,Biscuits,Rusk,Banana,Mango,
        Bathsoap,Facewash,Facecream,Lippalm,
        vaseline,Ponds,Fairandlovely,Sunscreen,
        Moisturizer,Bodyspray,Lipstick,Axe]:

            var.set("")

        bill_text.delete('1.0',tk.END)



    # ================= BUTTONS =================

    tk.Button(root,text="Generate Bill",
    bg="green",fg="white",
    font=("Arial",12,"bold"),
    command=generate_bill).place(x=900,y=620)

    tk.Button(root,text="Clear",
    bg="orange",
    font=("Arial",12,"bold"),
    command=clear_data).place(x=1050,y=620)

    tk.Button(root,text="Exit",
    bg="red",fg="white",
    font=("Arial",12,"bold"),
    command=root.destroy).place(x=1150,y=620)

    root.mainloop()


login.mainloop()
