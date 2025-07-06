#self example of packing in dictionary

def person(**data):
    score=0

    for i in data['marks']:
        score+=i

    prt=score/len('marks')
    print(f"my name is {data['name']} and my score is {score} and my percentage is {prt}")

dict1={
    'name':'Dipesh',
    'marks':[50,60,70,80,90]
}
person(**dict1)