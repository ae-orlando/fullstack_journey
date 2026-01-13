# Lec3: Django
## 13th Jan, 2026
### Discovered:
#### **functions:**
    From "django.contrib.auth"
1. **authenticate()**
```
authenticate(request, username="username", password="password")
```
    This:
        - Takes request, username and password.
        - if the username is valid it returns the users name.
---
2. **login()**
```
login(request, user)

    This:
    - logs in the user.
```
