from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Service, Hairdresser, Appointment
from .forms import AppointmentForm

# Home page view
def index(request):
    return render(request, 'hairdresser/index.html')

# Booking appointment view
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ensure 'home' is defined in your URLs
    else:
        form = AppointmentForm()
    return render(request, 'hairdresser/book_appointment.html', {'form': form})

# Hairdresser page view
def hairdresser_view(request):
    # Return a rendered template or HttpResponse as needed
    return render(request, 'hairdresser/hairdresser.html')  # Updated template path
