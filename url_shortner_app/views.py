from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from .models import ShortURL
from .serializers import ShortURLSerializer

from .utilities import shorten_url


@csrf_exempt
def shortURL_list(request):
    '''List all urls, or create new url'''
    if request.method == 'GET':
        short_URLs = ShortURL.objects.all()
        serializer = ShortURLSerializer(short_URLs,
                                        many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_data = {}
        serializer_data['actual_url'] = data['actualURL']
        serializer_data['short_url'] = shorten_url(data['actualURL'])
        serializer = ShortURLSerializer(data=serializer_data)
        print('*' * 80)
        print('iron man serializer.is_valid()', serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def shortURL_detail(request, short_url):
    '''Get or Add a short URL'''
    if request.method == 'GET':
        print('*' * 80)
        print('iron man short_url', short_url)
        try:
            shortURL = ShortURL.objects.get(
                short_url=short_url)
            # serializer = 
            return JsonResponse(shortURL.actual_url, safe=False)
        except ShortURL.DoesNotExist:
            return HttpResponse(status=404)
