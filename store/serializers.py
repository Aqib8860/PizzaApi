from rest_framework import serializers
from .models import *


class ToppingsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="store:viewadddeletetoppings-detail")

    class Meta:
        model = Toppings
        fields = '__all__'


class CreatePizzaSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Pizza
        fields = '__all__'


class EditPizzaSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Pizza
        fields = '__all__'


class ToppingsNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Toppings
        fields = ['name']


class ViewPizzaSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    toppings = ToppingsNameSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name="store:editpizza-detail")

    class Meta:
        model = Pizza
        fields = '__all__'
