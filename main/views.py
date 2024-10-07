from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import Product
from main.forms import ProductEntry
from django.contrib import messages
from django.views.decorators.http import require_http_methods, require_POST
from django.utils.html import strip_tags


# Create your views here.
@login_required(login_url="/login/")
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)
    login_success = request.session.pop("login_success", False)
    context = {
        "user": request.user,
        "product_entries": product_entries,
        "last_login": request.COOKIES.get("last_login"),
        "login_success": login_success,
    }
    return render(request, "main.html", context)


@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def create_product(request):
    if request.method == "POST":
        form = ProductEntry(request.POST)
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.name = strip_tags(form.cleaned_data["name"])
            product_entry.description = strip_tags(form.cleaned_data["description"])

            product_entry.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"status": "success"})
            return HttpResponseRedirect(reverse("main:show_main"))
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"status": "error", "message": "Invalid form data"})
    else:
        form = ProductEntry()

    context = {"form": form}
    return render(request, "create_product_entry.html", context)

@require_POST
def create_product_ajax(request):
    form = ProductEntry(request.POST)
    if form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user  
        product_entry.name = strip_tags(form.cleaned_data['name'])
        product_entry.description = strip_tags(form.cleaned_data['description'])
        product_entry.effects = strip_tags(form.cleaned_data['effects'])
        product_entry.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid form data'})


@login_required(login_url="/login/")
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)

    if request.method == "POST":
        form = ProductEntry(request.POST, instance=product)
        if form.is_valid():
            # Sanitize form
            product_entry = form.save(commit=False)
            product_entry.name = strip_tags(form.cleaned_data["name"])
            product_entry.description = strip_tags(form.cleaned_data["description"])
            product_entry.save()

            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"status": "success"})
            return HttpResponseRedirect(reverse("main:show_main"))
    else:
        form = ProductEntry(instance=product)

    context = {"form": form, "product": product}

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        html = render_to_string("edit_product.html", context, request=request)
        return JsonResponse({"html": html})

    return render(request, "edit_product.html", context)


@login_required(login_url="/login/")
@require_http_methods(["POST"])
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"status": "success"})
    return HttpResponseRedirect(reverse("main:show_main"))


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")
    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session["show_welcome_message"] = (
                True  # indeed used for something later
            )
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)

    context = {"form": form}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    request.session["show_welcome_message"] = False
    return response


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
