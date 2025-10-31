import json
from django.core.management.base import BaseCommand
from tvshows.models import TVShow

class Command(BaseCommand):
    help = 'Import TV Shows from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        count = 0
        for item in data:
            try:
                TVShow.objects.create(
                    title=item.get('Title', ''),
                    year=item.get('Year', ''),
                    rating=item.get('Rating', ''),
                    votes=item.get('Votes', ''),
                    time=item.get('Time', ''),
                    genre=item.get('Genre', ''),
                    stars=item.get('Stars', ''),
                    short_story=item.get('short_story', '').strip()
                )
                count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Imported: {item.get("Title")}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error importing {item.get("Title")}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully imported {count} TV shows'))
