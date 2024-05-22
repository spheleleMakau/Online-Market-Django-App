from django.shortcuts import render

# Create your views here.
def index(request):
    # render template, this will be available inside the template
    return render(request,'../templates/core/index.html' )
# puddle\templates\core\index.html