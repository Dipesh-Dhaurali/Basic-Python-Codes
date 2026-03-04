from django.db import models

# Create your models here.

class Student(models.Model):
    #id = models.AutoField() ==> django automatically add this field
    
    # Text field 
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    website = models.URLField()
    slug =models.SlugField(default='default-slug', unique=True) #/blog/1/   → less user-friendly   , /blog/my-first-post/   → readable and shareable

    #Numeric field
    age = models.IntegerField()
    phoneNumber = models.BigIntegerField()
    price = models.PositiveIntegerField()
    tax = models.DecimalField(max_digits=10, decimal_places=5) # Exact decimal values (used for money) ( always value required cannot be empty inside parameter)
    temperature = models.FloatField() #Decimal numbers (approximate)
    
    #Date and Time
    DOB = models.DateField() #Empty paramater
    created_date = models.DateField(auto_now_add=True)  # add the date each time when someone created and post somethings
    updated_date = models.DateField(auto_now=True)      # can be change and update
    interview_time=models.TimeField()
    DOB_and_time=models.DateTimeField()
    duration = models.DurationField() #can be time and date but need to handle

    #File & Media Fields
    image = models.ImageField() #require pillow
    file =  models.FileField() 

    #BooleanField and Choice Fields and JSONField
    is_active = models.BooleanField(default=True) 
    email_verified = models.BooleanField(null=True, blank=True) #null=true means if empty also no error
    
    skills = models.JSONField(default=dict)
    
    DEGREE_CHOICES = [
    ('highschool', 'High School'),
    ('bachelor', "Bachelor's"),
    ('master', "Master's"),
    ('phd', 'PhD'),
    ('diploma', 'Diploma'),
    ]
    degree=models.CharField(choices=DEGREE_CHOICES)
    



    #  UUIDField ( only theory this time) (from TextField)
    # id = models.AutoField(primary_key=True) ==> autoField django do itself
    # id = models.BigAutoField(primary_key=True) ==> BigAutoField when you have more than 2 billion ids
    
    #Later ==> count , cascade => parameters , case



    """
#) What is a Slug?

A slug is a short, URL-friendly version of a string, usually made from a title or name.
Rules:
--------
Lowercase letters
Numbers
Hyphens - instead of spaces
No special characters
"""