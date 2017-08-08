from django.apps import AppConfig
from scrapinghub import ScrapinghubClient


test = None
class UserManagementConfig(AppConfig):
    name = 'User_Management'

    def ready(self):
        global test
        apikey = '88133cc793ab4296b56db8a87eaae1ec'
        client = ScrapinghubClient(apikey)
        test = client.get_job('223795/1/3')
        test = sorted(test.items.list(), key=lambda k: k['score'], reverse=True)


