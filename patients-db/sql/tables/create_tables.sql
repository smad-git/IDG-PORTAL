-- patients table
CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address TEXT,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--encounters table
CREATE TABLE IF NOT EXISTS encounters (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    encounter_date TIMESTAMP NOT NULL,
    reason VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE
);

--conditions table
CREATE TABLE IF NOT EXISTS conditions (
    id SERIAL PRIMARY KEY,
    encounter_id INT NOT NULL,
    condition_code VARCHAR(50),
    description TEXT,
    diagnosed_at TIMESTAMP NOT NULL,
    FOREIGN KEY (encounter_id) REFERENCES encounters(id) ON DELETE CASCADE
);

--medications table
CREATE TABLE IF NOT EXISTS medications (
    id SERIAL PRIMARY KEY,
    encounter_id INT NOT NULL,
    medication_name VARCHAR(255),
    dosage VARCHAR(50),
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    FOREIGN KEY (encounter_id) REFERENCES encounters(id) ON DELETE CASCADE
);

-- conditions_medications table 
CREATE TABLE IF NOT EXISTS conditions_medications (
    condition_id INT NOT NULL,
    medication_id INT NOT NULL,
    PRIMARY KEY (condition_id, medication_id),
    FOREIGN KEY (condition_id) REFERENCES conditions(id) ON DELETE CASCADE,
    FOREIGN KEY (medication_id) REFERENCES medications(id) ON DELETE CASCADE
);
