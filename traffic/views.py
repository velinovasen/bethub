from django.shortcuts import render
from django.http import HttpResponse
from .models import BetsVolume, Prediction, ValueBet, RegularGame

# Create your views here.


def landing_view(request):
    return render(request, 'games/landing_page.html')


def traffic_volume(request):
    all_bets = BetsVolume.objects.all()
    context = {"all_bets": all_bets}
    return render(request, 'games/bets_volume.html', context)


def predictions(request):
    all_predictions = Prediction.objects.all()
    context = {"all_predictions": all_predictions}
    return render(request, 'games/predictions.html', context)


def valuebets(request):
    all_valuebets = ValueBet.objects.all()
    context = {"all_valuebets": all_valuebets}
    return render(request, 'games/valuebets.html', context)


def regular_games(request):
    context = {"all_regular_games": RegularGame.objects.all()}
    return render(request, 'games/regular_games.html', context)
