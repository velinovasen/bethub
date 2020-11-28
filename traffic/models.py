from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
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
    date = models.DateField()
    time = models.TimeField()
    home_team = models.CharField(max_length=40)
    away_team = models.CharField(max_length=40)
    score = models.CharField(max_length=7, default='-')
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()
    added_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.date} {self.time} {self.home_team} - {self.away_team} ' \
               f'{self.home_odd} {self.draw_odd} {self.away_odd} - {self.added_timestamp}'


class ResultGame(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.TimeField()
    home_team = models.CharField(max_length=40)
    away_team = models.CharField(max_length=40)
    score = models.CharField(max_length=7)
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()

    def __str__(self):
        return f'{self.id} {self.time} {self.home_team} - {self.away_team} {self.score} ' \
               f'{self.home_odd} {self.draw_odd} {self.away_odd}'


class TrendModel(models.Model):
    id = models.AutoField(primary_key=True)
    trend_1 = models.CharField(max_length=500, blank=True, null=True)
    trend_2 = models.CharField(max_length=500, blank=True, null=True)
    trend_3 = models.CharField(max_length=500, blank=True, null=True)
    trend_4 = models.CharField(max_length=500, blank=True, null=True)
    trend_5 = models.CharField(max_length=500, blank=True, null=True)
    trend_6 = models.CharField(max_length=500, blank=True, null=True)
    trend_7 = models.CharField(max_length=500, blank=True, null=True)
    trend_8 = models.CharField(max_length=500, blank=True, null=True)
    trend_9 = models.CharField(max_length=500, blank=True, null=True)
    trend_10 = models.CharField(max_length=500, blank=True, null=True)


class AppUser(models.Model):
    cash = models.DecimalField(validators=[MinValueValidator(0.00)],
                               max_digits=6, decimal_places=2)
    total_yield = models.FloatField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username