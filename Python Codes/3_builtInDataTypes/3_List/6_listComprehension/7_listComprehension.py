marks=[20,50,80,30,16,45,90,21]

passed=[i for i in marks if i>=50]
print(passed)

failed=[i for i in marks if i<50]
print(failed)
