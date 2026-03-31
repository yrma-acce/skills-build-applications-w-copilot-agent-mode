from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.urls import reverse

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration_minutes=30, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Iron Man')

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Marvel')

    def test_activity_str(self):
        self.assertIn('Iron Man', str(self.activity))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Pushups')

    def test_leaderboard_str(self):
        self.assertIn('Marvel', str(self.leaderboard))

class APITests(TestCase):
    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.json())
