import phonenumbers
from datetime import date
from phonenumbers.phonenumberutil import NumberParseException


def age_validator(date_of_birth):
    today = date.today()
    age = (
        today.year
        - date_of_birth.year
        - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    )
    if age not in range(18, 100):
        raise ValueError("Age must be over 18 and under 99")
    return date_of_birth


def policy_number_validator(policy_status, policy_number):
    if policy_status == "Policy Issued" and not policy_number:
        raise ValueError("Policy number if required after Policy is issued")


def phone_number_validator(number):
    try:
        if not phonenumbers.is_valid_number(phonenumbers.parse(number)):
            raise ValueError(
                "Phone number must be a valid Indian number starting with +91"
            )
        return number
    except NumberParseException as e:
        raise ValueError("Error parsing phone number") from e
