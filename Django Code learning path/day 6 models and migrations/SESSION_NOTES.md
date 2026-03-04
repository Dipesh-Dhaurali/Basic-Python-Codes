# Session Notes - Template Engine
**Date:** March 4, 2026

## Today's Focus: Django Template Engine

### What I Did Today:

#### 1. **Project Setup**
   - Created Django project: `ecom`
   - Created Django apps: `home` and `accounts`
   - Configured INSTALLED_APPS in settings.py to include both apps

#### 2. **Template Engine Implementation**
   - **Template Inheritance**: Created `base.html` as a parent template with Bootstrap 5 styling
   - **Block System**: Used `{% block start %}` to define content areas in child templates
   - **Dynamic Titles**: Used `{{ title }}` variable to dynamically set page titles

#### 3. **Views & Context Passing**
   - **home view**: Passes a list of dictionaries containing people data with name and age
   - **about view**: Passes a list of skills
   - **contact view**: Basic contact view with title
   - All views use `render()` to pass context to templates

#### 4. **Template Tags & Features Used**

   **Variables:**
   - `{{ variable }}` - Display context variables
   - `{{ forloop.counter }}` - Display loop iteration count

   **Control Structures:**
   - `{% for item in list %}...{% endfor %}` - Loop through data
   - `{% if condition %}...{% elif %}...{% else %}...{% endif %}` - Conditional rendering
   - `{% in %}` - Check if value exists in list

   **Inheritance:**
   - `{% extends "base.html" %}` - Inherit parent template
   - `{% block name %}...{% endblock %}` - Define or override content blocks

   **Comments:**
   - `{% comment %}...{% endcomment %}` - Template comments

#### 5. **Template Files Created**
   - **base.html**: Master template with Bootstrap styling and table CSS
   - **index.html**: Home page with dynamic people table showing voting eligibility based on age
   - **aboutus.html**: About page displaying skills with conditional checks
   - **contactus.html**: Contact page (basic structure)

#### 6. **Key Template Engine Concepts Demonstrated**
   - Dynamic data rendering from Python dictionaries and lists
   - Conditional styling based on data (age < 18 shows red background)
   - Loop iteration with counters
   - Data existence checking with `in` operator
   - DRY principle through template inheritance
   - Responsive design with Bootstrap 5

### Code Snippets Implemented:

**Example - People Table with Conditional Styling:**
```django
{% for c in context %}  
<tr> 
    <td>{{forloop.counter}}</td>
    <td>{{c.name}}</td>
    <td>{{c.age}}</td>
    <td {% if c.age < 18 %} style="background:red" {% endif %}>
        {% if c.age >= 18 %}
        yes👍
        {% else %}
        no👎
        {% endif %}
    </td>
</tr>
{% endfor %}
```

**Example - Template Inheritance & Navigation:**
```django
{% extends "base.html" %}
{% block start %}
    <a href="/">Home</a>
    <a href="/contactus">Contactus</a>
    <a href="/aboutus">about</a>
{% endblock %}
```

### Key Learnings:
1. Django templates are powerful for server-side rendering with dynamic data
2. Template inheritance reduces code duplication significantly
3. Comments in templates help document template logic
4. Context dictionary is the bridge between Python views and HTML templates
5. Template tags allow complex logic without leaving the template layer

### Next Steps (Optional):
- Add static files (CSS, JavaScript) configuration
- Implement form handling in contact page
- Add database models for accounts app
- Style pages with custom CSS
- Add URL routing for admin panel
- Implement user authentication

---
**Status:** ✅ Template Engine foundation complete and working
