from django.db import models
from . import utils

# Create your models here.


class Cartoon(utils.CommonFields):
    tagline = models.CharField('слоган мультика', max_length=100)
    year = models.PositiveSmallIntegerField('год выпуска')
    number_of_episodes = models.PositiveSmallIntegerField('количество серий')
    poster = models.ImageField(upload_to='posters/')
    country = models.CharField('Страна производитель', max_length=50)


class Actor(utils.CommonFields):
    photo = models.ImageField(upload_to='actors/', blank=True)
    cartoon_actor = models.ManyToManyField(Cartoon)


class Screenshot(utils.CommonFields):
    image = models.ImageField(upload_to='screenshots/')
    cartoon_sc = models.ForeignKey(Cartoon, on_delete=models.CASCADE)


class Episode(utils.CommonFields):
    episode_number = models.PositiveSmallIntegerField()
    season_number = models.PositiveSmallIntegerField()
    cartoon_ep = models.ForeignKey(Cartoon, on_delete=models.CASCADE)
    episode_url = models.URLField()


class CartoonCategory(utils.CommonFields):
    cartoon_cat = models.ForeignKey(Cartoon, on_delete=models.CASCADE)






    
