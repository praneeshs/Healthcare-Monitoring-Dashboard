import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import json

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate comprehensive healthcare dataset
def generate_healthcare_data():
    # Base parameters
    n_patients = 1200
    
    # Patient demographics
    patient_ids = [f"P{str(i).zfill(4)}" for i in range(1, n_patients + 1)]
    
    # Names (mix of common names)
    first_names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 
                   'David', 'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica',
                   'Thomas', 'Sarah', 'Christopher', 'Karen', 'Charles', 'Nancy', 'Daniel', 'Lisa',
                   'Matthew', 'Betty', 'Anthony', 'Helen', 'Mark', 'Sandra', 'Donald', 'Donna',
                   'Steven', 'Carol', 'Paul', 'Ruth', 'Joshua', 'Sharon', 'Kenneth', 'Michelle']
    
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
                  'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzales', 'Wilson', 'Anderson',
                  'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson',
                  'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson']
    
    # Departments and wards
    departments = ['Emergency', 'Surgery', 'Cardiology', 'Neurology', 'Orthopedics', 
                   'Pediatrics', 'ICU', 'General Medicine', 'Oncology', 'Maternity']
    
    wards = ['Ward A', 'Ward B', 'Ward C', 'Ward D', 'ICU', 'Emergency', 'Surgery Wing', 'Pediatric']
    
    # Doctors
    doctors = ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams', 'Dr. Brown', 'Dr. Jones', 
               'Dr. Garcia', 'Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez', 'Dr. Martinez',
               'Dr. Hernandez', 'Dr. Lopez', 'Dr. Wilson', 'Dr. Anderson', 'Dr. Thomas']
    
    # Treatment status options
    treatment_status = ['Admitted', 'Critical', 'Stable', 'Recovering', 'Discharged', 'Under Observation']
    
    # Generate data
    data = []
    
    for i in range(n_patients):
        # Basic patient info
        patient_id = patient_ids[i]
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        gender = random.choice(['Male', 'Female'])
        age = np.random.normal(45, 20)  # Normal distribution around 45
        age = max(1, min(95, int(age)))  # Clamp between 1-95
        
        # Department assignment - pediatrics for under 18
        if age < 18:
            department = 'Pediatrics'
            ward = 'Pediatric'
        else:
            department = random.choice(departments)
            ward = random.choice(wards)
        
        # Admission date - spread across 2024
        start_date = datetime(2024, 1, 1)
        admission_date = start_date + timedelta(days=random.randint(0, 364))
        admission_time = admission_date.replace(
            hour=random.randint(0, 23), 
            minute=random.randint(0, 59)
        )
        
        # Treatment duration and discharge
        treatment_days = np.random.exponential(7)  # Exponential distribution
        treatment_days = max(1, min(365, int(treatment_days)))
        
        # Some patients still admitted (30%)
        still_admitted = random.random() < 0.3
        if still_admitted:
            discharge_date = None
            status = random.choice(['Admitted', 'Critical', 'Stable', 'Recovering', 'Under Observation'])
        else:
            discharge_date = admission_date + timedelta(days=treatment_days)
            status = 'Discharged'
        
        # ICU and Emergency flags
        icu_flag = 1 if department == 'ICU' or random.random() < 0.12 else 0
        emergency_flag = 1 if department == 'Emergency' or random.random() < 0.25 else 0
        
        # Patient vitals - vary based on condition
        if icu_flag or status == 'Critical':
            # ICU patients have more extreme vitals
            heart_rate = np.random.normal(85, 25)
            heart_rate = max(40, min(150, int(heart_rate)))
            
            systolic_bp = np.random.normal(130, 20)
            systolic_bp = max(80, min(200, int(systolic_bp)))
            
            diastolic_bp = np.random.normal(80, 15)
            diastolic_bp = max(50, min(120, int(diastolic_bp)))
            
            spo2 = np.random.normal(94, 4)
            spo2 = max(85, min(100, int(spo2)))
            
            temperature = np.random.normal(99.2, 1.5)
            temperature = max(96, min(104, round(temperature, 1)))
        else:
            # Normal patients
            heart_rate = np.random.normal(72, 12)
            heart_rate = max(50, min(120, int(heart_rate)))
            
            systolic_bp = np.random.normal(120, 15)
            systolic_bp = max(90, min(160, int(systolic_bp)))
            
            diastolic_bp = np.random.normal(80, 10)
            diastolic_bp = max(60, min(100, int(diastolic_bp)))
            
            spo2 = np.random.normal(98, 2)
            spo2 = max(95, min(100, int(spo2)))
            
            temperature = np.random.normal(98.6, 0.8)
            temperature = max(97, min(101, round(temperature, 1)))
        
        # Doctor assignment
        doctor = random.choice(doctors)
        
        # Doctor rating (1-5 scale)
        doctor_rating = round(np.random.normal(4.2, 0.6), 1)
        doctor_rating = max(1.0, min(5.0, doctor_rating))
        
        # Bed number
        bed_number = f"{ward}-{random.randint(1, 50)}"
        
        # Insurance type
        insurance = random.choice(['Private', 'Medicare', 'Medicaid', 'Uninsured', 'Corporate'])
        
        # Create record
        record = {
            'PatientID': patient_id,
            'PatientName': name,
            'Gender': gender,
            'Age': age,
            'AdmissionDate': admission_date.strftime('%Y-%m-%d'),
            'AdmissionTime': admission_time.strftime('%H:%M'),
            'DischargeDate': discharge_date.strftime('%Y-%m-%d') if discharge_date else None,
            'Department': department,
            'Ward': ward,
            'BedNumber': bed_number,
            'DoctorAssigned': doctor,
            'DoctorRating': doctor_rating,
            'TreatmentStatus': status,
            'TreatmentDays': treatment_days if not still_admitted else (datetime.now() - admission_date).days,
            'ICUFlag': icu_flag,
            'EmergencyFlag': emergency_flag,
            'HeartRate': heart_rate,
            'SystolicBP': systolic_bp,
            'DiastolicBP': diastolic_bp,
            'SpO2': spo2,
            'Temperature': temperature,
            'Insurance': insurance
        }
        
        data.append(record)
    
    return pd.DataFrame(data)

# Generate the dataset
print("Generating healthcare dataset...")
df = generate_healthcare_data()

# Display basic statistics
print(f"\nDataset created with {len(df)} patient records")
print(f"Date range: {df['AdmissionDate'].min()} to {df['AdmissionDate'].max()}")
print(f"Departments: {df['Department'].value_counts().to_dict()}")
print(f"ICU patients: {df['ICUFlag'].sum()}")
print(f"Emergency cases: {df['EmergencyFlag'].sum()}")
print(f"Still admitted: {df['DischargeDate'].isna().sum()}")

# Save the dataset
df.to_csv('healthcare_data.csv', index=False)
print("\nDataset saved as 'healthcare_data.csv'")

# Display first few rows
print("\nFirst 5 records:")
print(df.head())