from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Restaurant.models import MenuItem
from Restaurant.serializers import MenuItemSerializer

class MenuViewTest(APITestCase):
    def setUp(self):
        """Setup initial data for the test database"""
        self.item1 = MenuItem.objects.create(title="Pizza", price=12.50, inventory=5)
        self.item2 = MenuItem.objects.create(title="Burger", price=8.99, inventory=20)

    def test_get_all_menu_items(self):
        """Test retrieving all menu items"""
        response = self.client.get(reverse('menu'))
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)