from django.test import TestCase
from django.test import Client

client = Client()


# Create your tests here.
class FakeTest(TestCase):
    def test_dummy_test(self):
        response = self.client.get("/polls/")
        self.assertEqual(response.status_code, 200)
