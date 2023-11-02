"""
test api
"""
import json
from django.test import TestCase, Client

# Create your tests here.
class ActorTest(TestCase):
    """
    test actor
    """

    def setUp(self):
        """
        intial unit test request
        """
        self.client = Client()

    def test_decorator(self):
        """
        pass
        """
        response = self.client.post(
            path="http://140.118.122.148:30302/api/data_mgt/app_metadata_manager/save_application_metadata",
            data=json.dumps({'test': '123', "test2": "1234"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)