from django.views.generic.edit import CreateView
from .models import Personnel
from .forms import PersonnelForm
from django.urls import reverse_lazy
from django.views.generic import ListView

class PersonnelListView(ListView):
    model = Personnel
    template_name = 'personel/personnel_list.html'
    context_object_name = 'personnel'

class PersonnelCreateView(CreateView):
    model = Personnel
    form_class = PersonnelForm
    template_name = 'personel/add_personnel.html'
    success_url = reverse_lazy('personnel_list')
