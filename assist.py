import pyttsx3
import speech_recognition as sr
import customtkinter
from termcolor import cprint
import numpy as np
from twilio.rest import Client
import datetime
import details
import csv
import time

twilo_sid = "AC67c15e1cfc3f36af2033da57cccdad30"
twilo_token = "6ae99edb8099acfcf1b5f35fd311295e"
csv_file_name = 'storage.csv'

#done
def listen():
    """to speak a output
    @paran -> none - outputs an source.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        cprint("Listening...",'red')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Sorry, there was an error with the speech recognition service."

#done
def speak(text):
    """to speak a output
    @paran -> audio - accepts a audio source.
    """
    cprint(f'system: {text}','light_cyan')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def wishMe():
    """to wish the user
    `@param` -> "none"
    """
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    # speak("welcome sir , I am your computer here to help you stay healthy.")       


#done
def take_data_ui():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root= customtkinter.CTk()
    root.geometry("500x350")

    def runner():
        name = entry1.get()
        age = entry2.get()
        weight = entry3.get()
        sex = entry4.get()
        data = [[name,age,weight,sex]]
        with open(csv_file_name, mode='w', newline='') as file:
            # fieldnames = ['name', 'age', 'weight', 'sex']  # Replace with your column names
            writer = csv.writer(file)

            for row in data:
                writer.writerow(row)
        root.destroy()

    frame= customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=30, fill="both", expand=True)

    label=customtkinter.CTkLabel(master=frame, text="Doctor AI",text_color="cyan",font=("Helvetica",24))
    label.pack(pady=20,padx=10)

    entry1=customtkinter.CTkEntry(master=frame,placeholder_text="Name")
    entry1.pack(pady=12,padx=10)

    entry2=customtkinter.CTkEntry(master=frame,placeholder_text="Age")
    entry2.pack(pady=12,padx=10)

    entry3=customtkinter.CTkEntry(master=frame,placeholder_text="Weight")
    entry3.pack(pady=12,padx=10)

    entry4=customtkinter.CTkEntry(master=frame,placeholder_text="Sex")
    entry4.pack(pady=12,padx=10)

    button=customtkinter.CTkButton(master=frame,text="Submit",command=runner)
    button.pack(pady=12,padx=10)
    
    
        

    root.mainloop()



#not my work
def symptom_checker(symptoms):
    diseases = {
        "fever": ["Common Cold", "Flu"],
        "cough": ["Common Cold", "Flu", "Bronchitis"],
        "headache": ["Migraine", "Tension Headache"],
        "fatigue": ["Mononucleosis", "Chronic Fatigue Syndrome"],
        "nausea": ["Food Poisoning", "Stomach Flu"],
        "influenza(flu)":["high fever","muscle","aches","sore throat","fatigue","cough"],
        "Diabetes":["frequent urination","excessive thrist","weight loss","fatigue"],
        "Asthma":["Shortness of Breath","wheezing","coughnung","chest tightness"],
        "Arthritis":["Joint paim","stiffness","swelling"],
        "heartattack":["chest pain"]
    }

    matched_diseases = []

    for symptom in symptoms:
        if symptom in diseases:
            matched_diseases.extend(diseases[symptom])

    matched_diseases = list(set(matched_diseases))  # Remove duplicates

    if not matched_diseases:
        return "No specific diseases found based on the provided symptoms."
    else:
        return "Possible diseases related to the symptoms: " + ", ".join(matched_diseases)


def diagnoser(user_input):
    print("Welcome to the Symptom Checker.")
    
    user_symptoms = [symptom.strip().lower() for symptom in user_input.split(" ")]
    
    result = symptom_checker(user_symptoms)
    print("Diagnosis Result:", result)
    
    # Speak the diagnosis result
    speak("Diagnosis Result: " + result)

def report():
    print("report")

def caller():
    call = Client.calls.create(
    url="http://demo.twilio.com/docs/voice.xml",
    to="+918837097517",
    from_=""
    )

    print(call.sid)

def take_data():
    speak("Please enter your details.")
    take_data_ui()

def show_details():
    speak ("Place your thumb into the sensor")
    time.sleep(5)
    speak("processing....")
    time.sleep(5)
    details.blood_pressure()
    details.pulse()
    details.temperature()
    



if __name__ == "__main__":
    wishMe()
    speak("I am an AI deveoped to help people in the medical field . I can help you with finding solutions to your health problems.")
    speak('Note -  this AI is made only for educational purposes and its data is not accurate and can give missleading information.')
    speak('this is made for the soul purpose to demonstrate the usefulness and uses of such a AI solution.')
    take_data()
    show_details()
    speak("please say your problems.")
    while True:
        query = listen().lower()
        
        if "hello" in query:
            speak('hello, how are you.')
        elif "help" in query:
            speak("please let me know what problems are you having.")
            problems = listen().lower()
            diagnoser(problems)
        elif "stop" in query:
            speak("Ok , powering off.")
            break