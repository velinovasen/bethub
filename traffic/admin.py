from django.contrib import admin

from traffic.models import Prediction, ValueBet, BetsVolume, RegularGame

# Register your models here.

admin.site.register(Prediction)
admin.site.register(ValueBet)
admin.site.register(BetsVolume)
admin.site.register(RegularGame)