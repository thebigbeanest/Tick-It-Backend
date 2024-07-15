from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image_url = models.TextField()
    capacity = models.IntegerField()
    type = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    venue_id = models.ForeignKey(Venue, related_name='events', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    image_url = models.TextField()

    def __str__(self):
        return self.name