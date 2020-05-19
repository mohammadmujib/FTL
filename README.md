

# Overview

Django REST framework is a powerful and flexible toolkit for building Web APIs.

# Requirements

* Python (3.5, 3.6, 3.7, 3.8)
* Django ( 3.0)

We **highly recommend** and only officially support the latest patch release of
each Python and Django series.

# Installation

Install using `pip`...

    pip install djangorestframework

Add `'rest_framework'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]
# Example

Let's take a look at a quick example of using REST framework to build a simple model-backed API for accessing users and groups.

Startup up a new project like so...

    pip install django
    pip install djangorestframework
    django-admin startproject test_api .
    ./manage.py migrate
    ./manage.py createsuperuser


Now edit the `test_api/urls.py` module in your project:

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('apis.urls')),
]

```

Now Define New models in `models.py`

```python
from django.db import models

class Member(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)

class Activity(models.Model):
    member = models.ForeignKey(
        Member, related_name='activities', null=True, on_delete=models.SET_NULL)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(blank=True, null=True)


```



Now Create New Files in `serielizers.py` 

```python
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('start_time','end_time',)
        model = Activity
        
class MemberSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        fields = ('id','real_name','tz','activities',)
        model = Member

```

Now edit in `views.py` 

```python

class ListCreateMember(generics.ListCreateAPIView):
    queryset = models.Member.objects.all()
    serializer_class = MemberSerializer
```

That's it, we're done!

Now Start Server

    $ python manage.py runserver
You can now open the API in your browser at `http://127.0.0.1:8000/api/`, and view your API. 

```
GET /api/
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "real_name": "Glinda Southgood",
        "tz": "Asia/Kolkata",
        "activities": [
            {
                "start_time": "2020-05-19T21:02:53.626718Z",
                "end_time": "2020-05-28T20:44:23Z"
            },
            {
                "start_time": "2020-05-19T20:47:44.543114Z",
                "end_time": "2020-05-11T20:47:42Z"
            }
        ]
    },
```

# Retrieve Update Destroy Member

`http://127.0.0.1:8000/api/1`

```
GET /api/1/
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "real_name": "Glinda Southgood",
    "tz": "Asia/Kolkata",
    "activities": [
        {
            "start_time": "2020-05-19T21:02:53.626718Z",
            "end_time": "2020-05-28T20:44:23Z"
        },
        {
            "start_time": "2020-05-19T20:47:44.543114Z",
            "end_time": "2020-05-11T20:47:42Z"
        }
    ]
}
```

# List Create Activity

`http://127.0.0.1:8000/api/1/activities`

```
GET /api/1/activities/
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "start_time": "2020-05-19T21:02:53.626718Z",
        "end_time": "2020-05-28T20:44:23Z"
    },
    {
        "start_time": "2020-05-19T20:47:44.543114Z",
        "end_time": "2020-05-11T20:47:42Z"
    }
]
```

# Retrieve Update Destroy Activity

`http://127.0.0.1:8000/api/1/activities/1`

```
GET /api/1/activities/1/
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "start_time": "2020-05-19T21:02:53.626718Z",
    "end_time": "2020-05-28T20:44:23Z"
}
```

