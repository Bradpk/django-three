from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, RandomSerializer
from .models import Random


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]

class RandomViewSet(viewsets.ModelViewSet):
     queryset = Random.objects.all()
     serializer_class = RandomSerializer

#------------------------------------------------

def random_list(request):
    random_stuff = Random.objects.select_related().all()
    data = []

    for item in random_stuff:
        data.append({
            'one': item.one,
            'two': item.two,
            'three': item.three,
        })

    return JsonResponse(data, safe=False)









# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def indextwo(request):
#     return HttpResponse("Lord Sauron Is Here")