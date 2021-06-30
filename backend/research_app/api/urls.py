import django.core.handlers.wsgi
from ninja import NinjaAPI
from django.urls import path

from ..schemas.testing import TestSchema, TestResponseSchema

api = NinjaAPI()


@api.get("/")
def root(request):
    return {'Hello': 'World!'}


@api.post("/multiple", response=TestResponseSchema)
def root(request: django.core.handlers.wsgi.WSGIRequest, body: TestSchema):

    # return {'result': body.input * body.x}
    return TestResponseSchema(result=body.input * body.x)


urlpatterns = [
    path('', api.urls)
]
