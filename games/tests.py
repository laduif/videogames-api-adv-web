from django.test import TestCase
from rest_framework.test import APIClient
from .models import Game

class GameAPItest(TestCase):
    def setUp(self):

        self.client = APIClient()

    # unit test 1 - testing whether the API returns a list of all the games in the database
    def test_get_all_games(self):
        
        response = self.client.get("/games/")

        self.assertEqual(response.status_code, 200)

    # unit test 2 - testing adding a game to the database
    def test_add_game(self):
        data = {
            "name": "Test game",
            "platform": "PC",
            "genre": "Action",
            "publisher": "Test publisher",
            "release_year": 2026,
            "na_sales": 10.25,
            "eu_sales": 5.30,
            "jp_sales": 1.20,
            "other_sales": 0.90,
            "global_sales": 15.15
        }

        response = self.client.post("/games/add/", data, format="json")

        print(response.data)
        
        self.assertEqual(response.status_code, 201)

    # unit test 3 - testing invalid year is validated
    def test_invalid_release_year(self):
        data = {
            "name": "Test game",
            "platform": "PC",
            "genre": "Action",
            "publisher": "Test Publisher",
            "release_year": 1970,
            "na_sales": 10.25,
            "eu_sales": 5.30,
            "jp_sales": 1.20,
            "other_sales": 0.90,
            "global_sales": 15.15
        }

        response = self.client.post("/games/add/", data, format="json")

        self.assertEqual(response.status_code, 400)

    # unit test 4 - testing filtering by genre
    def test_games_by_genre(self):

        Game.objects.create(
            name="Dark Souls 3",
            platform="PC",
            genre="ARPG",
            publisher="FromSoftware",
            release_year=2016,
            na_sales=10,
            eu_sales=5,
            jp_sales=1,
            other_sales=2,
            global_sales=18
        )

        response = self.client.get("/games/genre/ARPG/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["genre"], "ARPG")

    # unit test 5 - testing filtering by platform works
    def test_games_by_platform(self):

        Game.objects.create(
            name="God of War",
            platform="PS2",
            genre="Action",
            publisher="Sony",
            release_year=2005,
            na_sales=8,
            eu_sales=7,
            jp_sales=2,
            other_sales=1,
            global_sales=18
        )

        response = self.client.get("/games/platform/PS2/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["platform"], "PS2")