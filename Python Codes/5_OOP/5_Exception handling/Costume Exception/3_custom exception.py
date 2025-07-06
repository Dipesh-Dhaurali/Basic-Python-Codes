"""
costume exception for phone number validation
"""

class InvalidNumberError(Exception):
    def __init__(self, number, message="Phone number is not valid."):

        self.message = message
        super().__init__(f"{message} Num: {number}")


def phNum(phone):
    if not phone.isdigit():
        raise InvalidNumberError(phone, "Phone number must contain only digits.")
    if len(phone) != 10:
        raise InvalidNumberError(phone, "Phone number must be 10 digits long.")
    print("Phone number is valid.")


try:
    p_number= input("Enter your number with 10 digits : ")
    phNum(p_number)

except InvalidNumberError as e:
    print("Error: ",e)
