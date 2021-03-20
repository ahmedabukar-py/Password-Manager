from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ------------------------GENERATE PASSWORD-----------------------------
def random_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# --------------------------SAVE PASSWORD-------------------------------
def add():
    web_entry = website_entry.get()
    pass_entry = password_entry.get()
    mail_entry = email_entry.get()
    if len(web_entry) == 0 or len(pass_entry) == 0:
        messagebox.showinfo(title="Empty fields", message="Please fill the empty fields")
    else:
        is_ok = messagebox.askokcancel(title=web_entry, message=f"Website: {web_entry}\n Password:{pass_entry} \n email:"
                                                        f"{mail_entry} \n is it OK to save ?")
        if is_ok:
            with open("mypass.txt", mode="a") as data:
                data.write(f"{web_entry} | {mail_entry} | {pass_entry} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


# --------------------------UI-------------------------------
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=20,pady=20)

# upload img to canvas
canvas = Canvas(width=200,height=200,highlightthickness=0)
tomato_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=tomato_img)
canvas.grid(column=1,row=0)

# Text on Column 1w
website = Label(text="Website:",font=("Helvetica", 16))
website.grid(column=0,row=1)

Email = Label(text="Email/Username:",font=("Helvetica", 16))
Email.grid(column=0,row=2)

password = Label(text="Password:",font=("Helvetica", 16))
password.grid(column=0,row=3)

# Text Entry
website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, "ahmed-abdirahman@outlook.com")

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)
# Buttons

generate_pass = Button(text="Generate Password",command=random_password)
generate_pass.grid(column=2,row=3)

add = Button(text="Add",width=36,command=add)
add.grid(column=1,row=4,columnspan=2)


window.mainloop()