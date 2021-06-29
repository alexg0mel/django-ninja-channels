from ninja import NinjaAPI
from django.urls import path

api = NinjaAPI()


@api.get("/")
def root(request):
    return {'Hello': 'World!'}


urlpatterns = [
    path('', api.urls)
]
