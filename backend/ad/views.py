from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ad
from .serializers import AdSerializer

@api_view(['GET'])
def ads(request):
    ad = Ad.objects.all().order_by('-id')
    serializer = AdSerializer(ad, many=True)
    return Response(serializer.data)