from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # The root URL
    path('book/', views.book_appointment, name='book_appointment'),  # Booking page
    path('hairdresser/', views.hairdresser_view, name='hairdresser'),  # Hairdresser page
]
