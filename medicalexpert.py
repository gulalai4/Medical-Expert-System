import tkinter as tk
from tkinter import messagebox

class SecurityManager:
    def __init__(self):
        self.is_system_open = False
        self.password = "fiza"  # Replace with a strong password

    def open_system(self, entered_password):
        if entered_password == self.password:
            self.is_system_open = True
            return True
        else:
            return False

    def close_system(self):
        self.is_system_open = False

    def is_system_accessible(self):
        return self.is_system_open

class MedicalDiagnosisApp:
    def __init__(self, master, security_manager):
        self.master = master
        self.master.title("Medical Diagnosis Expert System")
        self.security_manager = security_manager
        self.user_name = ""

        # Dictionary to store symptom checkboxes
        self.symptoms = {
            'fever': tk.BooleanVar(),
            'runny_nose': tk.BooleanVar(),
            'cough': tk.BooleanVar(),
            'sore_throat': tk.BooleanVar(),
            'conjunctivitis': tk.BooleanVar(),
            'body_ache': tk.BooleanVar(),
            'headache': tk.BooleanVar(),
            'sneezing': tk.BooleanVar(),
            'rash': tk.BooleanVar(),
            'itching_skin': tk.BooleanVar(),
            'general_weakness': tk.BooleanVar(),
            'rose_colored_spot': tk.BooleanVar(),
            'swollen_salivary_glands': tk.BooleanVar(),
            'dry_mouth': tk.BooleanVar(),
            'vomiting': tk.BooleanVar(),
            'enlarged_lymph_nodes': tk.BooleanVar(),
            'slurred_speech': tk.BooleanVar(),
            'difficulty_breathing_or_swallowing': tk.BooleanVar(),
            'skin_lesion': tk.BooleanVar(),
            'myalgia': tk.BooleanVar(),
            'double_vision': tk.BooleanVar(),
            'chest_pain': tk.BooleanVar(),
            'paleness': tk.BooleanVar(),
            'low_blood_pressure': tk.BooleanVar(),
        }

        self.feedback_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Medical Diagnosis Expert System", font=("Helvetica", 16)).pack(pady=10)

        # Security-related widgets
        tk.Label(self.master, text="Enter Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack(pady=5)
        tk.Button(self.master, text="Open System", command=self.open_system).pack(pady=5)
        tk.Button(self.master, text="Close System", command=self.close_system).pack(pady=5)

        # Ask for user's name
        tk.Label(self.master, text="Enter Your Name:").pack(pady=5)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(pady=5)

        # Create symptoms input widgets
        self.create_input_widgets()

        # Diagnose button
        diagnose_button = tk.Button(self.master, text="Diagnose", command=self.diagnose)
        diagnose_button.pack(pady=10)

        # Diagnosis result label
        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 12), wraplength=400)
        self.result_label.pack(pady=10)

        # Feedback entry
        tk.Label(self.master, text="Provide Feedback:").pack(pady=5)
        feedback_entry = tk.Entry(self.master, textvariable=self.feedback_text)
        feedback_entry.pack(pady=5)

        # Submit Feedback button
        submit_feedback_button = tk.Button(self.master, text="Submit Feedback", command=self.submit_feedback)
        submit_feedback_button.pack(pady=10)

    def create_input_widgets(self):
        tk.Label(self.master, text="Please indicate your symptoms:").pack(pady=5)

        for symptom, var in self.symptoms.items():
            tk.Checkbutton(self.master, text=symptom.replace('_', ' ').title(), variable=var).pack(anchor='w', padx=10)

    def get_user_input(self):
        user_symptoms = {symptom: var.get() for symptom, var in self.symptoms.items()}
        return user_symptoms

    def open_system(self):
        password = self.password_entry.get()
        if self.security_manager.open_system(password):
            self.user_name = self.name_entry.get()
            messagebox.showinfo("System Opened", "Hello, {}! The system is now open.".format(self.user_name))
        else:
            messagebox.showerror("Access Denied", "Incorrect password. Access denied.")

    def close_system(self):
        self.security_manager.close_system()
        messagebox.showinfo("System Closed", "The system is now closed.")

    def diagnose(self):
        if not self.security_manager.is_system_accessible():
            messagebox.showerror("Access Denied", "The system is closed. Please open the system to proceed.")
            return

        user_symptoms = self.get_user_input()

        # Display diagnosis result
        diagnosis = self.diagnose_symptoms(user_symptoms)
        self.result_label.config(text=diagnosis)
        messagebox.showinfo("Diagnosis Result", diagnosis)

    def diagnose_symptoms(self, symptoms):
        # Symptom conditions for demonstration purposes
        if symptoms.get('fever', False) and symptoms.get('cough', False) and symptoms.get('sore_throat', False):
            return "Hello, {}! You may have a respiratory infection. Consult with a healthcare professional for further evaluation.".format(self.user_name)

        elif symptoms.get('fever', False) and symptoms.get('cough', False) and symptoms.get('conjunctivitis', False):
            return "Hello, {}! The symptoms may suggest a viral infection, possibly measles. Please see a doctor for a proper diagnosis and treatment.".format(self.user_name)

        elif symptoms.get('fever', False) and symptoms.get('cough', False) and symptoms.get('body_ache', False) and \
                symptoms.get('headache', False) and symptoms.get('runny_nose', False):
            return "Hello, {}! These symptoms are indicative of the flu. It is recommended to rest, stay hydrated, and take over-the-counter flu medication.".format(self.user_name)

        elif symptoms.get('runny_nose', False) and symptoms.get('cough', False) and symptoms.get('headache', False) and \
                symptoms.get('sore_throat', False):
            return "Hello, {}! You might be experiencing a common cold. Rest, drink fluids, and consider over-the-counter cold remedies.".format(self.user_name)

        elif symptoms.get('fever', False) and symptoms.get('swollen_salivary_glands', False) and symptoms.get('dry_mouth', False):
            return "Hello, {}! The symptoms may point to mumps. Seek medical attention for proper diagnosis and management.".format(self.user_name)

        elif symptoms.get('rash', False) and symptoms.get('itching_skin', False) and symptoms.get('general_weakness', False):
            return "Hello, {}! The presence of rash, itching, and general weakness could indicate chickenpox. Seek medical attention for appropriate care and isolation.".format(self.user_name)

        elif symptoms.get('cough', False) and symptoms.get('sneezing', False) and symptoms.get('runny_nose', False):
            return "Hello, {}! These symptoms are suggestive of whooping cough. Consult with a healthcare professional for proper diagnosis and treatment.".format(self.user_name)

        elif symptoms.get('fever', False) and symptoms.get('rash', False) and symptoms.get('body_ache', False) and \
                symptoms.get('vomiting', False) and symptoms.get('headache', False):
            return "Hello, {}! The symptoms may indicate meningitis. Urgent medical attention is required.".format(self.user_name)

        elif symptoms.get('fever', False) and symptoms.get('enlarged_lymph_nodes', False) and symptoms.get('slurred_speech', False) and \
                symptoms.get('difficulty_breathing_or_swallowing', False) and symptoms.get('skin_lesion', False):
            return "Hello, {}! These symptoms may suggest diphtheria. Seek immediate medical attention.".format(self.user_name)

        elif symptoms.get('fever', False) and symptoms.get('cough', False) and symptoms.get('headache', False) and symptoms.get('myalgia', False):
            return "Hello, {}! These symptoms are common in influenza (flu). Rest, stay hydrated, and consider over-the-counter flu medication.".format(self.user_name)

        elif symptoms.get('fever', False) and symptoms.get('rash', False) and symptoms.get('rose_colored_spot', False) and \
                symptoms.get('general_weakness', False) and symptoms.get('headache', False):
            return "Hello, {}! The symptoms may be consistent with typhoid fever. Urgent medical attention is required.".format(self.user_name)

        elif symptoms.get('chest_pain', False) and symptoms.get('paleness', False) and symptoms.get('low_blood_pressure', False) and \
                symptoms.get('general_weakness', False) and symptoms.get('difficulty_breathing_or_swallowing', False):
            return "Hello, {}! These symptoms could be indicative of anemia. Consult with a healthcare professional for further evaluation.".format(self.user_name)

        elif not any(symptoms.values()):
            return "Hello, {}! No symptoms provided. Please select at least one symptom for diagnosis.".format(self.user_name)

        else:
            return "Hello, {}! No specific diagnosis found based on provided symptoms. If symptoms persist or worsen, consult with a healthcare professional for a thorough evaluation.".format(self.user_name)

    def submit_feedback(self):
        feedback = self.feedback_text.get()
        if feedback:
            messagebox.showinfo("Feedback Submitted", "Thank you for your feedback, {}!".format(self.user_name))
        else:
            messagebox.showwarning("No Feedback", "Please provide feedback before submitting.")

def main():
    security_manager = SecurityManager()

    root = tk.Tk()
    app = MedicalDiagnosisApp(root, security_manager)
    root.mainloop()

if __name__ == "__main__":
    main()
