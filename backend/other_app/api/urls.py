from typing import List

from ninja import Router

from ..schemas.models import SettingsHolderSchema
from ..models import SettingsHolder

router = Router()


@router.get("/")
def other_root(request):
    return {'i`m': 'other app'}


@router.get("/settings/", response=List[SettingsHolderSchema])
def settings_view(request):
    return SettingsHolder.objects.all()
