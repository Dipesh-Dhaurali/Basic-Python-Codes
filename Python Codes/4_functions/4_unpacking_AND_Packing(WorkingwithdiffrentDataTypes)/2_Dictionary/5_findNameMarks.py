#self example of Unpacking in dictionary

def person(name,marks):
    score=0
    for i in marks:
        score+=i
    perct=score/len(marks)
    return name,marks,score,perct

a,b,s,p=person('Hari',[10,20,30,40,50])
print(b)

print(f"my name is {a} my total score is {s} and percentage is {p}")