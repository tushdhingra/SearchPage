from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView, Response, status
from django.http import HttpResponse
from .models import profile
from rest_framework import viewsets
from .serializers import profileSerializer

class profile_API(APIView):
    def get(self, request):
        profile_r = profile.objects.all()
        serializer = profileSerializer(profile_r, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def index(request):
	queryset = profile.objects.all()
	context = {
        'profile': queryset
    }
	return render(request, 'SearchApp/index.html',context)

def searchbar(request):
	search=request.GET['search']
	specific = profile.objects.filter(name__contains=search)
	return render(request,'SearchApp/searchbar.html',{'post':specific})