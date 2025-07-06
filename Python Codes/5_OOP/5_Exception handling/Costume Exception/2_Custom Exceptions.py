"""
cont...
"""
# costom exception form age validation
class AgeError(Exception):

    pass

try:
    age=5
    if age<18:
        raise AgeError

except AgeError:
    print("Person is not eligible to vote")
else:
    print("Person is eligible to vote")