from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Skipping deletion; only insert fresh test data

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body workout')
        running = Workout.objects.create(name='Running', description='Cardio workout')
        pushups.suggested_for.set([ironman, batman])
        running.suggested_for.set([captain, superman])

        # Create Activities
        Activity.objects.create(user=ironman, activity_type='Pushups', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=batman, activity_type='Running', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=superman, activity_type='Pushups', duration_minutes=20, date=timezone.now().date())
        Activity.objects.create(user=captain, activity_type='Running', duration_minutes=25, date=timezone.now().date())

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=100)
        Leaderboard.objects.create(team=dc, total_points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
