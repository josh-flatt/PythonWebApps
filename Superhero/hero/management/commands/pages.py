from django.core.management.base import BaseCommand
from requests import get


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        response = get('https://www.google.com/')
        print(response)
        msg = f'Google: {len(response.text)} characters'
        print(msg)
