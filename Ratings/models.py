from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.utils import timezone

# =============== Create Model For Account ============= #
class account_Model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=250,null=True, blank=True)

    def __str__(self):
        return self.name


# =============== Create Model For Movie ============= #
class movie_Model(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    release_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    
  # ===== Calculate the average Ratings ====== #
    def average_rating(self):
        return self.ratings.aggregate(Avg('rating'))['rating__avg']


# =============== Create the Ratings Model ============= #
class rating_Model(models.Model):
    user_id = models.ForeignKey(account_Model, on_delete=models.CASCADE,related_name='ratings')
    movie_id = models.ForeignKey(movie_Model, on_delete=models.CASCADE,related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.user_id.name} rated {self.movie_id.name} {self.rating}"