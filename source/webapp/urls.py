from django.urls import path, include
from webapp.views import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView, PhotoChosenView, PhotoRemoveView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('photo/', include([
        path('<int:pk>/', include([
            path('', PhotoView.as_view(), name='photo_view'),
            path('update/', PhotoUpdateView.as_view(), name='photo_update'),
            path('delete/', PhotoDeleteView.as_view(), name='photo_delete'),
            path('chosen/', PhotoChosenView.as_view(), name='photo_choose'),
            path('remove/', PhotoRemoveView.as_view(), name='photo_remove'),
        ])),
        path('create/', PhotoCreateView.as_view(), name='photo_create'),
    ])),
]