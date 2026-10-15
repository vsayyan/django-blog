from django.http import Http404, JsonResponse
from django.shortcuts import render

POSTS= [
    {"id":1,"title":"My First post", "author":"Vahe",
     "body":"Todya I started learning Django.","published":True
     },
    {"id":2,"title": "Templates are cool","author":"Vahe",
     "body":"Now my pages are real HTML.", "published": True
     },
    {"id": 3, "title": "Draft idea", "author": "Vahe",
    "body": "This one is not ready yet.", "published": False},
]

# Create your views here.
def home(request):
    posts = [post for post in posts if post["published"]]
    return render(request, "blog/home.html", {"posts":posts})

def post_detail(request,post_id):
    for post in POSTS:
        if post["id"] == post_id and post["published"]:
            return render(request,"blog/post_detail.html", {"post":post})
        raise Http404("Postnot found")

def about(request):
    return render(request,"blog/about.html")


def hello(request, name):
    return render(request,"blog/hello.html", {"name":name})

def status(request):
    return JsonResponse({"status": "ok", "site": "my blog"})

def contact(request):
    return HttpResponse("Contact us: hello@example.com")

def add(request,a,b):
    return JsonResponse({"result": a + b})
