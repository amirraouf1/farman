from django.db import models
from django.utils.translation import gettext_lazy as _

class Personnel(models.Model):
    first_name = models.CharField(_("نام"), max_length=50)
    last_name = models.CharField(_("نام خانوادگی"), max_length=50)
    rank = models.CharField(_("درجه"), max_length=50)
    personnel_number = models.CharField(_("شماره پرسنلی"), max_length=20)
    branch = models.CharField(_("رسته"), max_length=50)
    specialty = models.CharField(_("تخصص"), max_length=100)
    birth_date = models.DateField(_("تاریخ تولد"))
    birth_place = models.CharField(_("محل تولد"), max_length=100)
    national_id = models.CharField(_("کد ملی"), max_length=10)
    hire_date = models.DateField(_("تاریخ استخدام"))
    region_entry_date = models.DateField(_("تاریخ ورود به منطقه"))
    is_instructor = models.BooleanField(_("آیا نظام مدرسین دارد؟"), default=False)
    instructors_grade = models.CharField(_("پایه نظام مدرسین"), max_length=50, blank=True, null=True)
    instructors_rank = models.CharField(_("رتبه نظام مدرسین"), max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.personnel_number}"
