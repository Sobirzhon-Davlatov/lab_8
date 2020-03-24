from django.db import models



class Product(models.Model):
  name = models.CharField(max_length=300)
  price = models.FloatField(max_length=250)
  description = models.TextField()
  count = models.IntegerField(max_length=200)

  def to_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'price': self.price,
      'description': self.description,
      'count': self.count
    }


class Category(models.Model):
  name = models.CharField(max_length=400)

  def to_json(self):
    return {
      'id': self.id,
      'name': self.name
    }
