from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import VzkazForm
from .models import Vzkaz


def uvod(request):
    if request.method == "POST":
        form = VzkazForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Děkujeme, vzkaz je uložený.")
            return redirect("uvod")
    else:
        form = VzkazForm()
    vzkazy = Vzkaz.objects.filter(zverejneno=True)[:50]
    return render(request, "kniha/uvod.html", {"form": form, "vzkazy": vzkazy})
