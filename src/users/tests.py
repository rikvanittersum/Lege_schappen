from django.contrib.auth import get_user_model
from django.test import TestCase

class UserTester(TestCase):
    def setup(self):
        User = get_user_model()
        User.objects.create_user(**self.gegevens)

    def test_login(self):
        response = self.client.post('/login/', self.gegevens, follow=True)
        self.assertTrue(response.context['user'].is_active)