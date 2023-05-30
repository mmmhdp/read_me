from django.db import models

GLOBAL_GENRES = [('fiction', 'fiction'), ('non-fiction', 'non-fiction')]


class Author(models.Model):
    name = models.CharField(blank=True,
                            max_length=200)
    second_n = models.CharField(blank=True,
                                max_length=200)
    last_n = models.CharField(blank=True,
                              max_length=200)
    alias = models.CharField(blank=True,
                             max_length=200)

    def __str__(self):
        return f"{self.name} {self.second_n}"


class SubGenre(models.Model):
    name = models.CharField(blank=True, max_length=200)
    description = models.CharField(max_length=600, blank=True)

    def __str__(self):
        return f"{self.name}"


class PubInfo(models.Model):
    publisher = models.CharField(blank=True, max_length=200)
    year = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f"{self.publisher} {self.year}"


class Book(models.Model):
    title = models.CharField(max_length=400)
    summary = models.TextField()
    global_genre = models.CharField(choices=GLOBAL_GENRES,
                                    default="written",
                                    max_length=100)

    sub_genre = models.ForeignKey(SubGenre,
                                  on_delete=models.SET("no info"),
                                  blank=True,
                                  related_name="book")

    pub_info = models.ForeignKey(PubInfo,
                                 on_delete=models.SET("no info"),
                                 blank=True,
                                 related_name="book")

    author = models.ManyToManyField(Author, related_name="book")

    def __str__(self):
        return f"{self.title}"


class Note(models.Model):
    related_paper = models.OneToOneField(Book,
                                         on_delete=models.CASCADE,
                                         related_name="note")
    review = models.TextField(blank=True)
    rate = models.IntegerField(blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', related_name='note', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.related_paper}"
