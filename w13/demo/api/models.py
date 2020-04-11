from django.db import models


# Relations between tables
# - One to One ### 1 User - 1 Profile
# - One to Many ### 1 Category contains - many Products


class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=1000)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')

    def __str__(self):
        return f'Product id={self.id}, name={self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }
