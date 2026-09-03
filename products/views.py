from django.http import JsonResponse
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"


def product_list_json(request):
    products = [
        {
            "article": product.article,
            "name": product.name,
            "price": str(product.price),
        }
        for product in Product.objects.all()
    ]

    return JsonResponse(
        {"products": products},
        json_dumps_params={"ensure_ascii": False},
    )
