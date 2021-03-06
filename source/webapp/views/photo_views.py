from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, \
    UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.timezone import make_naive
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Photo, Chosen
from webapp.forms import PhotoForm
from .base_views import SearchView


class IndexView(SearchView):
    template_name = 'photos/index.html'
    context_object_name = 'photos'
    paginate_by = 9
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
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def has_permission(self):
        photo = self.get_object()
        return super().has_permission() or photo.author == self.request.user

    def get_queryset(self):
        return super().get_queryset()

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'photos/photo_delete.html'
    model = Photo
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        photo = self.get_object()
        return super().has_permission() or photo.author == self.request.user

    def has_permission(self):
        return super().has_permission()

    def get_queryset(self):
        return super().get_queryset()


class PhotoChosenView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        chosen, created = Chosen.objects.get_or_create(image=photo, user=request.user)
        if created:
            photo.save()
            return HttpResponse("Всё хорошо")
        else:
            return HttpResponseForbidden()


class PhotoRemoveView(LoginRequiredMixin, View):
    def delete(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        chosen = Chosen.objects.get(image=photo, user=request.user)
        chosen.delete()
        return HttpResponse('Удалён из избранных')