from django.shortcuts import render, redirect
from offapi.models import ProductSaved, Product
from authentification.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def favorite(request, pk, pk2):
    b = ProductSaved(user_id=User.objects.get(username=request.user.username),
                     product_id=Product.objects.get(product_id=pk),
                     sub_id=Product.objects.get(product_id=pk2))
    b.save()

    return redirect('favorite')


@login_required(login_url='login')
def display_favorite(request):
    user = request.user.username
    p = ProductSaved.objects.all().filter(user_id=User.objects.get(username=user))
    context = {'products': p,
               'title': 'favorite'}

    return render(request, 'addfav/display.html', context)
