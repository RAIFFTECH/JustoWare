from django.db import models
import re
from django.core.exceptions import ValidationError

class DefaultToZeroMixin(models.Model):
    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if (isinstance(field, models.IntegerField) or isinstance(field, models.FloatField)) and field.attname != 'id':
                if getattr(self, field.name) is None or getattr(self, field.name) == '':
                    setattr(self, field.name, 0)

        super(DefaultToZeroMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True

def validate_numeric(value):
    if not re.match(r'^[0-9]+$', value):
        raise ValidationError(
            'El número de celular debe contener solo dígitos numéricos.')