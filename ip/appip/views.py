from django.shortcuts import render,HttpResponse
from ipware import get_client_ip
# Create your views here.

def my_view(request):
    ip, is_routable = get_client_ip(request)
    
    if ip is None:
        # No IP found
        print("No IP address found")
    else:
        # IP found
        print(f"User IP: {ip}")
        if is_routable:
            print("Public IP")
        else:
            print("Private IP")
    
    return HttpResponse(f"Your IP is {ip}")
