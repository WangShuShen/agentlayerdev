"""
test api
"""
import os
from dotenv import load_dotenv
import json
from django.test import TestCase, Client

load_dotenv()
data_mgt_host_ip = os.environ.get('DATA_MGT_HOST_IP')
data_mgt_port = os.environ.get('DATA_MGT_PORT')
data_mgt_version = os.environ.get('DATA_MGT_VERSION')

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
            path=f"http://{data_mgt_host_ip}:{data_mgt_port}/api/{data_mgt_version}/central_layer_data_mgt/AppMetadataManager/save_application_metadata",
            data=json.dumps({'test': '123', "test2": "1234"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)