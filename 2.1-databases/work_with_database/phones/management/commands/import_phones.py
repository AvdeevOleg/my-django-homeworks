import csv
import os
from django.core.management.base import BaseCommand
from django.core.files import File
from phones.models import Phone
from django.utils.text import slugify

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', 'r', newline='', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            for phone in phones:
                image_path = os.path.join('static', 'phones', phone['image'])
                with open(image_path, 'rb') as img_file:
                    phone_obj, created = Phone.objects.get_or_create(
                        id=phone['id'],
                        defaults={
                            'name': phone['name'],
                            'price': phone['price'],
                            'image': File(img_file),
                            'release_date': phone['release_date'],
                            'lte_exists': phone['lte_exists'],
                            'slug': slugify(phone['name']),
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Successfully imported {phone_obj.name}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'{phone_obj.name} already exists'))


