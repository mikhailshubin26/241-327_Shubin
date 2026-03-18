import random
from decimal import Decimal
from django.db import transaction
from .models import MusicMedia

albums = [
    ("Россия 34", "Слава КПСС"),
    ("DAMN.", "Kendirck Lamar"),
    ("Корми своих демонов по расписанию", "pyrokinesis"),
    ("Не все дома", "Noize MC"),
    ("Любимые песни воображаемых людей", "Хаски"),
    ("Красота и уродство", "Oxxxymiron"),
    ("Монго", "Ежемесячные"),
    ("Short n' Sweet", "Sabrina Carpenter"),
    ("DON'T TAP THE GLASS", "Tyler, The Creator"),
    ("The Eminem Show", "Eminem"),
]

media_types = ['vinyl', 'cd', 'cassette']


def gentestdata():
    with transaction.atomic():
        for i in range(1000):
            title, artist = random.choice(albums)

            new_media = MusicMedia(
                title=title,
                artist=artist,
                media_type=random.choice(media_types),
                release_year=random.randint(1960, 2025),
                price=Decimal(str(round(random.uniform(300, 5000), 2))),
                is_available=random.choice([True, False]),
            )
            new_media.save()

    print('OK gentestdata()')