from django.shortcuts import render
from item.models import Category , Item
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    # render template, this will be available inside the template
    context={
            'categories': categories,
            'items':items, }
    return render(request,'../templates/core/index.html',context=context)

def contact(request):
    return render(request, "../templates/core/contact.html")