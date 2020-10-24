from django.urls import path, include
from webapp.views import IndexView, PhotoView, PhotoCreateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('photo/', include([
        path('<int:pk>/', include([
            path('', PhotoView.as_view(), name='photo_view'),
        ])),
        path('create/', PhotoCreateView.as_view(), name='photo_create'),
    ])),
]