from django.urls import path, include
from rest_framework import routers
from . import views


# ================== Create Routers  ================== #

router = routers.DefaultRouter()
# ================== All user Path Router  ================== #
router.register('users', views.AllUserViewSet)

# ================== Movies  Path Router  ================== #
router.register('movies', views.MovieViewSet)

# ================== Ratings Path Router  ================== #
router.register('ratings', views.RatingViewSet)



urlpatterns = [
    # ================== Routers Path  ================== #
    path('', include(router.urls)),

    # ================== Registation Path  ================== #
    path('register/', views.RegisterViewSet.as_view(), name='register'),

    # ================== Activation link Path  ================== #
    path('activate/<uid64>/<token>/', views.activate, name='activate'),

    # ================== Login Path  ================== #
     path('login/', views.UserLoginView.as_view(), name='login'),

    # ================== Logout Path  ================== #
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
