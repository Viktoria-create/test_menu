from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField('MenuItem', related_name='menus')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    text = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
