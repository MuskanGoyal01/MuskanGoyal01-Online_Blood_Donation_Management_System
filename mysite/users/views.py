from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegistrationSerializer


@api_view(["POST"])
def Register_Users(request):
    print(request.data)
    serializer = RegistrationSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)

