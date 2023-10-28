from decimal import Decimal
from rest_framework import generics
from .serializer import TradeSerializer
from django.shortcuts import render, get_object_or_404
import plotly.express as px
from .models import Trade, User

# REST API (OPTIONAL)
# class TradeListUserView(generics.ListAPIView):
#     serializer_class = TradeSerializer

#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         return Trade.objects.filter(user_id=user_id)


# class TradeListView(generics.ListAPIView):

#     serializer_class = TradeSerializer
#     queryset = Trade.objects.all()


def index(request):
    """
    Get all users(traders) from database
    """
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, 'traders/traders.html', context)


def user_trades(request, id):
    """
    User dashboard route. It display the user profit or loss, graph
    """
    # Get user by id
    user = get_object_or_404(User, pk=id)

    # Get trades of a single user
    trades = Trade.objects.filter(user=user).order_by('timestamp')

    # Plot line graph base on trades values (profit_or_loss and timestamp)
    fig = px.line(
        x=[trade.timestamp for trade in trades],
        y=[Decimal(trade.profit_or_loss) for trade in trades],
        title="Trade Chart",
        labels={'x': 'Timestamp', 'y': 'Profit/Loss'}
    )

    # Render chart in html
    chart = fig.to_html()

    # Total Profit/Loss of a user trade
    profit = Decimal(user.balance) - 100
    loss = 100 - Decimal(user.balance)

    context = {
        "chart": chart,
        "balance": Decimal(user.balance),
        "user": user.username,
        "profit": profit,
        "loss": loss,

    }
    return render(request, 'traders/user_trades.html', context)
