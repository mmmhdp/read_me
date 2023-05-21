from django.db import models

GLOBAL_GENRES = [('fiction','non-fiction')]


class Author(models.Model):
    name = models.CharField(max_length = 200)
    second_n = models.CharField(max_length = 200)
    last_n = models.CharField(blank = True,
                              max_length = 200)
    alias = models.CharField(blank = True, 
                             max_length = 200)


class SubGenre(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 600, blank = True)


class PubInfo(models.Model):
    publisher = models.CharField(max_length = 200)
    year = models.IntegerField(blank = True, default = 0)


class Book(models.Model):
    title = models.CharField(max_length = 400)
    summary = models.TextField()
    global_genre = models.CharField(choices = GLOBAL_GENRES,
                                    default = "written",
                                    max_length = 100)
    
    sub_genre = models.ForeignKey(SubGenre,
                                  on_delete = models.SET("no info"),
                                  blank = True,
                                  related_name = "book")
    pub_info = models.ForeignKey(PubInfo,
                                 on_delete = models.SET("no info"),
                                 blank = True,
                                 related_name = "book")

    author = models.ManyToManyField(Author, related_name = "book")
  


class Note(models.Model):
    related_paper = models.OneToOneField(Book,
                                         on_delete = models.CASCADE,
                                         related_name = "note")
    review = models.TextField(blank = True)
    rate = models.IntegerField(blank = True, default = 0)
    created = models.DateTimeField(auto_now_add = True)
 
