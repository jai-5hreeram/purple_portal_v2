from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from red_team.models import AttackIncident  # Importing the shared model

def dashboard(request):
    # Fetch all attacks, newest first
    incidents = AttackIncident.objects.all().order_by('-timestamp')
    
    # Simple logic: If more than 5 attacks exist, set alert level to High
    alert_level = "NORMAL"
    if incidents.count() > 5:
        alert_level = "CRITICAL"
        
    return render(request, 'blue_team/dashboard.html', {
        'incidents': incidents,
        'alert_level': alert_level
    })