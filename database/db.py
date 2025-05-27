import sqlite3
from sqlite3 import Error
import os

def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except Error as e:
        print(e)
    return conn

def initialize_database(conn):
    """ Initialize database tables """
    try:
        cursor = conn.cursor()
        
        # Patients table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            date_of_birth TEXT,
            gender TEXT,
            address TEXT,
            phone TEXT,
            email TEXT UNIQUE,
            blood_type TEXT,
            insurance_info TEXT,
            emergency_contact TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        # Staff table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS staff (
            staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            role TEXT NOT NULL,
            department TEXT,
            specialization TEXT,
            license_number TEXT UNIQUE,
            contact_info TEXT,
            hire_date TEXT
        );
        """)
        
        # Appointments table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            staff_id INTEGER NOT NULL,
            appointment_date TEXT NOT NULL,
            purpose TEXT,
            status TEXT DEFAULT 'Scheduled',
            notes TEXT,
            FOREIGN KEY (patient_id) REFERENCES patients (patient_id) ON DELETE CASCADE,
            FOREIGN KEY (staff_id) REFERENCES staff (staff_id) ON DELETE CASCADE
        );
        """)
        
        # Medical records table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS medical_records (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            diagnosis TEXT,
            treatment TEXT,
            notes TEXT,
            record_date TEXT DEFAULT CURRENT_TIMESTAMP,
            physician_id INTEGER,
            FOREIGN KEY (patient_id) REFERENCES patients (patient_id) ON DELETE CASCADE,
            FOREIGN KEY (physician_id) REFERENCES staff (staff_id)
        );
        """)
        
        conn.commit()
    except Error as e:
        print(f"Error initializing database: {e}")