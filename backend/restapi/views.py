from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET'])
def ship_list(request):
    """
        List ships
    """
    if request.method == 'GET':
        ships = Ships.objects.all()
        serializer = ShipsSerializer(ships, context={'request': request}, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def ship_position(request, imo):
    """
        Get Ship Position
    """
    if request.method == 'GET':
        try:
            positions = Positions.objects.filter(imo=imo).order_by('-time')
        except Positions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)
