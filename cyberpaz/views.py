from django.shortcuts import redirect, render

from .forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form = ContactForm()
    return render(request, "index.html", {"form": form})


def contact_success_view(request):
    return render(request, "contact_success.html")
