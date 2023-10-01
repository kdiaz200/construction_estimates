from django.contrib.auth.models import User
from django.db import models


class Region(models.Model):
    name = models.CharField('nombre', max_length=200)

    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'

class Trade(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'


class Subtrade(models.Model):
    name = models.CharField(max_length=100)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Subpartida'
        verbose_name_plural = 'Subpartidas'


class Material(models.Model):
    trade = models.ForeignKey(Trade, verbose_name='partida', on_delete=models.SET_NULL, null=True)
    subtrade = models.ForeignKey(Subtrade, verbose_name='subpartida', on_delete=models.SET_NULL, null=True)
    code = models.CharField('codigo', max_length=30, default='DEFAULT')
    name = models.CharField('nombre', max_length=200)
    # add drop down feature below
    unit = models.CharField('unidad', max_length=5, default='UNIT')
    unit_price = models.DecimalField('precio unitario', max_digits=10, decimal_places=2, default=0)
    region = models.ForeignKey(Region, verbose_name='región', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'


class Favorite(models.Model):
    user = models.ForeignKey(User, verbose_name='usuario', on_delete=models.CASCADE)
    material = models.ForeignKey(Material, verbose_name='material', on_delete=models.CASCADE)
    created_at = models.DateTimeField('creado en', auto_now_add=True)

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
