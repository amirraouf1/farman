from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Personnel
from .forms import PersonnelForm
from common.views import AdminCreateView  # Assuming AdminCreateView is in common/views.py
from django.shortcuts import render

# Define personnel_list view to list all personnel entries
def personnel_list(request):
    personnel = Personnel.objects.all()
    return render(request, 'personel/personnel_list.html', {'personnel': personnel})
class AddPersonnelView(AdminCreateView):
    model = Personnel
    form_class = PersonnelForm
    success_url = reverse_lazy('personnel_list')
    template_name = 'personel/add_personnel.html'
