from django.db import models

# Create your models here.
class Contacto(models.Model):
    full_name = models.CharField(max_length=60)
    email_contact = models.EmailField(max_length=100)
    subject_contact = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    message_contact = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name

class Servicio(models.Model):
    name = models.CharField(max_length=70)
    images = models.ImageField('Imagen', blank = True, null = True)
    description = models.CharField('Descripción', max_length = 500, blank = True, null = True)
    is_avaliable = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name