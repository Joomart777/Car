from django.db import models

# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


COUNTRY = (
    ('JP', 'Japan'),
    ('GR', 'Germany')
)


class Car(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True)
    country = models.CharField(max_length=50, choices=COUNTRY)
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand}, {self.title} - {self.country}'