from database.db import create_connection
from database.models import Staff

def add_staff(staff):
    """Add a new staff member to the database"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            sql = """INSERT INTO staff(
                        first_name, last_name, role, department,
                        specialization, license_number, contact_info, hire_date)
                    VALUES(?,?,?,?,?,?,?,?)"""
            cur = conn.cursor()
            cur.execute(sql, (
                staff.first_name, staff.last_name, staff.role, staff.department,
                staff.specialization, staff.license_number, staff.contact_info, staff.hire_date
            ))
            conn.commit()
            return cur.lastrowid
        except Exception as e:
            print(f"Error adding staff: {e}")
        finally:
            conn.close()
    return None

def get_all_staff():
    """Get all staff members from the database"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM staff")
            rows = cur.fetchall()
            
            staff_list = []
            for row in rows:
                staff_list.append(Staff(
                    staff_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    role=row[3],
                    department=row[4],
                    specialization=row[5],
                    license_number=row[6],
                    contact_info=row[7],
                    hire_date=row[8]
                ))
            return staff_list
        except Exception as e:
            print(f"Error getting staff: {e}")
        finally:
            conn.close()
    return []

def get_staff_by_id(staff_id):
    """Get a single staff member by ID"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM staff WHERE staff_id=?", (staff_id,))
            row = cur.fetchone()
            
            if row:
                return Staff(
                    staff_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    role=row[3],
                    department=row[4],
                    specialization=row[5],
                    license_number=row[6],
                    contact_info=row[7],
                    hire_date=row[8]
                )
        except Exception as e:
            print(f"Error getting staff: {e}")
        finally:
            conn.close()
    return None

def update_staff(staff):
    """Update an existing staff member"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            sql = """UPDATE staff
                     SET first_name = ?,
                         last_name = ?,
                         role = ?,
                         department = ?,
                         specialization = ?,
                         license_number = ?,
                         contact_info = ?,
                         hire_date = ?
                     WHERE staff_id = ?"""
            cur = conn.cursor()
            cur.execute(sql, (
                staff.first_name, staff.last_name, staff.role, staff.department,
                staff.specialization, staff.license_number, staff.contact_info, staff.hire_date,
                staff.staff_id
            ))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            print(f"Error updating staff: {e}")
        finally:
            conn.close()
    return 0

def delete_staff(staff_id):
    """Delete a staff member"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM staff WHERE staff_id=?", (staff_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            print(f"Error deleting staff: {e}")
        finally:
            conn.close()
    return 0

def get_staff_by_role(role):
    """Get staff members by their role"""
    conn = create_connection("data/hospital.db")
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM staff WHERE role=?", (role,))
            rows = cur.fetchall()
            
            staff_list = []
            for row in rows:
                staff_list.append(Staff(
                    staff_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    role=row[3],
                    department=row[4],
                    specialization=row[5],
                    license_number=row[6],
                    contact_info=row[7],
                    hire_date=row[8]
                ))
            return staff_list
        except Exception as e:
            print(f"Error getting staff by role: {e}")
        finally:
            conn.close()
    return []