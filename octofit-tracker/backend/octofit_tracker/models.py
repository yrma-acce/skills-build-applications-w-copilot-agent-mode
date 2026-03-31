
from django.db import models
from djongo import models as djongo_models
from bson import ObjectId


class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = djongo_models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = djongo_models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.name} - {self.activity_type}"


class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = djongo_models.ManyToManyField(User, blank=True, related_name='suggested_workouts')

    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    team = djongo_models.OneToOneField(Team, on_delete=models.CASCADE, related_name='leaderboard')
    total_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Leaderboard for {self.team.name}"
