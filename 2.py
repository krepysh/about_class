from datetime import datetime, timedelta


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
    def __init__(
            self,
            name: str,
            family_name: str,
            title: str,
            birthday: datetime,
            email: str,
            contact_phone: str,
            second_phone: str
    ):
        self.__name = name
        self.__family_name = family_name
        self.__title = title
        self.__birthday = birthday
        self.__email = email
        self.__contact_phone = contact_phone
        self.__second_phone = second_phone

    def send_appointment_reminder(self, appointment_date: datetime):
        reminder_message = f"""
            Dear {self.__title} {self.__name} {self.__family_name},
            It is a friendly reminder that you have an appointment on {appointment_date.strftime('%d.%m.%Y')} 
            at {appointment_date.strftime('%H:%M')}.
        """

        send_sms(reminder_message, self.__contact_phone)
        send_email(reminder_message, self.__email)

    def __full_age(self) -> str:
        age_difference = datetime.now() - self.__birthday

        age_in_years = age_difference.days // 365
        days_in_year = age_difference.days % 365
        age_in_months = days_in_year // 30
        age_in_days = days_in_year % 30

        return f"{age_in_years}Y {age_in_months}M {age_in_days}D"

    def greeting(self) -> str:
        return f"""
            Name: {self.__name}
            Family name: {self.__family_name}
            Email: {self.__email}
            Contact phone: {self.__contact_phone}
            Age: {self.__full_age()}
        """


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
