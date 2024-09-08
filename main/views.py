from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        "name": "Hawk Gel",
        "price": 3,
        "description": "An angel makes itself look scary to ward away evil, A demon makes itself look beautiful to deceive humans, The wolf howls but the hawk tuahs.",
        "effects": "+200 range to spit type attacks."
    }
    return render(request, "main.html", context)
