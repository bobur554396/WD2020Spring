from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=1000)
    description = models.TextField(default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }
