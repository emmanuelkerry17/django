from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("inner/", views.inner, name="inner"),
    path("portfolio/", views.portfolio, name="portfolio"),

]
