from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to my blog")

def about(request):
    return HttpResponse("This blog is my Django practice project.")

def hello(request, name):
    return HttpResponse(f"Hello, {name}!")

def status(request):
    return JsonResponse({"status": "ok", "site": "my blog"})

