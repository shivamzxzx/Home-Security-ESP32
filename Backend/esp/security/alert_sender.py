import requests


class Alert:
    def __init__(self, auth_key, receivers_numbers, msg):
        self.auth_key = auth_key
        self.receivers_numbers = receivers_numbers
        self.msg = msg

    def send_sms(self):
        receivers_numbers = ','.join(self.receivers_numbers)
        url = "https://www.fast2sms.com/dev/bulk"
        payload = f'sender_id=FSTSMS&message={self.msg}&language=english&route=p&numbers={receivers_numbers}'
        headers = {
            'authorization': self.auth_key,
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        return response
