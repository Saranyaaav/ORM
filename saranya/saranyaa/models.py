from django.db import models
from django.contrib import admin
class Football (models.Model):
    player_name=models.CharField(max_length=20)
    age=models.IntegerField()
    score=models.IntegerField()
    email=models.EmailField()
    date=models.DateField()
    
class FootballAdmin(admin.ModelAdmin):
    list_display=('player_name','age','score','email','date')
