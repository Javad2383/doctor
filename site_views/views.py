from django.shortcuts import render


def site_index(request):
    context = {}
    return render(request, "pgs/index.html", context)

