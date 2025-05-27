from database.db import create_connection
from database.models import Patient

def add_patient(patient):
    """Add a new patient to the database"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            sql = """INSERT INTO patients(
                        first_name, last_name, date_of_birth, gender, 
                        address, phone, email, blood_type, 
                        insurance_info, emergency_contact)
                    VALUES(?,?,?,?,?,?,?,?,?,?)"""
            cur = conn.cursor()
            cur.execute(sql, (
                patient.first_name, patient.last_name, patient.date_of_birth,
                patient.gender, patient.address, patient.phone, patient.email,
                patient.blood_type, patient.insurance_info, patient.emergency_contact
            ))
            conn.commit()
            return cur.lastrowid
        except Exception as e:
            print(f"Error adding patient: {e}")
        finally:
            conn.close()
    return None

def get_all_patients():
    """Get all patients from the database"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM patients")
            rows = cur.fetchall()
            
            patients = []
            for row in rows:
                patients.append(Patient(
                    patient_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    date_of_birth=row[3],
                    gender=row[4],
                    address=row[5],
                    phone=row[6],
                    email=row[7],
                    blood_type=row[8],
                    insurance_info=row[9],
                    emergency_contact=row[10],
                    created_at=row[11]
                ))
            return patients
        except Exception as e:
            print(f"Error getting patients: {e}")
        finally:
            conn.close()
    return []

def get_patient_by_id(patient_id):
    """Get a single patient by ID"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM patients WHERE patient_id=?", (patient_id,))
            row = cur.fetchone()
            
            if row:
                return Patient(
                    patient_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    date_of_birth=row[3],
                    gender=row[4],
                    address=row[5],
                    phone=row[6],
                    email=row[7],
                    blood_type=row[8],
                    insurance_info=row[9],
                    emergency_contact=row[10],
                    created_at=row[11]
                )
        except Exception as e:
            print(f"Error getting patient: {e}")
        finally:
            conn.close()
    return None

def update_patient(patient):
    """Update an existing patient"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            sql = """UPDATE patients
                     SET first_name = ?,
                         last_name = ?,
                         date_of_birth = ?,
                         gender = ?,
                         address = ?,
                         phone = ?,
                         email = ?,
                         blood_type = ?,
                         insurance_info = ?,
                         emergency_contact = ?
                     WHERE patient_id = ?"""
            cur = conn.cursor()
            cur.execute(sql, (
                patient.first_name, patient.last_name, patient.date_of_birth,
                patient.gender, patient.address, patient.phone, patient.email,
                patient.blood_type, patient.insurance_info, patient.emergency_contact,
                patient.patient_id
            ))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            print(f"Error updating patient: {e}")
        finally:
            conn.close()
    return 0

def delete_patient(patient_id):
    """Delete a patient"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM patients WHERE patient_id=?", (patient_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            print(f"Error deleting patient: {e}")
        finally:
            conn.close()
    return 0

def search_patients(search_term):
    """Search patients by name or phone"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            search_pattern = f"%{search_term}%"
            cur.execute("""
                SELECT * FROM patients 
                WHERE first_name LIKE ? OR last_name LIKE ? OR phone LIKE ?
            """, (search_pattern, search_pattern, search_pattern))
            rows = cur.fetchall()
            
            patients = []
            for row in rows:
                patients.append(Patient(
                    patient_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    date_of_birth=row[3],
                    gender=row[4],
                    address=row[5],
                    phone=row[6],
                    email=row[7],
                    blood_type=row[8],
                    insurance_info=row[9],
                    emergency_contact=row[10],
                    created_at=row[11]
                ))
            return patients
        except Exception as e:
            print(f"Error searching patients: {e}")
        finally:
            conn.close()
    return []