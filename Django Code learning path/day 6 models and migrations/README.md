# Ecom Django Project

A Django-based e-commerce template project demonstrating the Django Template Engine with template inheritance, dynamic data rendering, and conditional logic.

## 📋 Project Overview

This project showcases:
- Django Template Engine fundamentals
- Template inheritance and block system
- Dynamic context passing from views to templates
- Template tags, filters, and conditionals
- Bootstrap 5 responsive design

## 📁 Project Structure

```
ecom/
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── SESSION_NOTES.md           # Today's session documentation
├── README.md                  # This file
├── ecom/                      # Project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py               # URL routing
│   ├── asgi.py               # ASGI configuration
│   └── wsgi.py               # WSGI configuration
├── home/                      # Home app
│   ├── models.py             # Database models
│   ├── views.py              # View functions (home, about, contact)
│   ├── urls.py               # App URL routing
│   ├── admin.py              # Admin configuration
│   └── templates/            # HTML templates
│       ├── base.html         # Parent template with inheritance
│       ├── index.html        # Home page (people list with voting logic)
│       ├── aboutus.html      # About page (skills display)
│       └── contactus.html    # Contact page
└── accounts/                  # Accounts app (for future user authentication)
    ├── models.py
    ├── views.py
    └── admin.py
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Django 6.0.2
- pip (Python package manager)

### Installation

1. **Clone/Navigate to project directory:**
   ```bash
   cd ecom
   ```

2. **Install Django (if not already installed):**
   ```bash
   pip install django
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the application:**
   - Home: `http://127.0.0.1:8000/`
   - About: `http://127.0.0.1:8000/aboutus`
   - Contact: `http://127.0.0.1:8000/contactus`

## 🎯 Key Features

### 1. **Template Inheritance**
- `base.html` serves as the master template
- Child templates extend base.html using `{% extends %}`
- Content blocks allow customization per page

### 2. **Dynamic Data Rendering**
- Views pass context dictionaries to templates
- Templates render data using `{{ variable }}` syntax
- Support for nested data structures (lists, dictionaries)

### 3. **Template Tags Used**
- **For Loops:** `{% for item in list %}...{% endfor %}`
- **Conditionals:** `{% if condition %}...{% else %}...{% endif %}`
- **Comments:** `{% comment %}...{% endcomment %}`
- **Membership:** `{% if value in list %}`
- **Blocks:** `{% block name %}...{% endblock %}`

### 4. **Features by Page**

**Home Page (`index.html`):**
- Displays list of people in a table
- Shows name, age, and voting eligibility
- Uses `forloop.counter` for serial numbers
- Conditional styling: age < 18 highlights in red
- Dynamic vote eligibility calculation

**About Page (`aboutus.html`):**
- Displays list of skills
- Uses conditional checks with `in` operator
- Shows template variable output

**Contact Page (`contactus.html`):**
- Basic contact page structure
- Uses template inheritance

## 🔧 Views Configuration

All views are in `home/views.py`:

```python
def home(request):
    peoples = [
        {"name":"Dipesh Dhaurali" , "age":22},
        # ... more people data
    ]
    context = {"context": peoples, "title": "Ecom Site"}
    return render(request, "index.html", context)

def about(request):
    skills = ['python', 'php', 'django', 'sql']
    context = {"context": skills, "title": "aboutus"}
    return render(request, "aboutus.html", context)

def contact(request):
    context = {"title": "contactus"}
    return render(request, "contactus.html", context)
```

## 📝 Template Examples

### Using Template Inheritance
```django
{% extends "base.html" %}
{% block start %}
    <!-- Page-specific content -->
{% endblock %}
```

### Loop with Conditional
```django
{% for person in people %}
    {% if person.age >= 18 %}
        <p>{{ person.name }} can vote</p>
    {% endif %}
{% endfor %}
```

## 🎨 Styling

- Bootstrap 5 CDN integrated in `base.html`
- Custom table styling with borders
- Conditional inline styles based on data values

## 📚 Django Template Engine Concepts Covered

| Concept | Example | Purpose |
|---------|---------|---------|
| Variables | `{{ variable }}` | Display dynamic data |
| Filters | `{{ variable \| filter }}` | Modify variable output |
| Tags | `{% tag %}` | Implement logic in templates |
| Inheritance | `{% extends %}` | DRY principle for templates |
| Blocks | `{% block %}...{% endblock %}` | Define overridable sections |
| Loops | `{% for item in list %}` | Iterate through data |
| Conditionals | `{% if condition %}` | Conditional rendering |

## 🔮 Future Enhancements

- [ ] Add accounts app for user authentication
- [ ] Implement contact form with database storage
- [ ] Add product models and admin interface
- [ ] Static files configuration (CSS, JS, images)
- [ ] Database integration with custom models
- [ ] Admin panel customization
- [ ] User login/logout functionality
- [ ] Shopping cart feature

## 📖 Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Template Engine Guide](https://docs.djangoproject.com/en/6.0/topics/templates/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)

## 👨‍💻 Developer

- **Dipesh Dhaurali**

## 📅 Last Updated

- **March 4, 2026** - Template Engine implementation and documentation

---

**Status:** ✅ Active Development - Template Engine Foundation Complete
