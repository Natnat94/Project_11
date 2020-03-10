import logging
from sentry_sdk import capture_message
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import SearchForm
from offapi.models import Product, Category
from django.views.generic import FormView, ListView

FORMAT = '%(asctime)-15s  %(message)s : %(request)-8s'
logging.basicConfig(level=logging.INFO, format= FORMAT)

logger = logging.getLogger(__name__)

def search(request):
    query = request.GET.get('q')
    queryset = Product.objects.filter(product_name__icontains=query).order_by('product_name')
    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj,
               'title': 'Recherche',
               'big_title': 'voici le resultat de votre recherche'}

    capture_message("une recherche est faite", logger.info('New search', extra={
        'request': query,
    }))
    return render(request, 'search/search.html', context)


def substitute(request, pk):
    product = Product.objects.get(product_id=pk)
    cat = product.category_id.values_list('id', flat=True)
    substitute = Product.objects.all().filter(nutriscore__lt=product.nutriscore, category_id__in=cat)

    context = {'products': substitute,
               'title': 'Substitue',
               'big_title': 'Vous pouvez remplacer cet aliment par:',
               'previous_product': product,
               'substitut': True}

    return render(request, 'search/search.html', context)
