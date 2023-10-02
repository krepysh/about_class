from datetime import datetime


def send_sms(msg, phone):
    """Sends a given message to a given phone number as SMS.

    You don't have to implement this function.
    """
    ...


def send_email(msg, email):
    """Sends a given message to a given address as email.

    You don't have to implement this function.
    """
    ...

class Patient(object):
    def __init__(self, first_name, last_name, title, date, email, phone, mobile_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.age = datetime.now() - date
        self.email = email
        self.phone = phone
        self.mobile_phone = mobile_phone

    def greeting(self):
        return f"Hello, {self.title} {self.last_name}!"
    
    def send_sms(self, msg):
        send_sms(msg, self.mobile_phone)
    
    def send_email(self, msg):
        send_email(msg, self.email)

    def send_appointment_reminder(self, time):
        send_sms(f"Hi {self.first_name}, you have an appointment tomorrow at {time}.", self.mobile_phone)
        send_email(f"Hi {self.first_name}, you have an appointment tomorrow at {time}.", self.email)

patient1 = Patient(
    "John",
    "Doe",
    "mr.",
    datetime(1990, 2, 28),
    "john.doe@gmail.com",
    "+3345451555",
    "+6693932030",
)


print(patient1.greeting())

patient1.send_appointment_reminder(datetime(2023, 10, 13, 13, 0))
