from django.shortcuts import render

def index(request):
    return render(request, 'index1.html')

def fire_alarm(request):
    return render(request, 'Fire_alarm.html')

def burglar_alarm(request):
    return render(request, 'Burglar_alarm.html')
