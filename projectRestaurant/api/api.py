from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import LocalSerializer
from api.models import Local

@api_view(['GET'])
def local_api_view(request):

    if request.method == 'GET':
        locals =Local.objects.all()
        locals_serializer = LocalSerializer(locals, many=True)
        return Response(locals_serializer.data,status = status.HTTP_200_OK)