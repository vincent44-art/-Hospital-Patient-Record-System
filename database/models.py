from dataclasses import dataclass
from datetime import datetime

@dataclass
class Patient:
    patient_id: int = None
    first_name: str = ""
    last_name: str = ""
    date_of_birth: str = ""
    gender: str = ""
    address: str = ""
    phone: str = ""
    email: str = ""
    blood_type: str = ""
    insurance_info: str = ""
    emergency_contact: str = ""
    created_at: str = datetime.now().isoformat()

@dataclass
class Staff:
    staff_id: int = None
    first_name: str = ""
    last_name: str = ""
    role: str = ""
    department: str = ""
    specialization: str = ""
    license_number: str = ""
    contact_info: str = ""
    hire_date: str = datetime.now().isoformat()

@dataclass
class Appointment:
    appointment_id: int = None
    patient_id: int = 0
    staff_id: int = 0
    appointment_date: str = ""
    purpose: str = ""
    status: str = "Scheduled"
    notes: str = ""

@dataclass
class MedicalRecord:
    record_id: int = None
    patient_id: int = 0
    diagnosis: str = ""
    treatment: str = ""
    notes: str = ""
    record_date: str = datetime.now().isoformat()
    physician_id: int = 0