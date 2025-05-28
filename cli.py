import cmd
from datetime import datetime
from database.models import Patient, Staff, Appointment
from patients.patient_ops import *
from staff.staff_ops import *
from appointments.appointment_ops import *

class HospitalCLI(cmd.Cmd):
    intro = "Hospital Management System CLI. Type 'help' for commands."
    prompt = "(Hospital) > "

    # ----- Patient Commands -----
    def do_add_patient(self, arg):
        """Add a new patient: add_patient"""
        print("\n--- New Patient Registration ---")
        patient = Patient(
            first_name=input("First Name: "),
            last_name=input("Last Name: "),
            date_of_birth=input("Date of Birth (YYYY-MM-DD): "),
            gender=input("Gender: "),
            address=input("Address: "),
            phone=input("Phone: "),
            email=input("Email: "),
            blood_type=input("Blood Type: "),
            insurance_info=input("Insurance Info: "),
            emergency_contact=input("Emergency Contact: ")
        )
        patient_id = add_patient(patient)
        if patient_id:
            print(f"\nPatient added successfully with ID: {patient_id}")
        else:
            print("\nFailed to add patient.")

    def do_list_patients(self, arg):
        """List all patients: list_patients"""
        patients = get_all_patients()
        print("\n--- Patient List ---")
        for p in patients:
            print(f"{p.patient_id}: {p.first_name} {p.last_name} | Phone: {p.phone} | Email: {p.email}")

    def do_search_patients(self, arg):
        """Search patients by name or phone: search_patients <query>"""
        if not arg:
            print("Please provide a search term.")
            return
        results = search_patients(arg)
        print(f"\n--- Search Results for '{arg}' ---")
        for p in results:
            print(f"{p.patient_id}: {p.first_name} {p.last_name} | Phone: {p.phone}")

    # ----- Staff Commands -----
    def do_add_staff(self, arg):
        """Add new staff member: add_staff"""
        print("\n--- New Staff Registration ---")
        staff = Staff(
            first_name=input("First Name: "),
            last_name=input("Last Name: "),
            role=input("Role (Doctor/Nurse/Admin): "),
            department=input("Department: "),
            specialization=input("Specialization: "),
            license_number=input("License Number: "),
            contact_info=input("Contact Info: "),
            hire_date=datetime.now().strftime("%Y-%m-%d")
        )
        staff_id = add_staff(staff)
        if staff_id:
            print(f"\nStaff added successfully with ID: {staff_id}")
        else:
            print("\nFailed to add staff member.")

    def do_list_staff(self, arg):
        """List all staff: list_staff"""
        staff_members = get_all_staff()
        print("\n--- Staff List ---")
        for s in staff_members:
            print(f"{s.staff_id}: {s.first_name} {s.last_name} | {s.role} | {s.department}")

    # ----- Appointment Commands -----
    def do_schedule_appointment(self, arg):
        """Schedule new appointment: schedule_appointment"""
        print("\n--- New Appointment ---")
        self.do_list_patients("")
        patient_id = input("\nPatient ID: ")
        self.do_list_staff("")
        staff_id = input("Staff ID: ")
        date_str = input("Appointment Date & Time (YYYY-MM-DD HH:MM): ")
        purpose = input("Purpose: ")
        
        appointment = Appointment(
            patient_id=int(patient_id),
            staff_id=int(staff_id),
            appointment_date=date_str,
            purpose=purpose
        )
        appt_id = add_appointment(appointment)
        if appt_id:
            print(f"\nAppointment scheduled successfully with ID: {appt_id}")
        else:
            print("\nFailed to schedule appointment.")

    def do_list_appointments(self, arg):
        """List all appointments: list_appointments"""
        appointments = get_all_appointments()
        print("\n--- Appointments ---")
        for a in appointments:
            print(f"Appt #{a.appointment_id}: Patient {a.patient_id} with Staff {a.staff_id} on {a.appointment_date}")

    # ----- System Commands -----
    def do_clear_db(self, arg):
        """Clear and reset database: clear_db"""
        confirm = input("Are you sure you want to reset the database? (y/n): ")
        if confirm.lower() == 'y':
            import os
            if os.path.exists("data/hospital.db"):
                os.remove("data/hospital.db")
                print("Database cleared. Please restart the application.")
            else:
                print("Database file not found.")
        else:
            print("Database reset cancelled.")

    def do_exit(self, arg):
        """Exit the CLI: exit"""
        print("Exiting Hospital Management System.")
        return True

if __name__ == '__main__':
    HospitalCLI().cmdloop()