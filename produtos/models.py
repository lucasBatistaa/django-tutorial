from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        help_text="Nome da categoria",
        unique=True,
        max_length=80,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.name = self.name.upper()

        super(Category, self).save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(
        help_text="Nome do Produto",
        unique=True,
        max_length=80,
    )

    value = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
    )

    section = models.CharField(
        help_text="Nome da seção",
        unique=True,
        max_length=80,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.name = self.name.upper()

        super(Product, self).save(*args, **kwargs)