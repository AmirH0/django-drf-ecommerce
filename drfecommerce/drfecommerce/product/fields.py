from django.db import models
from django.core import checks
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    description = "ordering field on unique"

    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)

    def check(self, **kwargs):
        return [*super().check(**kwargs), *self._check_for_field_attribute(**kwargs)]

    def _check_for_field_attribute(self, **kwargs):
        if self.unique_for_field is None:
            return [checks.Error("order field must be unique")]
        elif self.unique_for_field not in [
            f.name for f in self.model._meta.get_fields()
        ]:
            return [checks.Error("order field enterd does not match")]
        return []

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:

            query = {
                self.unique_for_field: getattr(model_instance, self.unique_for_field)
            }
            qs = self.model.objects.filter(**query)

            try:
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 1

            setattr(model_instance, self.attname, value)

        return super().pre_save(model_instance, add)
