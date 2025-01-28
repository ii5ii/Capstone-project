from django.test import TestCase
from Restaurant.models import MenuItem

class MenuTest(TestCase):
    """Test if MenuItem can be created and its string representation is correct"""
    def test_create_menu_item(self):
        item = MenuItem.objects.create(title="Ice cream", price=6, inventory=10)
        self.assertEqual(str(item), "Ice cream : 6")