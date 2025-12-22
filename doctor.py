diseases = {
    "Flu": {
        "major": ["fever", "chills", "fatigue"],
        "minor": ["cough", "headache", "sore throat"],
        "medicine": ["Paracetamol", "Ibuprofen", "Rest", "Fluids"]
    },
    "Common Cold": {
        "major": ["runny nose", "sneezing"],
        "minor": ["cough", "sore throat", "fatigue"],
        "medicine": ["Paracetamol", "Antihistamines", "Warm fluids"]
    },
    "COVID-19": {
        "major": ["fever", "loss of taste", "loss of smell"],
        "minor": ["cough", "fatigue", "headache"],
        "medicine": ["Paracetamol", "Rest", "Isolation", "Fluids"]
    },
    "Migraine": {
        "major": ["headache", "sensitivity to light"],
        "minor": ["nausea", "vomiting"],
        "medicine": ["Ibuprofen", "Triptans", "Dark room rest"]
    },
    "Food Poisoning": {
        "major": ["vomiting", "diarrhea"],
        "minor": ["nausea", "stomach pain", "fever"],
        "medicine": ["Oral rehydration salts", "Rest", "Light food"]
    },
    "Allergy": {
        "major": ["sneezing", "itchy eyes"],
        "minor": ["runny nose", "cough"],
        "medicine": ["Antihistamines", "Avoid allergens"]
    }
}

# Collect all unique symptoms
user_symptoms = {}
all_symptoms = set()

for disease in diseases.values():
    all_symptoms.update(disease["major"])
    all_symptoms.update(disease["minor"])

print("Welcome to your personal doctor\nAnswer with y or n:\n")

for symptom in sorted(all_symptoms):
    answer = input(f"Do you have {symptom}? (y/n): ").lower()
    user_symptoms[symptom] = (answer == "y")

# Score diseases
scores = {}

for disease, data in diseases.items():
    score = 0
    major_count = 0
    minor_count = 0

    for symptom in data["major"]:
        if user_symptoms.get(symptom):
            score += 2
            major_count += 1

    for symptom in data["minor"]:
        if user_symptoms.get(symptom):
            score += 1
            minor_count += 1

    scores[disease] = {
        "score": score,
        "major": major_count,
        "minor": minor_count,
        "medicine": data["medicine"]
    }

# Find best disease (must have at least 1 major symptom)
best_disease = None
best_score = 0

for disease, info in scores.items():
    if info["score"] > best_score and info["major"] > 0:
        best_score = info["score"]
        best_disease = disease

# Display result
print("\n----------------------------------\n")

if best_disease:
    info = scores[best_disease]
    print(f"You are most likely to have: **{best_disease}**\n")
    print(f"Matched symptoms:")
    print(f"- Major: {info['major']}")
    print(f"- Minor: {info['minor']}\n")

    print("Suggested medicine / care:")
    for med in info["medicine"]:
        print(f"- {med}")

    print("\n⚠️ Please note:")
    print(
        "This is not a professional medical consultation.\n"
        "If your symptoms worsen or persist, please visit a professional doctor."
    )
else:
    print("No disease could be confidently identified.")
    print(
        "If you feel unwell, please consult a professional doctor."
    )
