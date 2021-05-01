from django.urls import path, include
from rest_framework import routers
from store import views


app_name = 'store'

router = routers.DefaultRouter()
router.register('view-add-delete-toppings', views.ToppingsViewSet, basename='viewadddeletetoppings')
router.register('create-pizza', views.CreatePizzaViewSet, basename='createpizza')
router.register('edit-pizza', views.EditPizzaViewSet, basename='editpizza')
router.register('view-pizza-list', views.ViewAllPizzaViewSet, basename='viewpizzalist')


urlpatterns = [
    path('', include(router.urls)),
]
