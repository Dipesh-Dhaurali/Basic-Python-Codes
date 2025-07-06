"""
code with harry(Finally keyword in Python)
+
bro code(Python EXCEPTION HANDLING)(last tira)

"""
a=5
try:
    n = int(input("Enter any number : "))   # user supposes to write string name inside integer
    div=a/n
    print(div)
except Exception as e:
    print(e)
finally:
    print("It will always print")



"""
note:
1) finally always execute weather the error occurs or not

"""