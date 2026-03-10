# Django CRUD Template 🐍


A simple and easy reference for Django CRUD operations .
Thi
```python
1) Using Django Shell

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

```



```html
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static'] 

# MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

#inside urls
# ----------------------------------------------------------------------
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# insite models
# ---------------------------------------------
cover = models.ImageField(upload_to='images/')





