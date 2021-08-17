from uuid import uuid4

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


def get_uuid():
    return uuid4()


class SettingsOne(models.Model):
    uuid = models.UUIDField(primary_key=True, default=get_uuid)
    field1 = models.CharField(max_length=32)

    def __str__(self):
        return f'setting1 {self.field1}'


class SettingsTwo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=get_uuid)
    field2 = models.CharField(max_length=32)

    def __str__(self):
        return f'setting2 {self.field2}'


class SettingsHolder(models.Model):
    uuid = models.UUIDField(primary_key=True, default=get_uuid)
    setting_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    setting_id = models.UUIDField()
    setting = GenericForeignKey('setting_type', 'setting_id')

    def __str__(self):
        return self.setting
