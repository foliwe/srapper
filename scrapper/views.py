from django.shortcuts import render, redirect
import requests 
from . models import Link

from bs4 import BeautifulSoup

def scrape(request):
    if request.method == "POST":
        site = request.POST.get("site", "")
        
        # Check if the user entered a site that starts with "https://www."
        if not (site.startswith("http://www.") or site.startswith("https://www.")):
            # If not, prepend "https://www." to the site
            site = "https://www." + site

        page = requests.get(site)
        soup = BeautifulSoup(page.content, "html.parser")
        links = soup.find_all("a")
        for link in links:
            link_address = link.get("href")
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)

        return redirect('/')
    else:
        data = Link.objects.all()
        context = {"data": data}
        return render(request, "scrape.html", context)

# def scrape(request):
#     if request.method == "POST":
#         site = request.POST.get("site", "")
#         page = requests.get(site)
#         soup = BeautifulSoup(page.content, "html.parser")
#         links = soup.find_all("a")
#         for link in links:
#             link_address = link.get("href")
#             link_text = link.string
#             Link.objects.create(address=link_address, name=link_text)

#         return redirect('/')
#     else:
#         data = Link.objects.all()
#         context = {"data": data}
#         return render(request, "scrape.html", context)

def clear(request):
    Link.objects.all().delete()
    return redirect('/')
   