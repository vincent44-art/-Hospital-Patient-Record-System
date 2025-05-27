# -Hospital-Patient-Record-System
# Hospital Management System

A complete Python-based hospital management system using SQLite for data persistence.

## Features

- **Patient Management**:
  - Add, view, update, and delete patient records
  - Search patients by name or phone number

- **Staff Management**:
  - Add, view, update, and delete staff records
  - Filter staff by role (Doctor, Nurse, etc.)

- **Appointment Scheduling**:
  - Schedule, view, update, and cancel appointments
  - View appointments by patient, staff, or date

## Setup

1. Clone this repository
2. Ensure you have Python 3.8+ installed
3. Run `python main.py` to:
   - Create the database directory
   - Initialize the SQLite database with all tables
   - Run a demonstration of all features

## Database Schema

The system uses SQLite and stores data in `data/hospital.db` with the following tables:

- `patients`: Stores patient information
- `staff`: Stores staff information
- `appointments`: Manages appointment scheduling
- `medical_records`: Stores patient medical history

## Modules

- `database/`: Database connection and models
  - `db.py`: Database connection and initialization
  - `models.py`: Data classes for system entities

- `patients/`: Patient operations
  - `patient_ops.py`: All patient-related database operations

- `staff/`: Staff operations
  - `staff_ops.py`: All staff-related database operations

- `appointments/`: Appointment operations
  - `appointment_ops.py`: All appointment-related database operations

## Usage

The `main.py` file contains demonstration code showing how to use all the system's features. You can:

1. Run it directly to see the system in action
2. Use it as reference to build your own interface
3. Import and use the operations modules in your own code

## Extending the System

To add more functionality:

1. Create new operation files for additional entities
2. Add new tables to `database/db.py`
3. Create new model classes in `database/models.py`
4. Implement new operation functions following the existing patterns