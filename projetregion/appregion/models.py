from django.db import models

# Create your models here.

class Region(models.Model):
    nom = models.CharField(max_length=50)
    biome = models.CharField(max_length=50)
    description = models.TextField(null = True,blank = True)

    def __str__(self):
        chaine = f"Région de {self.nom}"#, biome {self.biome}, voici la description de cette région : {self.description}"
        return chaine

    def dico(self):
        return{'nom':self.nom,'biome':self.biome,'description':self.description}

class Champ(models.Model):
    region = models.ForeignKey("Region",on_delete=models.CASCADE, default=None)
    alias = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    sexe = models.CharField(max_length=50)
    classification = models.TextField(blank = False)

    def __str__(self):
        chaine2 = f"Le champion {self.alias}"#Alias : {self.alias}, Âge : {self.age}, Sexe : {self.sexe}, Classification {self.classification}, champion de la région de {self.region.nom}"
        return chaine2

    def dico(self):
        return{'region' : self.region.nom, 'alias' : self.alias,'age' : {self.age}, 'sexe' : self.sexe, 'classification': self.classification}


