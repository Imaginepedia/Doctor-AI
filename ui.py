import customtkinter
import numpy as np

def runnr():
    name=entry1.get()
    age=entry2.get()
    weight=entry3.get()
    sex=entry4.get()
    result = np.array([name,age,weight,sex])
    return result

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root= customtkinter.CTk()
root.geometry("500x350")


frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=30, fill="both", expand=True)

label=customtkinter.CTkLabel(master=frame, text="Dr. AI")
label.pack(pady=12,padx=10)

entry1=customtkinter.CTkEntry(master=frame,placeholder_text="Name")
entry1.pack(pady=12,padx=10)

entry2=customtkinter.CTkEntry(master=frame,placeholder_text="Age")
entry2.pack(pady=12,padx=10)

entry3=customtkinter.CTkEntry(master=frame,placeholder_text="Weight")
entry3.pack(pady=12,padx=10)

entry4=customtkinter.CTkEntry(master=frame,placeholder_text="Sex")
entry4.pack(pady=12,padx=10)

button=customtkinter.CTkButton(master=frame,text="Submit",command=runnr)
button.pack(pady=12,padx=10)

root.mainloop()
