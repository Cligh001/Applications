from tkinter import *
from random import randint, choice, shuffle
from tkinter import messagebox
import pyperclip
import json

BACKGROUND = "#FDFDE2"
FONT_NAME = "Courier"
FONT_COLOUR = "#96B9D0"
FONT_SIZE = 12

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    pw_entry.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    
    generate_letter = [choice(letters) for _ in range(randint(8,10))]
    generate_number = [choice(numbers) for _ in range(randint(2,4))]
    generate_symbol = [choice(symbols) for _ in range(randint(2,4))]

    password_list = generate_letter + generate_number + generate_symbol #add all randomly generated characters
    shuffle(password_list) #shuffles list
    password_final = ''.join(password_list) #joins shuffled list of characters

    pw_entry.insert(0, password_final) #places into entry insert
    pyperclip.copy(password_final)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    ws_text = ws_entry.get() #appends into file
    email_user_text = email_user_entry.get() #grabs entry input
    pw_text = pw_entry.get() #grabs password input
    new_data = {
        ws_text: {
        "email": email_user_text,
        "password": pw_text,
    }
        }
    
    #field is missing
    if len(ws_text) == 0 or len(pw_text) == 0 or len(email_user_text) == 0:
        messagebox.showinfo(title="ALERT!", message="Do not leave empty fields.")
    else:
        try:
            with open("saver_doc.json", "r") as saver: #opens up file as append
                #read exisiting data
                existing_data = json.load(saver)
                
        except FileNotFoundError: #code executes if file is not present
            with open("saver_doc.json", "w") as saver:
                json.dump(new_data, saver, indent=4)
        else: #only executes if try block went through
            #update exisiting data with new data
            existing_data.update(new_data)
                
            with open("saver_doc.json", "w") as saver:
                #saving updated data
                json.dump(existing_data, saver, indent=4)
        finally:
            #clear all entries
            ws_entry.delete(0, END)
            pw_entry.delete(0, END)
# ---------------------------- SEARCH ------------------------------- #
def search_data():
    searched_website = ws_entry.get()
    try:
        with open("saver_doc.json", "r") as saver:
            all_data = json.load(saver)
            website_data = all_data[searched_website]
    except KeyError:
        messagebox.showinfo(title="Alert!", message="That website has no saved information! \n Make sure spelling is correct. \n Remember: Entries are case sensitive.")
    except FileNotFoundError:
        messagebox.showinfo(title="Alert!", message="Data File Does NOT Exist! \n Try adding an entry first.")
    else:
        email_user_data = website_data['email']
        pw_data = website_data['password']
        messagebox.showinfo(title="", message="Password/Email Information", detail=f'Email: {email_user_data}\n Password: {pw_data}')

# ---------------------------- UI SETUP ------------------------------- #

#window
wn = Tk()
wn.title("Password Manager")
wn.config(padx=50,pady=50,bg=BACKGROUND)

#lock image
canv = Canvas(width=200,height=200,bg=BACKGROUND,highlightthickness=0)
lock_img = PhotoImage(file="Saver/pink_lock_logo.png")
canv.create_image(100,100,image=lock_img)
canv.grid(row=0, column=1)

#all labels
my_pass = Label(text="MY PASS")
my_pass.grid(row=1, column=1)
my_pass.config(fg = "#FF99D7", background= BACKGROUND, font=("Courier", 40, "bold"))

ws_label = Label(text="Website:") #website label
ws_label.grid(row=2,column=0)
ws_label.config(fg = FONT_COLOUR, background=BACKGROUND)

email_user_label = Label(text="Email/Username:") #email and username label
email_user_label.grid(row=3,column=0)
email_user_label.config(fg = FONT_COLOUR, background=BACKGROUND)

pw_label = Label(text="Password:") #password label
pw_label.grid(row=4,column=0)
pw_label.config(fg = FONT_COLOUR, background=BACKGROUND)

#all entries
ws_entry = Entry(width=21) #website entry
ws_entry.grid(row=2, column=1, sticky= "EW")
ws_entry.focus()
ws_entry.config(fg = FONT_COLOUR, highlightbackground=BACKGROUND, highlightthickness=0)

email_user_entry = Entry(width=35) #email/username entry
email_user_entry.grid(row=3, column=1, columnspan=2, sticky="EW")
email_user_entry.insert(0, "c.m.light001@gmail.com")
email_user_entry.config(fg = FONT_COLOUR, highlightbackground=BACKGROUND, highlightthickness=0)

pw_entry = Entry(width=21) #password entry
pw_entry.grid(row=4,column=1, sticky="EW")
pw_entry.config(fg = FONT_COLOUR, highlightbackground=BACKGROUND, highlightthickness=0)

#all buttons
pw_gen_button = Button(fg= FONT_COLOUR, text="Generate Password", command=generate) #generate password button
pw_gen_button.grid(row=4,column=2, sticky="EW")
pw_gen_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

add_button = Button(fg= FONT_COLOUR, text="Add", width=36, command=save_info) #add button
add_button.grid(row=5,column=1, columnspan=2, sticky="EW")
add_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

search_button = Button(fg= FONT_COLOUR, text="Search", command=search_data) #search button
search_button.grid(row=2, column=2, sticky="EW")
search_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

wn.mainloop()
