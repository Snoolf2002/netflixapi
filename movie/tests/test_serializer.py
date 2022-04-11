from django.test import TestCase

from movie.models.actor import Actor


class TestActorSerializer(TestCase):
    def setUp(self):
        self.artist = Actor.objects.all()
    
    def test_data(self):
        pass