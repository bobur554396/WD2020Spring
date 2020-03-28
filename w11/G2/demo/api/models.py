from django.db import models


# DB Table Relations / Model Relations (Django)
# 1) OneToOne: 1 => 1, (Ex: 1 User - 1 Profile)
# 2) OneToMany -> ManyToOne: 1 => n, (Ex: 1 Category - Many Products)
# 3) ManyToMany: n => n, (Ex: Many Products - Many Tags)


class Category(models.Model):
    name = models.CharField(max_length=300)

    def short(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=300, unique=True)
    price = models.FloatField()
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')

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
