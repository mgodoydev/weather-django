from django.db import models

# Create your models here.
class WeatherQuery(models.Model):
    city = models.CharField(max_length=200)
    temperature = models.FloatField()
    description = models.CharField(max_length=300)
    queried_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.city} - {self.temperature}°C - ({self.description})' 