from typing import List
import asyncio

import django.core.handlers.wsgi
from ninja import NinjaAPI, Path
from django.urls import path

from ..schemas.testing import TestSchema, TestResponseSchema, PathDate
from ..schemas.models import CountrySchema
from ..models import Country

api = NinjaAPI()


@api.get("/")
def root(request):
    return {'Hello': 'World!'}


@api.post("/multiple", response=TestResponseSchema)
def root(request: django.core.handlers.wsgi.WSGIRequest, body: TestSchema):

    # return {'result': body.input * body.x}
    # return TestResponseSchema(result=body.input * body.x)
    return body.result()


# use schema for path params, see docs
@api.get("/events/{year}/{month}/{day}")
def events(request, date: PathDate = Path(...)):
    return {"date": date.value()}


@api.get("/countries", response=List[CountrySchema])
def get_countries(request):
    return Country.objects.all()


@api.get("/delay")
async def delay_view(request):
    """ test async """
    await asyncio.sleep(2)
    return {'asd': 'zxc'}


urlpatterns = [
    path('', api.urls)
]
