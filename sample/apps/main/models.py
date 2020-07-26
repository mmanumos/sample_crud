from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.AutoField(primary_key=True)  # autoincrement - Primary Key
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return str(self.name + " " + self.last_name)
