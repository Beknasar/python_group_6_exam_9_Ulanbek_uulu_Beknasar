from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View
import json
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

# from api_v1.permissions import GETModelPermissions
# from api_v1.serializers import ProductSerializer, UserSerializer, OrderSerializer
from webapp.models import Photo, Chosen


@ ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class ChosenAddView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request, *args, **kwargs):
        print(kwargs.get('pk'))
        photo = get_object_or_404(Photo, pk=kwargs['pk'])
        if request.user not in photo.chosens.all():
            Chosen.objects.add(user=request.user, image=photo)
            return HttpResponse('Good job!')
        else:
            return HttpResponse(status=400)



class ChoosenRemoveView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs['pk'])
        if request.user in photo.chosens.all():
            ch = Chosen.objects.get(user=request.user, image=photo)
            ch.delete()
            return HttpResponse('Работает')
        else:
            return HttpResponse(status=400)