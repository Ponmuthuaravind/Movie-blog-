from django.db import models

# Create your models here.
class MovieModel(models.Model):
    title = models.CharField(max_length=100)
    story = models.TextField()
    review = models.TextField()
    relesed_on = models.DateField()
    reviewed_on = models.DateField()
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    poster = models.ImageField(upload_to='movies')

    def __str__(self):
        return self.title

class CommentsModel(models.Model):
    username = models.CharField(max_length=20)
    Comment = models.TextField()
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    command_date = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(to=MovieModel,on_delete=models.CASCADE)
