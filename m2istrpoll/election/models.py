from django.db import models


class Election(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.title


class Candidate(models.Model):
    election = models.ForeignKey(
        Election,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=250)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
