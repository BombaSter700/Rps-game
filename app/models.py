from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    '''Player moder'''
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')

    def __str__(self):
        return self.name
    
class Result(models.Model):
    '''Resul model in which all player will be stored'''
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name='score')
    bot_move = models.CharField(max_length=50, blank=True)
    user_move = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return 'Status -- ' + self.status + ' ' + self.player.name
