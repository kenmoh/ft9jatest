from django.urls import path
from .views import index, user_trades

urlpatterns = [

    path('', index, name='traders'),
    path('trades/<int:id>', user_trades, name='traders'),

]
