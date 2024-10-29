import csv
from faker import Faker

fake = Faker()
races = ["White", "Black or African American", "Asian", "American Indian", "Unknown", "Not Reported"]
genders = ["Male", "Female"]
statuses = ["Active", "Inactive"]
medications = ["Ibuprofen", "Paracetamol", "Amoxicillin", "Cetirizine", "Metformin", "Simvastatin"]
diseases = [ "Common Cold", "Flu", "Hypertension", "Diabetes", "Asthma", "Arthritis", "Migraine", "Pneumonia", "Bronchitis", "Sinusitis", "Strep Throat", "Anemia", "Gastroenteritis", "COVID-19", "Skin Rash", "Chronic Pain" ]
conditions = ["Allergies", "Anxiety", "COPD", "Epilepsy", "Heart Disease", "Kidney Disease", "Liver Disease",
                   "Mental Health Disorders", "Obesity", "Osteoporosis", "Parkinson's Disease", "Thyroid Disease"]

patientIds = []  # Store generated patient IDs
encounterIds = []  #Store generated encounter IDs
# Generate patient records
with open('patient.csv', 'w', newline='') as csvFile:
    fieldNames = ['patientId', 'firstName', 'lastName', 'dateOfBirth', 'race', 'gender',
                  'registerationDate', 'registerationStatus', 'email', 'address', 'createdDate']
    writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
    writer.writeheader()
    for _ in range(1000):
        patient_id = fake.unique.random_int(1, 10000)
        patientIds.append(patient_id)  # Save the patient ID
        writer.writerow({
            'patientId': patient_id,
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'dateOfBirth': fake.date_of_birth(),
            'race': fake.random_choices(races)[0],
            'gender': fake.random_choices(genders)[0],
            'registerationDate': fake.date(),
            'registerationStatus': fake.random_choices(statuses)[0],
            'email': fake.email(),
            'address': fake.address(),
            'createdDate': fake.date()
        })

# Generate encounter records using patient IDs
with open('encounter.csv', 'w', newline='') as csvFile:
    fieldNames = ['encounterId', 'patientId', 'encounterDate', 'reason','createdDate']
    writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
    writer.writeheader()
    for _ in range(500):
        encounterId = fake.unique.random_int(1, 10000)
        encounterIds.append(encounterId)  # Save the patient ID
        writer.writerow({
            'encounterId': encounterId,
            'patientId': fake.random_choices(patientIds)[0],  # Use a random patient ID
            'encounterDate': fake.date(),
            'reason': fake.random_choices(diseases),
            'createdDate': fake.date()
        })

# Generate condition records using patient IDs
with open('conditions.csv', 'w', newline='') as csvFile:
    fieldNames = ['conditionId', 'encounterId', 'condition', 'dateDiagnosed']
    writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
    writer.writeheader()
    for _ in range(1000):
        writer.writerow({
            'conditionId': fake.unique.random_int(1, 10000),
            'encounterId': fake.random_choices(encounterIds)[0],  # Use a random patient ID
            'condition': fake.random_choices(conditions),
            'dateDiagnosed': fake.date()
        })


# Generate medication records using patient IDs
with open('medications.csv', 'w', newline='') as csvFile:
    fieldNames = ['medicationId', 'patientId', 'medication', 'startDate', 'endDate']
    writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
    writer.writeheader()
    for _ in range(1000):
        writer.writerow({
            'medicationId': fake.unique.random_int(1, 10000),
            'patientId': fake.random_choices(patientIds)[0],  # Use a random patient ID
            'medication': fake.random_choices(medications),
            'startDate': fake.date(),
            'endDate': fake.date()
        })
