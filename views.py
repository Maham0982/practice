from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def home(request):
    peoples=[
        {"name":"maham", "age":20,},
        {"name": "amna", "age":19,},
        {"name": "hamna", "age":19},
        {"name": "fiza", "age":19},
        {"name": "eshal", "age":19}
        ]
    
    fruits=['mango','apple','orange']

    return render(request,"home/index.html", context={'page': 'django basic', 'peoples':peoples , 'fruits': fruits})




def about(request):
    context={'page':'about'}
    return render(request,"home/about.html", context)



def contact(request):
    context={'page':'contact'}
    return render(request,"home/contact.html", context)



def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>hey this is a success page<h1>")
