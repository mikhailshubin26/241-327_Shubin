from rest_framework import serializers
from .models import MusicMedia

class MusicMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicMedia
        fields = '__all__'