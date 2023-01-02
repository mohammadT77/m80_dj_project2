from django.http import HttpResponse

from app1.utils import get_client_ip, get_ip_info


def restrict_local_ip(view_func):
    banned_ip = '127.0.0.1'

    def wrapper(request, *args, **kwargs):
        client_ip = get_client_ip(request)
        if client_ip == banned_ip:
            return HttpResponse("Forbidden!!!", status=403)
        return view_func(request, *args, **kwargs)

    return wrapper


def restrict_ip(*banned_ip):
    def inner_restrict_ip(view_func):
        def wrapper(request, *args, **kwargs):
            client_ip = get_client_ip(request)
            if client_ip in banned_ip:
                return HttpResponse("Forbidden!!!", status=403)
            return view_func(request, *args, **kwargs)

        return wrapper

    return inner_restrict_ip


def restrict_countries(*countries):
    def inner_restrict_country(view_func):
        def wrapper(request, *args, **kwargs):
            client_ip = get_client_ip(request)
            ip_info = get_ip_info(client_ip)
            if ip_info['country'] in countries:
                return HttpResponse("Forbidden!!!", status=403)
            return view_func(request, *args, **kwargs)

        return wrapper

    return inner_restrict_country

