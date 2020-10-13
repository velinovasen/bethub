from django.shortcuts import render
from django.http import HttpResponse
from .models import BetsVolume

# Create your views here.


def index(request):
    all_bets = BetsVolume.objects.all()
    context = {"all_bets": all_bets}
    return render(request, 'games/bets_volume.html', context)