from datetime import datetime

def send_sms(msg, phone):
    """Sends a given message to a given phone via SMS.

    You don't have to implement this function.
    """
    ...


def send_email(msg, email):
    """Sends a given message to a given address as email.

    You don't have to implement this function.
    """
    ...
class Patient:
    def __init__(self, name, surname, title, birthday, email, stationarynumber, mobilenumber):
        self.name = name
        self.surname = surname
        self.title = title
        self.birthday = birthday
        self.email = email 
        self.stationarynumber = stationarynumber
        self.mobilenumber = mobilenumber

    def greeting(self):
        return f"hello {self.title} {self.name} what is your problem? "  
    
    def send_appointment_reminder(self, date):

       msg = f"dear {self.name} this is a reminder that you have an appointment on {date}. "
       return send_email(msg,self.email)

    def calculate_age(self):
        time_now = datetime.now()
        age = time_now.year - self.birthday.year
        months = time_now.month - self.birthday.month
        days = time_now.day - self.birthday.day
        if days < 0:
            months -=1
            days += 30
        userage = f"{age} Y {months} M {days} D"
        return userage




# Solution goes here

patient1 = Patient(
    'John',
    'Doe',
    'mr.',
    datetime(1990, 2, 28),
    'john.doe@gmail.com',
    '+3345451555',
    '+6693932030',
)

print(patient1.greeting())

patient1.send_appointment_reminder(datetime(2023, 10, 13, 13, 0))
print(patient1.calculate_age())
