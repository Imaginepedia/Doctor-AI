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
    # print("Diagnosis Result: " + result)

diagnoser("heartattack")