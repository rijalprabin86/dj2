from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hairdresser/index.html')


from django.shortcuts import render , redirect
from .models import Service, Hairdresser, Appointment
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'hairdresser/book_appointment.html', {'form': form})