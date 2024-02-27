from django.db import models


class DadosRegistro(models.Model):

    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 15)
    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length = 14)
    last_name = models.CharField(max_length = 15)
    age = models.IntegerField()


    def __str__(self):
        return self.username
    