from django.shortcuts import render
from django.http import Http404
from markdown2 import markdown
from django.urls import reverse
from django.shortcuts import HttpResponse,redirect,HttpResponseRedirect
import re
import random
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request,title):
    try:
        entry_content = util.get_entry(title)
        if entry_content is None:
            raise Http404("Page not found")
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": markdown(entry_content)
        })
    except Http404:
        return render(request, "encyclopedia/error.html", {
        "title": title
        })
    

def search(request):
    title = request.POST['q']
    entry_content = util.get_entry(title)
    if entry_content is not None:
        return redirect("entry", title=title)
    else:
        # No exact match found, generate recommendations
        recommendations = []
        all_entries = util.list_entries()  # Assuming util.list_entries() returns a list of entry titles
        for entry in all_entries:
            match = re.findall(title, entry, re.IGNORECASE)
            if match:
                recommendations.append(entry)
        return render(request, "encyclopedia/search.html", {
            "title":title,
            "recommendations": recommendations
        })
    
def create(request):
    if request.method=="GET":
        return render(request,"encyclopedia/create.html")
    else:
        title=request.POST.get('title')
        if util.get_entry(title):
            return render(request,"encyclopedia/index.html",{
                "message":"The title  already exists"
            })
        entry=request.POST['entry']
        util.save_entry(title,entry)
        return render(request,"encyclopedia/index.html",{
            "entries":util.list_entries()
        })

def edit_page(request, title):
    if request.method == "GET":
        # Fetch the existing data associated with the title
        content = util.get_entry(title)
        if content is None:
            # If entry doesn't exist, handle appropriately (e.g., redirect to a 404 page)
            return redirect('not_found')  # Redirect to a 'not_found' URL pattern
        return render(request, "encyclopedia/edit.html", {'title': title, 'content': content})
    elif request.method == "POST":
        # Get the updated data from the form
        new_title = request.POST.get('title')
        new_entry = request.POST.get('entry')
        
        if not new_title:
            return render(request, "encyclopedia/edit.html", {
                'title': title,
                'content': new_entry,
                
            })
        util.save_entry(new_title, new_entry)
        return redirect('entry', title=new_title)

def random_page(request):
    entry=util.list_entries()
    rand=random.choice(entry)
    content=markdown(util.get_entry(rand))
    return render(request,"encyclopedia/entry.html",{
        "title":rand,
        "entry":content
    })

        
