import requests
import json


class DiscordLogin:

    def login(self):
        response = self.client.get(url=f'{self.testdata["url"]}/login')
        assert response.ok

        login_data = {
            "captcha_key": "null",
            "gift_code_sku_id": "null",
            "login": self.testdata('username'),
            "login_source": "null",
            "password": self.testdata('password'),
            "undelete": "false"
        }

        repsponse = self.client.post(url=f'{self.testdata["url"]}/login', data=login_data)
        assert response.ok
