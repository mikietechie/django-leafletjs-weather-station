'''
Copyrights 2021
Work Done By Mike Zinyoni https://github.com/mikietechie
mzinyoni7@gmail.com (Do not spam please)
(Open to work)
'''

from django.test import TestCase
from app.models import User, Location
from django.shortcuts import reverse
import sys, os

# Create your tests here.
class GlobalTestCase(TestCase):
    
    def setUp(self):
        self.user = User(
            username="mike",
            email="mzinyoni7@gmail.com",
        )
        self.user.set_password("12345678")
        self.user.save()
        self.client.force_login(self.user)
        self.loc1 = Location(**{
            "title": "Fairbury",
            "latitude": 39.300299,
            "longitude": -94.833984,
        })
        self.loc2 = Location(**{
            "title": "Cambridge",
            "latitude": 40.258569,
            "longitude": -100.167847
        })
        self.loc3 = Location(**{
            "title": "Russel",
            "latitude": 38.873929,
            "longitude": -98.827515,
        })
    
    ''' Test Models '''
    def test_user_model(self):
        self.assertIsInstance(self.user, User)
    
    def test_location_model(self):
        self.loc1.save()
        self.loc2.save()
        self.loc3.save()
        self.assertIsInstance(self.loc1, Location)
        #   check count
        self.assertEqual(Location.objects.count(), 3)
        #   Now test the auto creation of the other fields grid_x/_y/_id data
        self.assertIsNotNone(self.loc1.grid_id)
    
    def test_location_str(self):
        self.assertIn(self.loc1.title, str(self.loc1))
    
    def test_location_weather(self):
        self.loc1.save()
        self.assertIsInstance(self.loc1.weather, dict)
    
    def test_location_weather_now(self):
        self.loc1.save()
        self.assertIsInstance(self.loc1.weather_now, dict)
        
    ''' Test views '''
    def test_404_view(self):
        response = self.client.get("/non-existent-path")
        self.assertLess(response.status_code, 400)
        self.assertTrue("404" in str(response.content))
    
    def test_index_view_with_no_locations(self):
        Location.objects.all().delete()
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_index_view(self):
        self.loc1.save()
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    ''' Test management commands '''
    def test_setup(self):
        python = sys.argv[0]
        print(f"{python} manage.py setup")
        exit_code = os.system(f'"{python}" setup')
        self.assertFalse(bool(exit_code), msg="Most probably works on Windows OS Only!!!")
    
    
    
        
