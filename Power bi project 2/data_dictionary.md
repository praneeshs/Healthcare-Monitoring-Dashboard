# Data Dictionary - Healthcare Monitoring Dataset

| Field Name       | Data Type | Description                                                              |
|------------------|-----------|--------------------------------------------------------------------------|
| PatientID        | String    | Unique identifier for each patient encounter (e.g., P0001)               |
| PatientName      | String    | Full name of the patient                                                 |
| Gender           | String    | Biological sex (Male / Female)                                           |
| Age              | Integer   | Age of patient in years                                                  |
| AdmissionDate    | Date      | Date of admission (YYYY-MM-DD)                                           |
| AdmissionTime    | Time      | Time of admission (HH:MM, 24-hour format)                                |
| DischargeDate    | Date      | Date of discharge, blank if still admitted                               |
| Department       | String    | Clinical department handling the patient (e.g., Surgery, ICU)            |
| Ward             | String    | Ward location (e.g., Ward A, ICU)                                        |
| BedNumber        | String    | Bed identifier in the ward (format: Ward-X-##)                           |
| DoctorAssigned   | String    | Primary attending physician                                              |
| DoctorRating     | Decimal   | Patient feedback rating for doctor (1.0 – 5.0)                           |
| TreatmentStatus  | String    | Current treatment status (Admitted, Critical, Stable, Recovering, etc.)  |
| TreatmentDays    | Integer   | Length of stay in days                                                   |
| ICUFlag          | Integer   | 1 if patient is/was in ICU, else 0                                       |
| EmergencyFlag    | Integer   | 1 if admission classified as emergency, else 0                           |
| HeartRate        | Integer   | Latest recorded heart rate (beats per minute)                            |
| SystolicBP       | Integer   | Latest systolic blood pressure (mmHg)                                    |
| DiastolicBP      | Integer   | Latest diastolic blood pressure (mmHg)                                   |
| SpO2             | Integer   | Peripheral oxygen saturation (%)                                         |
| Temperature      | Decimal   | Body temperature (°F)                                                    |
| Insurance        | String    | Insurance type (Private, Medicare, Medicaid, Uninsured, Corporate)       |
