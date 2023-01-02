from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app1.decorators import restrict_local_ip, restrict_ip, restrict_countries
from app1.utils import get_client_ip

my_decorator = restrict_ip("127.0.0.1", "2.3.4.5")


@restrict_countries("IR")
def simple_view(request):
    ip = get_client_ip(request)
    return HttpResponse(f"Hello ip {ip}!")
