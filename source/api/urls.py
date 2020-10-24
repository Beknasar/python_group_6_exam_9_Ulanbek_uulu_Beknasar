from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import get_token_view, ChosenAddView, ChoosenRemoveView
# from .views import QuoteViewSet

app_name = 'api'

router = DefaultRouter()
# router.register(r'chosen', ChosenAddView)
# router.register(r'product', ProductViewSet)
# router.register(r'user', UserViewSet)
# router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('', include(router.urls)),
    path('chosen/', include([
        path('add', ChosenAddView.as_view(), name='chosen_add'),
        path('remove/', ChoosenRemoveView.as_view(), name="chosen_delete"),
    ])),
]