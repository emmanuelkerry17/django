from django.urls import path
from . import views


urlpatterns=[
    path("", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("courses/", views.courses, name="courses"),
    path("location/", views.location, name="location")

]