from django.db import models

"""
A Collectible is a Djinni or Summon Tablet found in-game. They are divided by game, by collectable type (coltype), and by chapter.
"""
class Collectible(models.Model):
    name = models.CharField(
        max_length=20
    )

    game = models.SmallIntegerField()

    coltype = models.SmallIntegerField()

    chapter = models.SmallIntegerField()

    location = models.CharField(
        max_length=100
    )

    description = models.TextField()

    picture_url = models.CharField(
        max_length=100
    )

    def get_picture_url(self):
        return '/assets/' + self.picture_url

    def __str__(self):
        return f"{self.name} ({self.coltype}, {self.chapter}, {self.get_picture_url()}) - {self.game} @ {self.location}: {self.description}"

    def serialize(self):
        return {
            "name": self.name,
            "game": self.game,
            "coltype": self.coltype,
            "chapter": self.chapter,
            "location": self.location,
            "description": self.description,
            "pic_url": self.get_picture_url()
        }

"""
A Category is a grouping of Collectables based on shared properties (game, coltype, chapter). This is all represented in the "query" parameter.

Categories are used for Selection Lists to determine the types of URL queries React should send to Django.
"""
class Category(models.Model):
    game = models.CharField(max_length=20)
    query = models.CharField(max_length=50)
    label = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.label} -> {self.query} @ {self.game}"

    def serialize(self):
        return {
            "game": self.game,
            "query": self.query,
            "label": self.label
        }