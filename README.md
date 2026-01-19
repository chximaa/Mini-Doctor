# 🩺 Simple Symptom-Based Disease Detection (Python)

This project is a **Python console application** that simulates a very<br>
basic **symptom-based medical assistant**.<br>
It asks the user about common symptoms and suggests the **most likely disease** <br>
along with **basic care or medicine**, based on predefined rules.

⚠️ **Disclaimer:** This project is for **educational purposes only** and **is<br>
not a real medical diagnosis tool**.

---

## 📌 Features

* Uses a predefined database of diseases
* Distinguishes between **major** and **minor** symptoms
* Interactive **yes/no symptom questionnaire**
* Weighted scoring system:

  * Major symptom → **2 points**
  * Minor symptom → **1 point**
* Suggests:

  * Most probable disease
  * Number of matched symptoms
  * Basic medication or care advice

---

## 🦠 Diseases Covered

* Flu
* Common Cold
* COVID-19
* Migraine
* Food Poisoning
* Allergy

Each disease includes:

* Major symptoms
* Minor symptoms
* Suggested medicine or care

---

## ⚙️ How It Works

1. The program collects **all unique symptoms** from the disease database.
2. The user is asked whether they experience each symptom (`y` or `n`).
3. A **score** is calculated for each disease:

   * Major symptom = 2 points
   * Minor symptom = 1 point
4. The disease with the **highest score and at least one major symptom** is selected.
5. Results are displayed with suggested care.

---

## ▶️ How to Run

### Requirements

* Python 3.x

### Run the program

```bash
python doctor.py
```

(Replace `doctor.py` with your file name if different.)

---

## 📤 Example Output

```
You are most likely to have: Flu

Matched symptoms:
- Major: 2
- Minor: 1

Suggested medicine / care:
- Paracetamol
- Ibuprofen
- Rest
- Fluids
```

---

## 🚨 Important Note

This program:

* ❌ Does NOT replace a doctor
* ❌ Should NOT be used for real medical decisions

If symptoms persist or worsen, **consult a healthcare professional**.

---

## 🎓 Educational Purpose

This project is useful for practicing:

* Python dictionaries
* Loops and conditionals
* User input handling
* Basic scoring logic
* Simple decision systems

---

