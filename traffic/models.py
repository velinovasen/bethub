from django.db import models

# Create your models here.


class BetsVolume(models.Model):
    day = models.CharField(max_length=15)
    time = models.TimeField()
    home_team = models.CharField(max_length=60)
    away_team = models.CharField(max_length=60)
    final_bet = models.CharField(max_length=1)
    odds = models.FloatField()
    amount = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.home_team} - {self.away_team} - ' \
               f'{self.final_bet} - {self.odds} - {self.amount}'
