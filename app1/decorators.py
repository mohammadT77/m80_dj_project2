from django.http import HttpResponse

from app1.utils import get_client_ip


def restrict_local_ip(view_func):
    banned_ip = '127.0.0.1'

    def wrapper(request, *args, **kwargs):
        client_ip = get_client_ip(request)
        if client_ip == banned_ip:
            return HttpResponse("Forbidden!!!", status=403)
        return view_func(request, *args, **kwargs)

    return wrapper


def restrict_ip(*banned_ip):  # @restrict_ip('1.2.3.4', '12.54.22.22')
    def inner_restrict_ip(view_func):
        def wrapper(request, *args, **kwargs):
            client_ip = get_client_ip(request)
            if client_ip in banned_ip:
                return HttpResponse("Forbidden!!!", status=403)
            return view_func(request, *args, **kwargs)

        return wrapper

    return inner_restrict_ip
