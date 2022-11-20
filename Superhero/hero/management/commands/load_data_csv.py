from django.core.management.base import BaseCommand
import csv
from pathlib import Path
from hero.models import Superhero


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_data_csv()


def load_data_csv():
    # Delete the old objects
    Superhero.objects.all().delete()

    # Read the CSV file
    # path = Path('hero_objects.json')
    # if path.exists:
    #     objects = loads(path.read_text())

    # Read the CSV file
    with open("hero_objects.csv") as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip headers
        for row in reader:
            _, created = Superhero.objects.get_or_create(
                pk=row[0],
                investigator=row[1],
                created_at=row[2],
                last_updated_at=row[3],
                name=row[4],
                identity=row[5],
                description=row[6],
                image=row[7],
                strengths=row[8],
                weaknesses=row[9],
            )

    # # Create new objects
    # for o in objects:
    #     Superhero.objects.get_or_create(**o)

    # Show the objects
    for hero in Superhero.objects.all().values():
        print(hero)
    print("End of script")
