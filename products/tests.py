from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            article="ART-001",
            name="Тестовый товар",
            price=Decimal("199.90"),
        )

    def test_string_representation(self):
        self.assertEqual(str(self.product), "ART-001 — Тестовый товар")

    def test_product_list_view(self):
        response = self.client.get(reverse("product-list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовый товар")
        self.assertContains(response, "ART-001")
        self.assertTemplateUsed(response, "products/product_list.html")

    def test_product_list_json(self):
        response = self.client.get(reverse("product-list-json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(
            response.json(),
            {
                "products": [
                    {
                        "article": "ART-001",
                        "name": "Тестовый товар",
                        "price": "199.90",
                    }
                ]
            },
        )
