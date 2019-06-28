from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from googlemaps import Client
import requests, json
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def audio_data(request):
    # if request.method == 'POST':
    # gmaps = Client(key='AIzaSyCz1f09KVtopkT8WUZVcORb1B0AoTVzx_g&libraries=place')
    # print(gmaps)
    # geocode_result = gmaps.geocode('banyuwangi')

    # x = geocode_result[0]['geometry']['location']['lat'] #get latitute for the query 
    # y = geocode_result[0]['geometry']['location']['lng'] #get longitude for the query 

    if request.method == 'POST':
        url = 'http://photon.komoot.de/api/?q='
        data_audio = request.POST['send']
        addresses = ['soul']

        for address in addresses:
            resp = requests.get(url=url+address)
            data = json.loads(resp.text)
            print(data)

            return JsonResponse(data)