from django.shortcuts import render
from django.conf import settings
import os

def home_view(request):
    return render(request, "home.html")

def contact_view(request):
    return render(request, "contact.html")

def menu_view(request):
    images_dir = os.path.join(settings.BASE_DIR, "main", "static", "images")
    items = []
    try:
        for fname in sorted(os.listdir(images_dir)):
            if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            base = os.path.splitext(fname)[0]
            name = base.replace("_", " ").replace("-", " ").title()
            items.append({
                "name": name,
                "price": "₹100",
                "image": f"images/{fname}",
            })
    except:
        items = []
    return render(request, "menu.html", {"items": items})
