from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductEntry


# Create your views here.
def show_main(request):
    context = {
        "name": "Hawk's Revenge",
        "price": 2700,
        "description": "An angel makes itself look scary to ward away evil, A demon makes itself look beautiful to deceive humans, The wolf howls but the hawk growls.",
        "effects": "+200 Attack, +50 range, +3 speed.",
    }
    return render(request, "main.html", context)


def create_product(request):
    form = ProductEntry(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("main:show_main")

    context = {"form": form}
    return render(request, "create_products.html", context)


def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json_by_id(request, id):
    data = Product.objects.all(pk=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )
