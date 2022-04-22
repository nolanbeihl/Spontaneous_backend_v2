from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Explorer
from .serializers import ExplorerSerializer
from django.contrib.auth.models import User

class ExplorerList(APIView):

    permission_classes = [AllowAny]

    def get(self,request):
        explorers = Explorer.objects.all()
        serializer =  ExplorerSerializer(explorers, many=True)
        return Response(serializer.data)

# Create your views here.
