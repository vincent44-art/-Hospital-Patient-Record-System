from database.db import create_connection, initialize_database
from patients.patient_ops import add_patient, get_all_patients, get_patient_by_id, update_patient, delete_patient, search_patients
from staff.staff_ops import add_staff, get_all_staff, get_staff_by_id, update_staff, delete_staff, get_staff_by_role
from appointments.appointment_ops import add_appointment, get_all_appointments, get_appointments_by_patient
from database.models import Patient, Staff, Appointment
import os
from datetime import datetime, timedelta

def setup_database():
    """Initialize the database and create tables"""
    db_path = "data/hospital.db"
    os.makedirs("data", exist_ok=True)
    
    conn = create_connection(db_path)
    if conn:
        initialize_database(conn)
        conn.close()
        print("Database initialized successfully")
    else:
        print("Failed to initialize database")

def demo_patient_operations():
    """Demonstrate patient operations"""
    print("\n=== Patient Operations Demo ===")
    
    # Add a new patient
    new_patient = Patient(
        first_name="John",
        last_name="Doe",
        date_of_birth="1985-05-15",
        gender="Male",
        address="123 Main St",
        phone="555-1234",
        email="john.doe@example.com",
        blood_type="O+",
        insurance_info="Blue Cross",
        emergency_contact="Jane Doe (555-5678)"
    )
    patient_id = add_patient(new_patient)
    print(f"Added patient with ID: {patient_id}")
    
    # Get all patients
    patients = get_all_patients()
    print("\nAll Patients:")
    for patient in patients:
        print(f"{patient.patient_id}: {patient.first_name} {patient.last_name}")
    
    # Get patient by ID
    if patients:
        patient = get_patient_by_id(patients[0].patient_id)
        print(f"\nPatient details: {patient}")
    
    # Search patients
    search_results = search_patients("Doe")
    print("\nSearch Results for 'Doe':")
    for result in search_results:
        print(f"{result.patient_id}: {result.first_name} {result.last_name}")

def demo_staff_operations():
    """Demonstrate staff operations"""
    print("\n=== Staff Operations Demo ===")
    
    # Add a new staff member
    new_staff = Staff(
        first_name="Sarah",
        last_name="Smith",
        role="Doctor",
        department="Cardiology",
        specialization="Cardiologist",
        license_number="MD12345",
        contact_info="sarah.smith@hospital.com",
        hire_date="2020-01-15"
    )
    staff_id = add_staff(new_staff)
    print(f"Added staff with ID: {staff_id}")
    
    # Get all staff
    staff_list = get_all_staff()
    print("\nAll Staff:")
    for staff in staff_list:
        print(f"{staff.staff_id}: {staff.first_name} {staff.last_name} ({staff.role})")
    
    # Get staff by role
    doctors = get_staff_by_role("Doctor")
    print("\nDoctors:")
    for doctor in doctors:
        print(f"{doctor.staff_id}: Dr. {doctor.last_name}")

def demo_appointment_operations():
    """Demonstrate appointment operations"""
    print("\n=== Appointment Operations Demo ===")
    
    # Get some existing patients and staff
    patients = get_all_patients()
    doctors = get_staff_by_role("Doctor")
    
    if patients and doctors:
        # Schedule an appointment
        appointment_date = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d %H:%M")
        new_appointment = Appointment(
            patient_id=patients[0].patient_id,
            staff_id=doctors[0].staff_id,
            appointment_date=appointment_date,
            purpose="Annual checkup",
            notes="Patient has history of high blood pressure"
        )
        appointment_id = add_appointment(new_appointment)
        print(f"Scheduled appointment with ID: {appointment_id}")
        
        # Get appointments for patient
        patient_appointments = get_appointments_by_patient(patients[0].patient_id)
        print("\nPatient's Appointments:")
        for appt in patient_appointments:
            print(f"Appt #{appt.appointment_id} on {appt.appointment_date} with Dr. {appt.staff_id}")

def main():
    setup_database()
    
    # Demonstrate operations
    demo_patient_operations()
    demo_staff_operations()
    demo_appointment_operations()

if __name__ == "__main__":
    main()