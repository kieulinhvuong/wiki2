from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def subPage(request, entry):
    content = util.get_entry(entry)
    if (content):
        return render(request, "encyclopedia/entrypage.html", {
        "entries": util.get_entry(entry)
    })
    else:
        return render(request, "encyclopedia/errorpage.html")




