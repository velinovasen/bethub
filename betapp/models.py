from django.db import models

# Create your models here.


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    home_team = models.CharField(max_length=40)
    away_team = models.CharField(max_length=40)
    score = models.CharField(max_length=7, default='-')
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()
    added_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.time} {self.home_team} - {self.away_team} ' \
               f'{self.home_odd} {self.draw_odd} {self.away_odd} - {self.added_timestamp}'
