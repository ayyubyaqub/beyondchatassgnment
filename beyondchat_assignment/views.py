import requests
from django.http import JsonResponse
from django.views import View

class GetApiResponseView(View):
    def get(self, request, *args, **kwargs):
        url = 'https://devapi.beyondchats.com/api/get_message_with_sources' 
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()  #Fetch the data from the pages of the API above.


            return JsonResponse(data)  # Return the JSON response as a Django JsonResponse
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)