from collections import deque
from datetime import datetime, timedelta

class Patient:
    def __init__(self, patient_id, name, dob, medical_history, phone, allergies=None, current_medications=None):
        self.__patient_id = patient_id
        self.__name = name
        self.__dob = datetime.strptime(dob, "%Y-%m-%d")
        self.__medical_history = medical_history
        self.__phone = phone
        self.__allergies = allergies if allergies else []
        self.__current_medications = current_medications if current_medications else []
        self.__appointments = deque()  # Queue of appointments

    def get_details(self):
        return self.__patient_id, self.__name, self.__phone

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_medical_history(self, medical_history):
        self.__medical_history = medical_history

    def set_allergies(self, allergies):
        self.__allergies = allergies

    def set_current_medications(self, current_medications):
        self.__current_medications = current_medications

    def add_appointment(self, appointment):
        self.__appointments.append(appointment)  # Add to the end of the queue

    def get_appointments(self):
        return self.__appointments

    def remove_appointment(self):
        if self.__appointments:  # Check if deque is not empty
            return self.__appointments.popleft()  # Remove and return the first appointment from the queue
        return None  # Return None if there are no appointments to remove


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization

class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time):
        self.__appointment_id = appointment_id
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__date = date
        self.__time = time

    def get_details(self):
        return self.__appointment_id, self.__patient_id, self.__doctor_id, self.__date, self.__time

    def get_id(self):
        return self.__appointment_id


class Prescription:
    def __init__(self, prescription_id, patient_id, doctor_id, date, medication):
        self.__prescription_id = prescription_id
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__date = date
        self.__medication = medication

    def get_details(self):
        return self.__prescription_id, self.__patient_id, self.__doctor_id, self.__date, self.__medication
