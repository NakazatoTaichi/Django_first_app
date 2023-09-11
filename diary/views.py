from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Diary
from .forms import DiaryForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(TemplateView ,LoginRequiredMixin):
    template_name = "index.html"

class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')

class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

class DiaryListView(ListView):
    template_name = 'diary_list.html'
    model = Diary

class DiaryDetailView(DetailView):
    template_name = 'diary_detail.html'
    model = Diary

class DiaryUpdateView(UpdateView):
    template_name = 'diary_update.html'
    model = Diary
    fields = ('date', 'title', 'text',)
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.updated_at = timezone.now()
        diary.save()
        return super().form_valid(form)

class DiaryDeleteView(DeleteView):
    template_name = 'diary_delete.html'
    model = Diary
    success_url = reverse_lazy('diary:diary_list')

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

