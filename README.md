# detect-django-version
Demonstrates a simple approach to detect which version of Django a website is running. The website you are trying to identify the version must be using the django.contrib.admin app, as it is used to detect the version.

## Usage

```python
from detect import detect

print(detect('http://<site>/static/admin'))
```
