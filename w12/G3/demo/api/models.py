from django.db import models


# DB Relations / Model Relations
# 1) OneToOne: 1 => 1, (Ex: 1 User - 1 Profile)
# 2) OneToMany: 1 => n, (Ex: 1 Category - many Products)
# 3) ManyToMany: n => n, (Ex: Many products - Many tags)


class Category(models.Model):
    name = models.CharField(max_length=300)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='products', null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }
