from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

class Result(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    bot_move = models.CharField(max_length=10)
    user_move = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    series = models.BooleanField(default=False)

