from django import models


class Election(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()


class Candidate(models.Model):
    election = models.ForeignKey(Election)
    name = models.CharField(max_length=250)
    score = models.IntegerField(default=0)
