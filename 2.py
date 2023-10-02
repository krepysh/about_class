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
# Solution goes here

class Patient:
    def __init__(self, name, family_name, sex, birthday, gmail, number1, number2):
        self.name = name
        self.family_name = family_name
        self.sex = sex
        self.birthday = birthday
        self.gmail = gmail
        self.number1 = number1
        self.number2 = number2

    def greeting(self):
        return f'Hello {self.sex} {self.name} {self.family_name} !'

    def age(self):
        now = datetime.now()
        your_age = now.year - self.birthday.year
        your_month = now.month - self.birthday.month
        your_day = now.day - self.birthday.day
        if your_month < 0:
            your_month = int(your_month) * -1
            your_age = your_age -1
        if your_day < 0:
            your_day = your_day * -1
            your_month = your_month -1
            if your_month < 0:
                your_month = int(your_month) * -1
                your_age = your_age -1

        return f'{your_age}Y {your_month}M {your_day}D'
    
    def send_appointment_reminder(self, date):
        self.date = date
        msg = f'I send an appointment reminder letter. Your appointment will be {self.date}'
        send_email(msg , self.gmail)
        send_sms(msg, self.number1)
        send_sms(msg, self.number2)
        return msg


        


patient1 = Patient(
    'John',
    'Doe',
    'mr.',
    datetime(1994, 2, 25),
    'john.doe@gmail.com',
    '+3345451555',
    '+6693932030',
)
print(patient1.greeting())
print(patient1.age())
print(patient1.send_appointment_reminder(datetime(2023, 10, 13, 13, 0)))
