from django.shortcuts import render,redirect
def Maintenance_Middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print('FIRST IRFAN MIDDLWARE TRIGGERED.....')
        
        response = get_response(request)
        return response

    return middleware