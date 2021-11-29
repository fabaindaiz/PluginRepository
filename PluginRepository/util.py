from django.shortcuts import redirect

def login_required(function):
    def wrapper(request, *args, **kw):
        if not request.user.is_authenticated:
            return redirect('/login')
        else:
            return function(request, *args, **kw)
    return wrapper

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip