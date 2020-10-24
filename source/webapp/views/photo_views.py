from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, \
    UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.timezone import make_naive
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Photo
from webapp.forms import PhotoForm
from .base_views import SearchView


class IndexView(SearchView):
    template_name = 'photos/index.html'
    context_object_name = 'photos'
    paginate_by = 2
    paginate_orphans = 0
    model = Photo
    ordering = ['-created_at']
    search_fields = ['signature__icontains', 'author__icontains']

    def get_queryset(self):
        data = super().get_queryset()
        # if not self.request.GET.get('is_admin', None):
        #     data = data.filter(status='moderated')
        return data


class PhotoView(DetailView):
    model = Photo
    template_name = 'photos/photo_view.html'

    # чтоб товары, которых не осталось нельзя было и просмотреть
    # это можно добавить вместо model = Product в Detail, Update и Delete View.
    def get_queryset(self):
        return super().get_queryset()


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'photos/photo_create.html'
    form_class = PhotoForm
    model = Photo

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        form.save_m2m()
        return redirect('webapp:photo_view', pk=photo.pk)


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'photos/photo_update.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'product'
    permission_required = 'webapp.change_photo'

    def get_queryset(self):
        return super().get_queryset()

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})



