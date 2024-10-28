import csv
from faker import Faker

fake = Faker()

races = ["White", "Black or African American", "Asian","American Indian", "Unknown","Not Reported"]

genders = ["Male", "Female"]

statuses = ["Active", "Inactive"]
with open('patient.csv','w', newline='') as csvFile:
    fieldNames = ['patientId', 'firstName','lastName','dateOfBirth', 'race','gender','registerationDate','registerationStatus','createdDate']
    writer = csv.DictWriter(csvFile,fieldnames=fieldNames)

    writer.writeheader()
    for _ in range(1000):
        writer.writerow({
            'patientId': fake.unique.random_int(1,10000),
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'dateOfBirth': fake.date_of_birth(),
            'race': fake.random_choices(races),
            'gender': fake.random_choices(genders),
            'registerationDate': fake.date(),
            'registerationStatus': fake.random_choices(statuses),
            'createdDate': fake.date()
        })
