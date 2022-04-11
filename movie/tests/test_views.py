from django.test import TestCase, Client

from movie.models import Movie



class TestMovieViewSet(TestCase):
    def setUp(self):
        self.movie1 = Movie.objects.create(title='Venom', year=2018, imdb='8.8')
        self.movie2 = Movie.objects.create(title='Halk', year=2022, imdb='9.0')
        self.client = Client()
        
    def test_get_all_movies(self):
        response = self.client.get('/movies/')
        data = response.data
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]['title'], 'Venom')
        self.assertEquals(data[1]['title'], 'Halk')
        
    def test_serach_movie(self):
        response = self.client.get('/movies/?search=Halk')
        data = response.data
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['title'], 'Halk')
        
    def test_order_by_imdb(self):
        response = self.client.get('/movies/?ordering=-imdb')
        data = response.data
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]['title'], 'Halk')
        self.assertEquals(data[1]['title'], 'Venom')
        
        
        