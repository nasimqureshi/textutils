#  I have created this file - Nasim

from django.http import HttpResponse

# def index (request):
#
#     return HttpResponse("<h1>Nasim Qureshi how are you and where are you</h1>")
#
# def about(request):
#     return HttpResponse("My name is Nasim Qureshi")

def index(request):
    return HttpResponse("<h1>Home</h1>")
def removepunc(request):
    return HttpResponse("<h1>Remove Punctuation</h1>")

def capfirst(request):
    return HttpResponse("<h1>Capitalize First</h1>")

def newlineremove(request):
    return HttpResponse("<h1>New Line Remove First</h1>")

def spaceremove(request):
    return HttpResponse("<h1>Space Remove</h1>")

def charcount(request):
    return HttpResponse("<h1>Char Count</h1>")