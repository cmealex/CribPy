from django.db import models

# Create your models here.

class Rooms(models.Model): # table name

    room = models.CharField(max_length=100, blank=False)  # column name
    furniture = models.CharField(max_length=100, blank=False)  # column name
    drawer_section = models.CharField(max_length=100)  # column name
    item_name = models.CharField(max_length=100, blank=False)  # column name
    item_description = models.CharField(max_length=200, default='')  # column name
    item_count = models.IntegerField()
    comments = models.CharField(max_length=200)  # column name

    def __str__(self):
        return 'Room: {0}, furniture: {1}, section: {2}, item_name: {3}, item_count: {4}'.format(self.room,
                                                                                                 self.furniture,
                                                                                                 self.drawer_section,
                                                                                                 self.item_name,
                                                                                                 self.item_count)
