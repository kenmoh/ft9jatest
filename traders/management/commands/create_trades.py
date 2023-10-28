from typing import Any
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from traders.models import Trade, User


class Command(BaseCommand):

    """
    This management command generate 25 trades for each user in the database
    """
    number_of_traders = 10
    number_of_data_points = 25

    help = "Generate random Trades for 10 users(traders)"

    # Helper function to generate random profit or loss
    def genetaye_random_profit_or_loss(self):
        return round(random.uniform(-10, 10), 2)

    def handle(self, *args: Any, **options: Any):
        users = User.objects.all()

        # Get start time and interval for the timestamp
        start_time = timezone.now() - timezone.timedelta(minutes=self.number_of_data_points)
        interval = timezone.timedelta(minutes=1)

        for user in users:
            for data_point in range(self.number_of_data_points):
                timestamp = start_time + data_point * interval
                profit_or_loss = self.genetaye_random_profit_or_loss()
                trade = Trade(user=user, timestamp=timestamp,
                              profit_or_loss=profit_or_loss)

                trade.save()

                # Update user balance base on profit or loss
                user.balance = Decimal(user.balance) + \
                    Decimal(trade.profit_or_loss)
                user.save()

                self.stdout.write(self.style.SUCCESS(
                    f'Successfully created trades for existing {trade.user} @ {trade.timestamp}'))
