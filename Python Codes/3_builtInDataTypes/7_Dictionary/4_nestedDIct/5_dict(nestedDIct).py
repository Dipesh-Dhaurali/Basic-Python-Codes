"""
https://youtu.be/078tYSD7K8E?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0
Shradha Khapra (Lecture 4 : 2_Dictionary) (12:40)

"""""
#creating nested dictionary
student={
    'name':'Dipesh',
    'Age':21,
    'marks':{
                'python':98,
                'AI':99,
                'IS':97
            },

    'address':'kathmandu'
}

print(student)  #{'name': 'Dipesh', 'Age': 21, 'marks': {'python': 98, 'AI': 99, 'IS': 97}, 'address': 'kathmandu'}

print(student['marks']) #{'python': 98, 'AI': 99, 'IS': 97}
print(student['marks']['AI'])  #99
