from django.shortcuts import render
from students.serializers import UserSerializer
from rest_framework import generics
from students.models import User

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    print(queryset)
    print('this is the main branch do nothing here ')
    print("this is the third commit")
    print("This is the main branch change")

