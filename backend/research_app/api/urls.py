from typing import List
import asyncio

from ninja import Router, Path

from ..schemas.testing import TestSchema, TestResponseSchema, PathDate
from ..schemas.models import CountrySchema
from ..models import Country

router = Router()


@router.get("/")
def root(request):
    # request type:
    # django.core.handlers.wsgi.WSGIRequest
    # or
    # django.core.handlers.asgi.ASGIRequest
    #
    return {'Hello': 'World!'}


@router.post("/multiple/", response=TestResponseSchema)
def root(request, body: TestSchema):

    # return {'result': body.input * body.x}
    # return TestResponseSchema(result=body.input * body.x)
    return body.result()


# use schema for path params, see docs
@router.get("/events/{year}/{month}/{day}/")
def events(request, date: PathDate = Path(...)):
    return {"date": date.value()}


@router.get("/countries/", response=List[CountrySchema])
def get_countries(request):
    return Country.objects.all()


@router.get("/delay/")
async def delay_view(request):
    """ test async """
    await asyncio.sleep(2)
    return {'asd': 'zxc'}
