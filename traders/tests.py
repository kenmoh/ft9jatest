from django.test import TestCase
from django.urls import reverse

from django.test import TestCase
from traders.models import User, Trade


class TradersAppTests(TestCase):
    def setUp(self):
        # Create some test users
        self.trader1 = User.objects.create(username='trader1', balance=100.0)
        self.trader2 = User.objects.create(username='trader2', balance=100.0)

        # Create some test trades for Trader1
        Trade.objects.create(user=self.trader1, profit_or_loss=10.0)
        Trade.objects.create(user=self.trader1, profit_or_loss=-5.0)
        Trade.objects.create(user=self.trader1, profit_or_loss=8.0)

    def test_get_all_users(self):

        # Retrieve all traders from the database
        all_traders = User.objects.all()

        # Ensure there are two traders in the database
        self.assertEqual(all_traders.count(), 2)

    def test_get_trades_by_user(self):

        # Retrieve all trades for trader1 from the database
        response = self.client.get(
            reverse('traders', args=[self.trader1.id]))
        self.assertEqual(response.status_code, 200)
