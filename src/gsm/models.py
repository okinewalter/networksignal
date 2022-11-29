from django.db import models

class Network(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = 'Networks'

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name

class Signal(models.Model):   
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Signals'

    def __str__(self):
        return (self.network.name+' '+self.location.name)

class Topsearch(models.Model): 
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    counter = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Topsearches'

    def __str__(self):
        return self.location.name