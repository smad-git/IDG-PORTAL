import json
import psycopg2
import csv
import boto3
from io import StringIO

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Database connection details
    db_host = 'your-db-host'
    db_name = 'your-db-name'
    db_user = 'your-db-user'
    db_password = 'your-db-password'
    db_port = 5432

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=db_port
    )
    cursor = conn.cursor()
    
    # Define your S3 bucket and files
    bucket_name = 'your-bucket-name'
    files = ['patient.csv', 'conditions.csv', 'medications.csv', 'encounter.csv']
    
    for file in files:
        response = s3.get_object(Bucket=bucket_name, Key=file)
        file_content = response['Body'].read().decode('utf-8')
        csv_reader = csv.reader(StringIO(file_content))

        # Skip the header
        next(csv_reader)
        
        for row in csv_reader:
            if file == 'patient.csv':
                cursor.execute("INSERT INTO patient (patientId, firstName, lastName, dateOfBirth, race, gender, registerationDate, registerationStatus, email, address, createdDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
            elif file == 'conditions.csv':
                cursor.execute("INSERT INTO conditions (conditionId, patientId, condition, dateDiagnosed) VALUES (%s, %s, %s, %s)", row)
            elif file == 'medications.csv':
                cursor.execute("INSERT INTO medications (medicationId, patientId, medication, startDate, endDate, dosage) VALUES (%s, %s, %s, %s, %s, %s)", row)
            elif file == 'encounter.csv':
                cursor.execute("INSERT INTO encounter (encounterId, patientId, date, type, description) VALUES (%s, %s, %s, %s, %s)", row)
    
    # Commit and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted successfully!')
    }
