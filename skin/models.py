from django.db import models

# Create your models here.
class SkinDiseasesClassification(models.Model):
    skin_image           = models.ImageField(upload_to='skin_process/')
    skin_classification  = models.CharField(max_length=225)
    skin_accuracy        = models.CharField(max_length=225)
    
    class Meta:
        verbose_name_plural = 'Skin Diseases Classification'
        
    def __str__(self):
        return f"Image ( {self.id} ) , it classify to ( {self.skin_classification} ) , with accuracy ( {self.skin_accuracy} % )"

class SkinDiseasesInfo(models.Model):
    title      = models.CharField(max_length=255)
    definition = models.TextField()
    causes     = models.TextField()
    treatment  = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Skin Diseases Info'
        
    def __str__(self):
        return self.title
