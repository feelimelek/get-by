from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.
class Address(models.Model):
    UniqueConstraint(fields = ['cep', 'state'], name = 'address_pk')
    cep = models.IntegerField(primary_key=True)
    # sigla do estado:
    state = models.CharField(max_length=2)
    streetName = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.cep + '\n' + self.state