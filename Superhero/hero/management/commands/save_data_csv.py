import csv
from django.http import HttpResponse
from django.core.management.base import BaseCommand

from hero.models import Superhero

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        save_data_csv()

def save_data_csv():
    # print(Superhero.objects.all().values())
    
    # Get all data from superhero DB table
    heroes = Superhero.objects.all()
    
    # Create HTTpResponse Object with the appropriate CSV header.
    # response = HttpResponse(content_type="text/csv")
    # response["Content-Disposition"] = 'attachment; filename="hero_objects.csv"'
    
    with open('hero_objects.csv', "w") as outfile:
        f = csv.writer(outfile, delimiter=",", lineterminator="\n")
        f.writerow(['pk', 'investigator', 'created_at', 'last_updated_at', 'name', 'identity', 'description', 'image', 'strengths', 'weaknesses'])
    
        for hero in heroes:
            f.writerow([hero.pk, hero.investigator, hero.created_at, hero.last_updated_at, hero.name, hero.identity, hero.description, hero.image, hero.strengths, hero.weaknesses])