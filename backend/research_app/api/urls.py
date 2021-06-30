import django.core.handlers.wsgi
from ninja import NinjaAPI, Path
from django.urls import path

from ..schemas.testing import TestSchema, TestResponseSchema, PathDate

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


urlpatterns = [
    path('', api.urls)
]
