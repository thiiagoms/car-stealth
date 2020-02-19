from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests
import json


# Create your views here.
def crawler(request, placa=None):
    url = f"https://apicarros.com/v1/consulta/{placa}/json"
    request = requests.get(url, timeout=5)
    content = json.loads(request.text)
    data = json.dumps(content, indent=4, sort_keys=True)
    return HttpResponse(data)