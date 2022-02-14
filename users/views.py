from numbers import Number
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from users.models import User
from .serializers import UserSerializer


@api_view(['GET'])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUser(request, id):
    try:
        user = User.objects.get(id=int(id))
        serializer = UserSerializer(user, many=False)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The User does not exist'}, status=404)
    user.delete()
    return Response(serializer.data)


@api_view(['PUT'])
def updateUser(request, id):
    try:
        user = User.objects.get(id=int(id))
    except User.DoesNotExist:
        return JsonResponse({'message': 'The User does not exist'}, status=404)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
