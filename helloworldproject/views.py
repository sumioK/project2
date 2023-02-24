from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunc(request):
    object = HttpResponse('<h1>Hello world !!</h1>')
    return object

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'