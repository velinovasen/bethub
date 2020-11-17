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


class Prediction(models.Model):
    date = models.DateField()
    time = models.TimeField()
    home_team = models.CharField(max_length=40)
    away_team = models.CharField(max_length=40)
    home_prob = models.IntegerField()
    draw_prob = models.IntegerField()
    away_prob = models.IntegerField()
    bet_sign = models.CharField(max_length=1)
    score_predict = models.CharField(max_length=10)
    avg_goals = models.FloatField()
    odds_for_prediction = models.FloatField()
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()
    temp = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.home_team} - {self.away_team} ' \
               f'{self.home_prob} {self.draw_prob} {self.away_prob} --- ' \
               f'{self.bet_sign}'


class ValueBet(models.Model):
    date = models.DateField()
    time = models.TimeField()
    home_team = models.CharField(max_length=40)
    away_team = models.CharField(max_length=40)
    home_prob = models.IntegerField()
    draw_prob = models.IntegerField()
    away_prob = models.IntegerField()
    bet_sign = models.CharField(max_length=1)
    odds_for_pred = models.FloatField()
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()
    value_percent = models.IntegerField()

    def __str__(self):
        return f'{self.home_team} {self.away_team} ' \
               f'{self.bet_sign} {self.odds_for_pred} ' \
               f'{self.value_percent}'


class RegularGame(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.TimeField()
    home_team = models.CharField(max_length=40)
    away_team = models.CharField(max_length=40)
    score = models.CharField(max_length=7, default='-')
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()

    def __str__(self):
        return f'{self.home_team} - {self.away_team} ' \
               f'{self.home_odd} {self.draw_odd} {self.away_odd}'


class ResultGame(models.Model):
    time = models.TimeField()
    home_team = models.CharField(max_length=40)
    away_team = models.CharField(max_length=40)
    score = models.CharField(max_length=7)
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()

    def __str__(self):
        return f'{self.home_team} - {self.away_team} {self.score} ' \
               f'{self.home_odd} {self.draw_odd} {self.away_odd}'
