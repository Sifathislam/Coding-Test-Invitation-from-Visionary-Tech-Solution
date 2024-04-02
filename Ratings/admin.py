from django.contrib import admin
from .models import movie_Model, rating_Model,account_Model

#====== register account_Model Model for admin pannel === #
admin.site.register(account_Model)

#====== register movie Model for admin pannel === #
admin.site.register(movie_Model)


#====== register rating Model for admin pannel === #
admin.site.register(rating_Model)
