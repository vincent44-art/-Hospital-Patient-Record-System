from database.db import create_connection
from database.models import Appointment
from datetime import datetime

def add_appointment(appointment):
    """Add a new appointment to the database"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            sql = """INSERT INTO appointments(
                        patient_id, staff_id, appointment_date,
                        purpose, status, notes)
                    VALUES(?,?,?,?,?,?)"""
            cur = conn.cursor()
            cur.execute(sql, (
                appointment.patient_id, appointment.staff_id, appointment.appointment_date,
                appointment.purpose, appointment.status, appointment.notes
            ))
            conn.commit()
            return cur.lastrowid
        except Exception as e:
            print(f"Error adding appointment: {e}")
        finally:
            conn.close()
    return None

def get_all_appointments():
    """Get all appointments from the database"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM appointments")
            rows = cur.fetchall()
            
            appointments = []
            for row in rows:
                appointments.append(Appointment(
                    appointment_id=row[0],
                    patient_id=row[1],
                    staff_id=row[2],
                    appointment_date=row[3],
                    purpose=row[4],
                    status=row[5],
                    notes=row[6]
                ))
            return appointments
        except Exception as e:
            print(f"Error getting appointments: {e}")
        finally:
            conn.close()
    return []

def get_appointment_by_id(appointment_id):
    """Get a single appointment by ID"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM appointments WHERE appointment_id=?", (appointment_id,))
            row = cur.fetchone()
            
            if row:
                return Appointment(
                    appointment_id=row[0],
                    patient_id=row[1],
                    staff_id=row[2],
                    appointment_date=row[3],
                    purpose=row[4],
                    status=row[5],
                    notes=row[6]
                )
        except Exception as e:
            print(f"Error getting appointment: {e}")
        finally:
            conn.close()
    return None

def update_appointment(appointment):
    """Update an existing appointment"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            sql = """UPDATE appointments
                     SET patient_id = ?,
                         staff_id = ?,
                         appointment_date = ?,
                         purpose = ?,
                         status = ?,
                         notes = ?
                     WHERE appointment_id = ?"""
            cur = conn.cursor()
            cur.execute(sql, (
                appointment.patient_id, appointment.staff_id, appointment.appointment_date,
                appointment.purpose, appointment.status, appointment.notes,
                appointment.appointment_id
            ))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            print(f"Error updating appointment: {e}")
        finally:
            conn.close()
    return 0

def delete_appointment(appointment_id):
    """Delete an appointment"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM appointments WHERE appointment_id=?", (appointment_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            print(f"Error deleting appointment: {e}")
        finally:
            conn.close()
    return 0

def get_appointments_by_patient(patient_id):
    """Get all appointments for a specific patient"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM appointments WHERE patient_id=?", (patient_id,))
            rows = cur.fetchall()
            
            appointments = []
            for row in rows:
                appointments.append(Appointment(
                    appointment_id=row[0],
                    patient_id=row[1],
                    staff_id=row[2],
                    appointment_date=row[3],
                    purpose=row[4],
                    status=row[5],
                    notes=row[6]
                ))
            return appointments
        except Exception as e:
            print(f"Error getting patient appointments: {e}")
        finally:
            conn.close()
    return []

def get_appointments_by_staff(staff_id):
    """Get all appointments for a specific staff member"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM appointments WHERE staff_id=?", (staff_id,))
            rows = cur.fetchall()
            
            appointments = []
            for row in rows:
                appointments.append(Appointment(
                    appointment_id=row[0],
                    patient_id=row[1],
                    staff_id=row[2],
                    appointment_date=row[3],
                    purpose=row[4],
                    status=row[5],
                    notes=row[6]
                ))
            return appointments
        except Exception as e:
            print(f"Error getting staff appointments: {e}")
        finally:
            conn.close()
    return []

def get_appointments_by_date(date):
    """Get all appointments for a specific date"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM appointments WHERE date(appointment_date)=date(?)", (date,))
            rows = cur.fetchall()
            
            appointments = []
            for row in rows:
                appointments.append(Appointment(
                    appointment_id=row[0],
                    patient_id=row[1],
                    staff_id=row[2],
                    appointment_date=row[3],
                    purpose=row[4],
                    status=row[5],
                    notes=row[6]
                ))
            return appointments
        except Exception as e:
            print(f"Error getting appointments by date: {e}")
        finally:
            conn.close()
    return []