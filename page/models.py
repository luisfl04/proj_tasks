from django.db import models


class DadosCard(models.Model):

    titulo_card = models.CharField(max_length = 100)
    tarefas_card = models.CharField(max_length = 100)
    done = models.BooleanField(default = False)

    def make_done(self):
        self.done = True
        self.save()

        
