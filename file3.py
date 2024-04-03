from collections import deque
from datetime import datetime, timedelta
from file1 import Patient, Doctor, Appointment, Prescription
from file2 import HospitalSystem

def main_menu(system):
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add patient record")
        print("2. Verify and remove patient record")
        print("3. Update patient record")
        print("4. Book an appointment")
        print("5. Cancel an appointment")
        print("6. Manage Queue")
        print("7. Issue a prescription")
        print("8. View recent prescriptions")
        print("9. Search for a patient and display a summary")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = input("Enter patient ID: ")
            if patient_id in system._HospitalSystem__patients:
                print("A patient with this ID already exists.")
                patient = system._HospitalSystem__patients[patient_id]
                confirmed_name = input(f"Is the patient's name {patient.get_details()[1]}? (Yes/No): ")
                if confirmed_name.lower() == 'yes':
                    print("Patient record already exists. No need to add again.")
                else:
                    print("Please double-check the patient ID and try again.")
            else:
                name = input("Enter patient's name: ")
                dob = input("Enter patient's date of birth (YYYY-MM-DD): ")
                medical_history = input("Enter patient's medical history: ")
                phone = input("Enter patient's phone number: ")
                allergies = input("Enter patient's allergies (comma separated, leave blank if none): ")
                allergies_list = allergies.split(",") if allergies else []
                current_medications = input("Enter patient's current medications (comma separated, leave blank if none): ")
                medications_list = current_medications.split(",") if current_medications else []
                new_patient = Patient(patient_id, name, dob, medical_history, phone, allergies_list, medications_list)
                system.add_patient_record(new_patient)

        elif choice == "2":
            patient_id = input("Enter patient ID to remove: ")
            name = input("Enter patient's name for verification: ")
            phone = input("Enter patient's phone number for verification: ")
            system.verify_and_remove_patient_record(patient_id, name, phone)

        elif choice == "3":
            patient_id = input("Enter patient ID to update: ")
            if patient_id in system._HospitalSystem__patients:
                patient = system._HospitalSystem__patients[patient_id]
                print("\nSelect the patient detail to update:")
                print("1. Name")
                print("2. Phone Number")
                print("3. Medical History")
                print("4. Allergies")
                print("5. Current Medications")
                print("6. Exit Update")
                update_options = {
                    "1": "name",
                    "2": "phone",
                    "3": "medical_history",
                    "4": "allergies",
                    "5": "current_medications"
                }
                update_choice = input("Enter your choice: ")
                if update_choice in update_options:
                    new_value = input(f"Enter the new {update_options[update_choice]}: ")
                    system.update_patient_record(patient_id, update_options[update_choice], new_value)

                else:
                    print("Invalid choice. Please enter a valid number or press '6' to exit update mode.")
            else:
                print("Patient ID does not exist in the system.")

        elif choice == "4":
            phone = input("Enter patient's phone number: ")
            matching_patients = [patient for patient_id, patient in system._HospitalSystem__patients.items() if
                                 patient._Patient__phone == phone]
            if not matching_patients:
                print("No patient record found for that phone number. Please add the patient first.")
                continue

            patient = matching_patients[0]
            patient_id = patient._Patient__patient_id
            patient_name = patient._Patient__name

            patient_name_confirmation = input(f"Is the patient's name {patient_name}? (Yes/No): ")
            if patient_name_confirmation.lower() != 'yes':
                print("Patient name does not match. Please try again.")
                continue

            print("\nAvailable Specializations:")
            for specialization in system._HospitalSystem__doctors:
                print(f"{specialization}")
            chosen_specialization = input("Choose a specialization: ")
            if chosen_specialization not in system._HospitalSystem__doctors:
                print("Specialization not found. Please try again.")
                continue

            print("\nAvailable Doctors:")
            for idx, doctor in enumerate(system._HospitalSystem__doctors[chosen_specialization], start=1):
                print(f"{idx}. {doctor._Doctor__name}")

            chosen_doctor_index = int(input("Choose a doctor by number: ")) - 1
            if not (0 <= chosen_doctor_index < len(system._HospitalSystem__doctors[chosen_specialization])):
                print("Invalid doctor choice. Please try again.")
                continue
            chosen_doctor = system._HospitalSystem__doctors[chosen_specialization][chosen_doctor_index]
            doctor_id = chosen_doctor._Doctor__doctor_id

            time_slots = system.generate_time_slots()
            print("\nAvailable Appointment Slots:")
            for idx, slot in enumerate(time_slots, start=1):
                print(f"{idx}. Date: {slot[0]}, Time: {slot[1]}")

            chosen_slot_index = int(input("Choose a slot number: ")) - 1
            if not (0 <= chosen_slot_index < len(time_slots)):
                print("Invalid slot choice. Please try again.")
                continue
            chosen_date, chosen_time = time_slots[chosen_slot_index]

            system.book_appointment(patient_id, doctor_id, chosen_date, chosen_time)


        elif choice == "5":
            appointment_id = input("Enter appointment ID: ")
            system.cancel_appointment(appointment_id)
        elif choice == "6":
            print("Managing Queue...")
            system.manage_queue()
        elif choice == "7":
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            medication = input("Enter medication details: ")
            system.issue_prescription(patient_id, doctor_id, medication)

        elif choice == "8":
            count = input("How many recent prescriptions do you want to see? ")
            try:
                count = int(count)
            except ValueError:
                print("Please enter a valid number.")
                continue
            recent_prescriptions = system.get_recent_prescriptions(count)
            print("\nRecent Prescriptions:")
            for prescription in recent_prescriptions:
                prescription_id, patient_id, doctor_id, date, medication = prescription.get_details()
                print(f"Prescription ID: {prescription_id}, Patient ID: {patient_id}, Doctor ID: {doctor_id}, Date: {date}, Medication: {medication}")
        elif choice == "9":
            patient_id = input("Enter patient ID to search: ")
            system.search_patient_summary(patient_id)

        elif choice == "10":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    hospital_system = HospitalSystem()
    main_menu(hospital_system)