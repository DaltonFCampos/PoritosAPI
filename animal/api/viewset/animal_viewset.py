from rest_framework import viewsets

from animal.api.serializers.animal_serializer import AnimalSerializer
from animal.models.animal import Animal

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
