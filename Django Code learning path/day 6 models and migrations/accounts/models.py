from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


#one to one realtionship
class Contact(models.Model):
    address=models.CharField(max_length=100)
    student=models.OneToOneField(Student,on_delete=models.CASCADE,related_name='contact')
    
    def __str__(self):
        return f"{self.student} - {self.address}"



#one to many relationship ( foreign key relationship )
class Attendance(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='attendance')
    
    def __str__(self):
        return f"{self.title} ({self.student})"



#many to many realtionship 
class Subjects(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title



class Faculty(models.Model):  
    name=models.CharField(max_length=100)
    subjects=models.ManyToManyField(Subjects,related_name='faculty') # note on delete not possible

    def __str__(self):
        return self.name
    

