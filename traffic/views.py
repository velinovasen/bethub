from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import UserRegisterForm
from .models import BetsVolume, Prediction, ValueBet, RegularGame, ResultGame, AppUser


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


def demo_view(request):
    context = {"all_regular_games": ResultGame.objects.all()}
    return render(request, 'games/demo.html', context)


def results_view(request):
    context = {"all_regular_games": ResultGame.objects.all()}
    return render(request, 'games/results.html', context)


def check_if_exists(username):
    return User.objects.filter(username=username).exists()


class RegisterView(FormView):
    def test_func(self):
        return not self.request.user.is_authenticated

    template_name = 'registration_page.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        #ADD AppUser as well
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        
        messages = []
        flag = True
        
        if check_if_exists(username):
            messages.append("User already exists!!!")
            flag = False
        if password != confirm_password:
            messages.append(("Passwords don't match!!!"))
            flag = False
            
        if flag:
            user = User.objects.create_user(username=username, password=password, email=email)

            AppUser.objects.create(user=user, tokens=200, total_yield=0)
        
        else:
            form = UserRegisterForm()
            context = {"messages": messages, "form": form}
            return render(self.request, "registration_page.html", context)
        return super(RegisterView, self).form_valid(form)