from django.db import models


# class ActiveManager(models.Manager):
#     # def get_queryset(self):
#     #     return super().get_queryset().filter(is_active=True)
    
#     def isactive(self):
#         return self.get_queryset().filter(is_active=True)

class ActiveQuerySet(models.QuerySet):
    # def get_queryset(self):
    #     return super().get_queryset().filter(is_active=True)
    
    def isactive(self):
        return self.filter(is_active=True)
