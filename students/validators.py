from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 10:
        raise ValidationError(_('Students must be at least 10 years old.'))