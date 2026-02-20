from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import AttackIncident

def trigger_attack(request):
    if request.method == "POST":
        # Get data from the form
        attack_type = request.POST.get('attack_type')
        payload_data = request.POST.get('payload')
        
        # Save to MySQL
        AttackIncident.objects.create(
            type=attack_type,
            payload=payload_data
        )
        return redirect('attack_success') # We will create this next
        
    return render(request, 'red_team/trigger.html')

def attack_success(request):
    return render(request, 'red_team/success.html')
