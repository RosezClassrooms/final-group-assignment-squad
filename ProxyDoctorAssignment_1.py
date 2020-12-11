from abc import ABC, abstractmethod

#Appopintment class
class Appointment(ABC):
    @abstractmethod

    def make_appointment(self):

        pass
#Doctor is Actual Subject that interacts with DoctorAssistant

# This class includes functions like is_available, get_Name, get_Expertise, set_date for appointment adjustment and specifications.
class Doctor(Appointment):

    def __init__(self,name, expertise):

        self.name = name
        self.expertise = expertise
        self.availability = True
        self.schedule=[]

    def is_available(self):
        return self.availability


    def get_name(self):
        return self.name

    def get_expertise(self):
        return self.expertise


    def set_date(self, date):
        if self.is_available():
            print("Appointment date " + str(date) + " accepted with the doctor:",self.get_name(),",",self.get_expertise(),".")
            self.schedule.append(date)

        else:
            print("Can't make appointment.")

    def make_appointment(self):
        if self.is_available():
            print("Appointment made.\n")

        else:
            print("Appointment can't be made beacuse the doctor is busy for entered day.\n")


#Doctor Assistant is our Proxy Subject that works as a proxy between patient and doctor
class DoctorAssistant(Appointment):

    #Assistant make appointment with requested date from patient and in the same time it checks the availability of doctor
    def make_appointment(self,date,doc):

        print("The assistant is trying to make appointment for the date:",date)
        for i in doc.schedule:
            if i==date:
                doc.availability=False
            else:
                doc.availability=True

        doc.set_date(date)
        return doc.make_appointment()

#Patient is our client interacts with Assistant
class Patient:

    #Assigning doctorassistant to  DoctorAssistant
    def __init__(self,name):
        self.doctorassistant = DoctorAssistant()
        self.name = name
        print("\n============ The patient" ,self.name, "contacted the doctor's assistant. Making an appointment for the doctor from the assistant... ===========\n")

# Date checking
    def appointment(self,date,doc):
        if (date<1 or date>31 ):
            print("You entered invalid date")
        else:
            self.doctorassistant.make_appointment(date,doc)

#Assigning Appointments to clients and doctors with Proxy template
if __name__ == "__main__":

    doc = Doctor("Dr. Williams","Neurologist")
    doc2 = Doctor("Dr. Satadisha", "Dermatologists")
    doc3 = Doctor("Dr. Merwyn ", "Gastroenterologists")
    doc4 = Doctor("Dr. Jake", "Oncologists")

    patient = Patient("Ilayda")
    patient.appointment(11,doc)
    patient.appointment(12,doc2)
    patient.appointment(13,doc3)

    patient2 = Patient("Birkan")
    patient2.appointment(11,doc)
    patient2.appointment(11,doc2)

    patient3 = Patient("Ugur")
    patient3.appointment(12,doc)
    patient3.appointment(11,doc4)
    patient3.appointment(13,doc3)

    patient4 = Patient("Kerem")
    patient4.appointment(23,doc2)
    patient4.appointment(11,doc2)
    patient4.appointment(41,doc4)
