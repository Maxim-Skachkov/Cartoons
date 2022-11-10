from django.db import models
from . import utils

# Create your models here.


class Actor(utils.CommonFields):
    photo = models.ImageField(upload_to='actors/', blank=True)


class Screenshot(utils.CommonFields):
    image = models.ImageField(upload_to='screenshots/')


class Episode(utils.CommonFields):
    episode_number = models.PositiveSmallIntegerField()
    season_number = models.PositiveSmallIntegerField()
    episode_url = models.URLField()


class CartoonCategory(utils.CommonFields):
    pass


class Cartoon(utils.CommonFields):
    tagline = models.CharField('слоган мультика', max_length=100)
    year = models.PositiveSmallIntegerField('год выпуска')
    number_of_episodes = models.PositiveSmallIntegerField('количество серий')
    poster = models.ImageField(upload_to='posters/')
    country = models.CharField('Страна производитель', max_length=50)
    actors = models.ManyToManyField(Actor)
    screenshots = models.ForeignKey(Screenshot, on_delete=models.CASCADE)
    episodes = models.ForeignKey(Episode, on_delete=models.CASCADE)
    category = models.ForeignKey(CartoonCategory, on_delete=models.CASCADE)







    
