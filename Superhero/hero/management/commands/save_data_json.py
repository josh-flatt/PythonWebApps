from json import dump
from django.core.management.base import BaseCommand

from hero.models import Superhero

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        save_data_json()

def save_data_json():
    # print(Superhero.objects.all().values())

    # for hero in Superhero.objects.all().values():
    #     print(hero)

    data = [b for b in Superhero.objects.all().values()]

    with open('hero_objects.json', "w") as f:
        dump(data, f, indent = 4, default=str)
