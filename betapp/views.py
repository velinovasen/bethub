from django.shortcuts import render

# Create your views here.


def index_view(request):
    if request.method == "GET":
        #context = {"all_regular_games": Game.objects.all()}
        return render(request, 'games/regular_games.html', {})
    else:
        pass