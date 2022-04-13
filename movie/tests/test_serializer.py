from django.test import TestCase

from movie.models.actor import Actor


class TestActorSerializer(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(name='Jaloliddin', birthdate='2000-10-18', gender='male')
    
    def test_data(self):
        response = self.client.get('/actors/')
        data = response.data
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['name'], 'Jaloliddin')
        self.assertEquals(data[0]['gender'], 'male')