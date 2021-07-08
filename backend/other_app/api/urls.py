from typing import List

from ninja import Router

router = Router()


@router.get("/")
def other_root(request):
    return {'i`m': 'other app'}
