from typing import List

from ninja import Router

router = Router()


@router.get("/")
def root(request):
    return {'i`m': 'other app'}
