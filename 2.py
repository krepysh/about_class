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

    def __init__(self, first_name, second_name, title, birth_date, email, phone_number, mobile_number):
        self.first_name = first_name
        self.second_name = second_name
        self.title = title
        self.birth_date = birth_date
        self.email = email
        self.phone_number = phone_number
        self.mobile_number = mobile_number

    def greeting(self):
        return f"Hello {self.title} {self.first_name} {self.second_name}"

    def calculating_age(self,current_date):
        age = current_date.year - self.birth_date.year
        month = current_date.month - self.birth_date.month
        days = current_date.day - self.birth_date.day
        if days < 0:
            month -= 1
            days += 30
        if month < 0:
            age -= 1

        return f"{age} Y {month} M {days} D"

    def send_appointment_reminder(self, appointment_date):
        current_date = datetime.now()
        age = self.calculating_age(current_date)

        msg = f"Dear {self.first_name}, your appointment is scheduled for {appointment_date.strftime('%Y-%m-%d %H:%M')}.\n"
        msg += f"Your age is {age}"

        send_sms(msg, self.mobile_number)
        send_email(msg, self.email)

        print(msg)




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
