from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Explorer
from .serializers import ExplorerSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all(request):
    explorers = Explorer.objects.all()
    serializer = ExplorerSerializer(explorers, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def explorers(request):
    if request.method =='POST':
        serilizer = ExplorerSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save(user=request.user)
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        explorers = Explorer.objects.filter(user_id=request.user.id)
        serilizer = ExplorerSerializer(explorers, many=True)
        return Response(serilizer.data)
        







# class ExplorerList(APIView):

#     permission_classes = [AllowAny]

#     def get(self,request):
#         explorers = Explorer.objects.all()
#         serializer =  ExplorerSerializer(explorers, many=True)
#         return Response(serializer.data)

# Create your views here.
