from django.db import models

class Propriete(models.Model):
    adresse = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    chambres = models.IntegerField()
    salles_de_bain = models.IntegerField()
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    publie_le = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.adresse
