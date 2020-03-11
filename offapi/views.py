import json

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from offapi.models import Product


def product(request, pk):

    try:
        data = Product.objects.get(product_id=pk)
        data.nutriments = json.loads(data.nutriments)
        satfat = data.nutriments['saturated-fat_100g']
        nutriscore = "https://static.openfoodfacts.org/images/misc/nutriscore-" + data.nutriscore + ".svg"
        context = {'product': data,
                   'title': 'Produit',
                   'nutriscore': nutriscore,
                   'fat': satfat}
        return render(request, 'offapi/product.html', context)
    except ObjectDoesNotExist:
        return redirect('/')
