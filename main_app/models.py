from django.db import models
from django.urls import reverse

GENDERS = (
    ('M', 'Male/s'),
    ('F', 'Female/s'),
    ('B','Both male/s and female/s')
)

class Place(models.Model):
    name = models.CharField(max_length=40, unique=True)
    country = models.CharField(max_length=40)

class Finch(models.Model):
    name = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    size = models.CharField(max_length=25)
    range = models.CharField(max_length=25)
    places = models.ManyToManyField(Place)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id' : self.id})
    
class Sighting(models.Model):
    date = models.DateField('Seen on:')
    gender = models.CharField(
        max_length=1,
        choices=GENDERS,
        default=GENDERS[0][0],
        )

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_gender_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']    

