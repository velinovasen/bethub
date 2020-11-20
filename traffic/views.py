from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import BetsVolume, Prediction, ValueBet, RegularGame, ResultGame
from .forms import UserRegisterForm


# Create your views here.


def landing_view(request):
    return render(request, 'games/landing_page.html')


def traffic_volume(request):
    all_bets = BetsVolume.objects.all()
    context = {"all_traffic_bets": all_bets}
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


def results_view(request):
    context = {"all_regular_games": ResultGame.objects.all()}
    return render(request, 'games/results.html', context)


def register_user(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registration successful for {username}! Login to continue')
            return redirect('login')
        return render(request, 'users/registration_page.html', {"form": form})
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration_page.html', {"form": form})


@login_required()
def profile_view(request):
    return render(request, 'users/profile.html', {})


def demo_view(request):
    form = UserCreationForm()
    context = {"form": form}
    return render(request, 'users/demo.html', context)
