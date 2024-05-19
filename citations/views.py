from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from django.views import View

from django.shortcuts import render

class FetchCitationsView(View):
    def get(self, request, *args, **kwargs):
        base_url = 'https://devapi.beyondchats.com/api/get_message_with_sources'
        page = 1
        all_citations = []

        while True:
            response = requests.get(base_url, params={'page': page})

            if response.status_code != 200:
                break

            data = response.json()

            # return JsonResponse(data)
            messages = data.get('data', [])

            for message in messages.get('data', []):
                
                sources = message.get('source', [])
      
                citations = [ source for source in sources  if  source.get('link', '')=='' ]
          
                all_citations.append({ 'citations': citations})

            if not data.get('next'):
                break

            page += 1
        print(all_citations,)
        return JsonResponse(all_citations,safe=False)
