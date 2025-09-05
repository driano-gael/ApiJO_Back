from django.db import models
from api.models.lieu import Lieu


class Evenement(models.Model):
    description = models.CharField(max_length=250)
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='evenements')
    date = models.DateField()
    horraire= models.TimeField()
    nb_place_total = models.IntegerField(default=1000)
    nb_place_restante = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        if not self.pk:  # création
            if self.nb_place_restante is None:
                self.nb_place_restante = self.nb_place_total
        super().save(*args, **kwargs)