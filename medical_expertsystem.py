#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ExpertSystem:
    def __init__(self):
        self.symptoms = {
            'fever': False,
            'cough': False,
            'rash': False,
            'sore throat': False,
            'runny nose': False,
            'diarrhea': False,
            'vomiting': False,
            'fatigue': False,
            'itchiness': False,
            'ear pain': False,
            'body aches': False,
            'swollen glands': False,
            'abdominal pain': False,
            'sneezing': False,
            'itchy eyes': False,
            'excessive thirst': False,
            'frequent urination': False,
            'dehydration': False,
            'unexplained weight loss': False,
        }
        self.diseases = {
            'Common Cold': ['fever', 'cough', 'runny nose', 'sore throat', 'fatigue'],
            'Flu': ['fever', 'cough', 'fatigue', 'body aches'],
            'Chickenpox': ['fever', 'rash', 'itchiness', 'fatigue'],
            'Strep Throat': ['sore throat', 'fever', 'swollen glands'],
            'Gastroenteritis': ['vomiting', 'diarrhea', 'abdominal pain'],
            'Asthma': ['cough', 'wheezing', 'difficulty breathing'],
            'Ear Infection': ['ear pain', 'fever', 'difficulty sleeping'],
            'Allergies': ['runny nose', 'sneezing', 'itchy eyes', 'itchiness'],
            'Measles': ['high fever', 'cough', 'rash', 'sore throat'],
            'Hand, Foot, and Mouth Disease': ['fever', 'sore throat', 'rash', 'blisters'],
            'Diabetes': ['excessive thirst', 'frequent urination', 'fatigue', 'unexplained weight loss'],
            'Paranasal Sinusitis': ['facial pain', 'headache', 'nasal congestion', 'cough'],
            'Diarrheal Diseases': ['abdominal pain', 'diarrhea', 'vomiting', 'dehydration']
        }

        self.treatments = {
   
    'Common Cold': {
        'description': 'The common cold is a viral infection of the upper respiratory tract. It is characterized by symptoms such as sneezing, nasal congestion, sore throat, and mild fever.',
        'treatment': 'Get plenty of rest, stay hydrated, and take over-the-counter cold medication such as decongestants, antihistamines, and pain relievers. Gargling with warm salt water may also help relieve a sore throat.'
    },
    'Flu': {
        'description': 'Influenza, commonly known as the flu, is a highly contagious viral infection that affects the respiratory system. Symptoms often include high fever, muscle aches, headache, fatigue, and cough.',
        'treatment': 'Rest, drink plenty of fluids, and take antiviral medication if prescribed by a doctor. Over-the-counter medications such as pain relievers, decongestants, and cough suppressants can help alleviate symptoms. In severe cases, hospitalization may be necessary.'
    },
    'Chickenpox': {
        'description': 'Chickenpox is a highly contagious viral infection characterized by an itchy rash, fever, and fatigue. It is caused by the varicella-zoster virus.',
        'treatment': 'Apply calamine lotion to relieve itching, take oatmeal baths to soothe the skin, and avoid scratching the rash to prevent scarring. Over-the-counter pain relievers such as acetaminophen or ibuprofen can help reduce fever and discomfort.'
    },
    'Strep Throat': {
        'description': 'Strep throat is a bacterial infection that causes inflammation and soreness of the throat, often accompanied by fever and swollen lymph nodes in the neck.',
        'treatment': 'Take antibiotics as prescribed by a doctor to treat the bacterial infection. Rest, drink plenty of fluids, and use over-the-counter pain relievers such as acetaminophen or ibuprofen to alleviate symptoms.'
    },
    'Gastroenteritis': {
        'description': 'Gastroenteritis, commonly known as stomach flu, is an inflammation of the stomach and intestines caused by viral or bacterial infection. Symptoms include diarrhea, vomiting, stomach cramps, and fever.',
        'treatment': 'Stay hydrated with electrolyte solutions, eat bland foods like rice and toast, and rest. Seek medical attention if symptoms worsen or persist. In severe cases, hospitalization may be necessary.'
    },
    'Asthma': {
        'description': 'Asthma is a chronic respiratory condition characterized by inflammation and narrowing of the airways, leading to wheezing, shortness of breath, chest tightness, and coughing.',
        'treatment': 'Use inhalers as prescribed to control symptoms and prevent asthma attacks. Avoid triggers such as allergens and irritants, and seek medical help if symptoms worsen despite treatment.'
    },
    'Ear Infection': {
        'description': 'An ear infection, or otitis media, is an inflammation of the middle ear often caused by bacterial or viral infection. Symptoms include ear pain, fever, and sometimes hearing loss.',
        'treatment': 'Take antibiotics as prescribed by a doctor to treat the bacterial infection. Apply warm compresses to the ear to relieve pain, and use over-the-counter pain relievers such as acetaminophen or ibuprofen.'
    },
    'Allergies': {
        'description': 'Allergies occur when the immune system reacts abnormally to substances that are usually harmless, such as pollen, dust mites, pet dander, or certain foods. Symptoms vary depending on the allergen but commonly include sneezing, runny nose, itchy eyes, and rash.',
        'treatment': 'Avoid allergens whenever possible. Take antihistamines to relieve symptoms, and use nasal sprays as prescribed. In severe cases, allergy shots (immunotherapy) may be recommended.'
    },
    'Measles': {
        'description': 'Measles is a highly contagious viral infection characterized by high fever, cough, runny nose, rash, and red, watery eyes. Complications can include pneumonia, encephalitis, and death.',
        'treatment': 'Rest, stay hydrated, and take fever-reducing medication. Seek medical attention if complications such as pneumonia or encephalitis arise. Vaccination with the measles, mumps, and rubella (MMR) vaccine can prevent measles.'
    },
    'Hand, Foot, and Mouth Disease': {
        'description': 'Hand, foot, and mouth disease is a viral infection common in children under 5 years old. It is characterized by fever, sore throat, rash, and blisters on the hands, feet, and mouth.',
        'treatment': 'Rest, stay hydrated, and use over-the-counter pain relievers to reduce fever and discomfort. Avoid close contact with others to prevent spread. Symptoms usually resolve on their own within a week.'
    },
    'Diabetes': {
        'description': 'Diabetes is a chronic condition characterized by high blood sugar levels due to insufficient production of insulin (Type 1 diabetes) or the body\'s inability to use insulin effectively (Type 2 diabetes). Symptoms of high blood sugar include frequent urination, increased thirst, and unexplained weight loss.',
        'treatment': 'Monitor blood sugar levels regularly, adhere to a balanced diet, take insulin or oral medications as prescribed, exercise regularly, and maintain a healthy lifestyle. Regular medical check-ups are essential for proper management of diabetes.'
    },
    'Paranasal Sinusitis': {
        'description': 'Paranasal sinusitis, or sinus infection, is an inflammation of the paranasal sinuses caused by viral, bacterial, or fungal infection. Symptoms include facial pain, nasal congestion, headache, and postnasal drip.',
        'treatment': 'Use saline nasal sprays to help clear nasal passages, apply warm compresses to relieve facial pain, take over-the-counter pain relievers such as acetaminophen or ibuprofen, and stay hydrated. In some cases, antibiotics may be prescribed for bacterial sinusitis.'
    },
    'Diarrheal Diseases': {
        'description': 'Diarrheal diseases are gastrointestinal infections that cause frequent loose stools, abdominal cramps, and sometimes vomiting and fever. They can be caused by viruses, bacteria, or parasites.',
        'treatment': 'Stay hydrated with clear fluids such as water, broth, or oral rehydration solutions to replace lost fluids and electrolytes. Eat bland foods like bananas, rice, and toast, and avoid dairy and fatty foods. Seek medical attention if symptoms persist or worsen.'
    },
    # Add more diseases if needed...
}

    def get_symptoms(self):
        print("Please answer with yes or no.")
        for symptom in self.symptoms.keys():
            response = input(f"Do you have {symptom}? ")
            if response == 'yes':
                self.symptoms[symptom] = True

    def diagnose_disease(self):
        max_shared_symptoms = 0
        likely_disease = None
        
        for disease, disease_symptoms in self.diseases.items():
            shared_symptoms = sum(self.symptoms[symptom] for symptom in disease_symptoms if symptom in self.symptoms)
            if shared_symptoms > max_shared_symptoms:
                max_shared_symptoms = shared_symptoms
                likely_disease = disease

        if likely_disease:
            print(f"The most likely disease based on symptoms is: {likely_disease}.")
            self.recommend_treatment(likely_disease)
        else:
            print("No matching disease found based on the symptoms provided.")

    def recommend_treatment(self, disease):
        if disease in self.treatments:
            print("Recommended treatment:")
            print(self.treatments[disease])
        else:
            print("Treatment recommendations not available for this disease.")

    def run(self):
        self.get_symptoms()
        self.diagnose_disease()


if __name__ == "__main__":
    expert_system = ExpertSystem()
    expert_system.run()


# In[ ]:




