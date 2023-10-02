from datetime import datetime

class Patient:
    def __init__(self, first_name, last_name, title, date_of_birth, email, phone, alt_phone):

        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone
        self.alt_phone = alt_phone

    def greeting(self):

        return f"\nHello {self.title} {self.first_name} {self.last_name}! \n"

    def calculate_age(self):

        birthdate = self.date_of_birth
        current_date = datetime.now()
        age = current_date - birthdate

        years = age.days // 365
        months = (age.days % 365) // 30
        days = (age.days % 365) % 30

        return f"{years} Years | {months} Months | {days} Days Old\n"
    
    def send_appointment_reminder(self, appointment_date):
            
        message = f"Dear {self.first_name}, you have an appointment on {appointment_date}. \n"

        send_sms(message, self.phone)
        send_email(message, self.email)


            
def send_sms(msg, phone):
    print(f"Sending SMS to {phone}: {msg}")

    """Sends a given message to a given phone via SMS
    .

    You don't have to implement this function.
    """
    ...


def send_email(msg, email):
    print(f"Sending email to {email}: {msg}")
    """Sends a given message to a given address as email.

    You don't have to implement this function.
    """
    ...

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

print(patient1.calculate_age())

patient1.send_appointment_reminder(datetime(2023, 10, 13, 13, 0))
