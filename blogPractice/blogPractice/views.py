from django.http import HttpResponse, request

def index(request):
    return HttpResponse(f"""<h1>Hello! You are at the main page!</h1>""")
