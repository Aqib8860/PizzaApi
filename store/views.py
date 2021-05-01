from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from core.models import User
from core.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


# Create your views here.

# ADD VIEW DELETE TOPPING VIEW USING HYPERLINK MODEL SERIALIZER
class ToppingsViewSet(viewsets.ModelViewSet):
    queryset = Toppings.objects.all()
    serializer_class = ToppingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"USER_DOES_NOT_EXIST": "Please create account first using rest-auth/registration"}, status=400)

        topping = Toppings.objects.filter(user=self.request.user, name=self.request.data['name'])
        if topping.exists():
            return Response({"error": "Already Exist"}, status=400)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer = self.perform_create(serializer.save(user=self.request.user))
            return Response({"msg": "Successfully Added"}, status=200)


class CreatePizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = CreatePizzaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"USER_DOES_NOT_EXIST": "Please create account first using rest-auth/registration"}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=self.request.user))
        return Response({"msg": "Successfully Created"}, status=200)


class EditPizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = EditPizzaSerializer
    permission_classes = [permissions.IsAuthenticated]


class ViewAllPizzaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = ViewPizzaSerializer
    # permission_classes = [permissions.IsAuthenticated]
