from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
