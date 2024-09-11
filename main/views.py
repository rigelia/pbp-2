from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        "name": "Hawk's Revenge",
        "price": 2700,
        "description": "An angel makes itself look scary to ward away evil, A demon makes itself look beautiful to deceive humans, The wolf howls but the hawk growls.",
        "effects": "+200 Attack, +50 range, +3 speed."
    }
    return render(request, "main.html", context)

# AKu suka pbp