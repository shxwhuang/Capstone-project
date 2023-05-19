from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuView

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(id=1, title="IceCream", price=8, inventory=200)
        Menu.objects.create(id=2, title="Chocolate", price=18, inventory=300)
    
    def tearDown(self):
        pass

    def test_getall(self):
        pass