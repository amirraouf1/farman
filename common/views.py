# common/views.py

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin

class AdminCreateView(UserPassesTestMixin, CreateView):
    """
    A reusable base class for creating records, restricted to admin users.
    """

    # Only allow users who are staff (admin) to access this view
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    # Specify where to redirect upon successful submission
    def get_success_url(self):
        if hasattr(self, 'success_url'):
            return self.success_url
        else:
            raise NotImplementedError("You must define 'success_url' in the derived class.")

    # Ensure the form is provided dynamically
    def get_form_class(self):
        if hasattr(self, 'form_class'):
            return self.form_class
        else:
            raise NotImplementedError("You must define 'form_class' in the derived class.")

    # Custom context data for the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'اضافه کردن اطلاعات'  # Example title (can be customized)
        return context
