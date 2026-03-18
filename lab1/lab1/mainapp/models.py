from django.db import models

class MusicMedia(models.Model):
    MEDIA_TYPES = [
        ('vinyl', 'Vinyl'),
        ('cd', 'CD'),
        ('cassete', 'Cassete'),
    ]

    title = models.CharField(max_length=255) # Название альбома
    artist = models.CharField(max_length=255)  # Исполнитель
    media_type = models.CharField(max_length=255, choices=MEDIA_TYPES) # Тип носителя
    release_year = models.IntegerField() # Год выпуска
    price = models.DecimalField(max_digits=6, decimal_places=2) # Цена
    is_available = models.BooleanField(default=True) # В наличии ли?
    created_at = models.DateTimeField(auto_now_add=True) # Дата добавления

    def __str__(self):
        return f"{self.artist} — {self.title} ({self.media_type})"