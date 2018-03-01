from ecommerce import settings
from django.shortcuts import render, get_object_or_404, HttpResponse, Http404


def search(request):
    context = {'message': ''}
    if request.method == 'GET' and request.GET:
        # results = Sear
        result = request.GET
        print(request.GET)
        query = result['query']
        print(query)
        if query:
            context['message'] = query
    return render(request, "ecommerce/search.html", context=context)