from django.db import models

# Create your models here.
from django.db import models

class AttackIncident(models.Model):
    ATTACK_TYPES = [
        ('SQLI', 'SQL Injection'),
        ('XSS', 'Cross-Site Scripting'),
        ('BRUTE', 'Brute Force'),
    ]
    
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=ATTACK_TYPES)
    payload = models.TextField(help_text="The malicious string or script used")
    attacker_ip = models.GenericIPAddressField(default="127.0.0.1")

    def __str__(self):
        return f"{self.type} - {self.timestamp}"