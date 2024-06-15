from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Saved
from .serializers import SavedSerializer, SavedCreateSerializer


class SavedProductApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        saveds = Saved.objects.filter(user=request.user)
        serializer = SavedSerializer(saveds, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SavedCreateSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)