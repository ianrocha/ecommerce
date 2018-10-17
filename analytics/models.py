from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = settings.AUTH_USER_MODEL


class ObjectViewed(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)  # User instance
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # User, Product, Order, Cart, Address...
    object_id = models.PositiveIntegerField()  # User id, product id, order id...
    content_object = GenericForeignKey('content_type', 'object_id')  # Product instance
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} viewed {}".format(self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']  # Most recent saved show up first
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'
