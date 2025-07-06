#WAF to convert USD to NPR.
def exchange(usd,exchangeRate=137.77):
    NPR=usd*exchangeRate
    return NPR

us_amount=float(input("Enter the USD amount: "))
np_amount=exchange(us_amount)

print(f"{us_amount} USD = {np_amount} NPR  =>> ({us_amount}*137.77)")



"""
output
-----

Enter the USD amount: 10
10.0 USD = 1377.7 NPR  =>> (10.0*137.77)

"""