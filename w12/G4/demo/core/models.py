from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField(default='')

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
        }

    def full(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
