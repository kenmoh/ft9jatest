from django.urls import path
from .views import TradeListView, TradeListUserView, index, user_trades

urlpatterns = [
    # path('', TradeListView.as_view(), name='user-trades'),
    path('', index, name='traders'),
    path('trades/<int:id>', user_trades, name='traders'),
    path('api/trades/', TradeListView.as_view(), name='user-trades'),
    path('api/trades/<int:user_id>/',
         TradeListUserView.as_view(), name='user-trades'),
]
