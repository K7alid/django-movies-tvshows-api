import json
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Import Movies from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        count = 0
        for item in data:
            try:
                Movie.objects.create(
                    title=item.get('Title', ''),
                    year=int(item.get('Year', 0)),
                    rated=item.get('Rated', ''),
                    released=item.get('Released', ''),
                    runtime=item.get('Runtime', ''),
                    genre=item.get('Genre', ''),
                    director=item.get('Director', ''),
                    writer=item.get('Writer', ''),
                    actors=item.get('Actors', ''),
                    plot=item.get('Plot', ''),
                    language=item.get('Language', ''),
                    country=item.get('Country', ''),
                    awards=item.get('Awards', ''),
                    poster=item.get('Poster', ''),
                    metascore=int(item.get('Metascore', 0)) if item.get('Metascore') else None,
                    imdb_rating=item.get('imdbRating', ''),
                    imdb_votes=item.get('imdbVotes', ''),
                    imdb_id=item.get('imdbID', ''),
                    images=item.get('Images', [])
                )
                count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Imported: {item.get("Title")}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error importing {item.get("Title")}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully imported {count} movies'))
