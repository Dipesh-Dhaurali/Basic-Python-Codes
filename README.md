# Django CRUD Template 🐍

1) Using Django Shell
A simple and easy reference for Django CRUD operations .
Thi
```python
# C = Create
ClassName.objects.create(obj1="value1", obj2=2, obj3="value3")

# R = Read
ClassName.objects.all()
ClassName.objects.get(obj1="value")
ClassName.objects.filter(id=1)

# U = Update
ClassName.objects.filter(id=1).update(obj="value")

# D = Delete
ClassName.objects.get(id=1).delete()
ClassName.objects.filter(id=2).delete()
ClassName.objects.all().delete()  # Delete all objects




2) Using Django Admin Pannel
inside admin.py
-----------
admin.site.register(ModelName)


models.py
-------------------
def __str__(self):
        return self.name





link
https://youtu.be/khdVg1lLbZo
