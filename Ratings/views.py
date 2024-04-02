# ============== Import all important files and packeges =========================  #
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from . import models
from . import serializers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from rest_framework.response import Response
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# ============== Create Registation Viewset With Auth Token Varification System  =========================  #
class RegisterViewSet(APIView):
    serializer_class = serializers.RegistrationSerializer
    #======== Create the token and Send Via Email  =============== #   
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/activate/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link':confirm_link})

            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response("Check your email to confirm registration.")
        return Response(serializer.errors)
    


# ============== Activate Funtion for After Click The Email Varification Mail  =========================  #   
def activate(request, uid64, token):
    try:
    # ========= Decode the uid  =========== #   
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # ========= Activate the user after confirm  =========== #   
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

    # ========= Redirect to login page after activation  =========== #   
        return redirect('login')

    else:
    # ========= Redirect to register page if activation fails  =========== #   
        return redirect('register')
   


# ============================ Viewsets For Login  =========================  #   
class UserLoginView(APIView):
    def post(self,request):
        serializer = serializers.userLoginSerializer(data=self.request.data)

    # ========= Validate data  =========== #   
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username = username, password = password)

            if user: 
                token,_ = Token.objects.get_or_create(user = user)
                login(request,user)

                return  Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': "InValid Credential"})
        return Response(serializer.errors)



# ============================ Viewsets For Logout  =========================  #   
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
    

# ============================ Viewsets For All User  =========================  #   
class AllUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.AllUserSerializer


# ============================  Viewsets For Movie Pagination  =========================  #   
class MoviesPagination(pagination.PageNumberPagination):
    page_size = 10 # items per page
    page_size_query_param = page_size
    max_page_size = 100

# ============================  Viewsets For Movie  =========================  #   
class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.movie_Model.objects.all()
    serializer_class = serializers.MovieSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = MoviesPagination
    search_fields = ['name','genre','rating','release_date']

# ============================ Viewsets For Ratings  =========================  #   
class RatingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.rating_Model.objects.all()
    serializer_class = serializers.RatingSerializer