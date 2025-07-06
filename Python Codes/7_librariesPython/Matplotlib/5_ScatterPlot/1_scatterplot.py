"""
https://youtu.be/kM_eVEEWfnE (1:43:06)

"""
import matplotlib.pyplot as plt

hour_studies=[1,2,3,4,5,6,7,8]
exam_score=[50,55,60,65,70,75,80,85]

plt.scatter(hour_studies,exam_score,color='green',linestyle='--',marker='D',label='Student data')

plt.xlabel('Hours studied')
plt.ylabel('Exam Score')
plt.title("Relation between Study time and Score")
plt.grid(linestyle=':')
plt.legend()

plt.show()