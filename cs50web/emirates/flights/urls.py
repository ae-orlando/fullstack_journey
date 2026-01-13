from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # tring to make a page for each flight
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book" ),
]