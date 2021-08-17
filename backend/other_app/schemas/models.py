from typing import Union
from uuid import UUID
from ninja import Schema


class ContentTypeSchema(Schema):
    model: str


class SettingsOneSchema(Schema):
    uuid: UUID
    field1: str


class SettingsTwoSchema(Schema):
    uuid: UUID
    field2: str


class SettingsHolderSchema(Schema):
    uuid: UUID
    setting_type: ContentTypeSchema
    setting: Union[SettingsOneSchema, SettingsTwoSchema]
