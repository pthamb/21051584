
import requests
from django.core.cache import cache
from django.utils.timezone import now
import datetime
from django.http import JsonResponse


def get_cached_token():
    # Check if a valid token exists in cache
    token = cache.get('api_token')
    if token and token['expires'] > now():
        return token['access_token']
    else:
        return refresh_token()



def refresh_token():
    
    response = requests.post('http://20.244.56.144/authenticate', data={'client_id': 'your_client_id', 'client_secret': 'your_secret'})
    data = response.json()
    print("API response:", data)  

    if 'expires_in' not in data:
        raise Exception('API did not return expected "expires_in" data')

    expires = now() + datetime.timedelta(seconds=data['expires_in'])
    token = {'access_token': data['access_token'], 'expires': expires}
    cache.set('api_token', token, timeout=data['expires_in'])  # Cache the token
    return data['access_token']


def get_top_products(request, companyname, categoryname):
    n = request.GET.get('top', 10)
    min_price = request.GET.get('minPrice', 0)
    max_price = request.GET.get('maxPrice', float('inf'))

    api_url = f"http://20.244.56.144/test/companies/{companyname}/categories/{categoryname}/products?top={n}&minPrice={min_price}&maxPrice={max_price}"
    response = requests.get(api_url)

    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch data from external API', 'status_code': response.status_code, 'details': response.text}, status=response.status_code)

    try:
        data = response.json()
    except ValueError:  # Includes JSONDecodeError
        return JsonResponse({'error': 'Invalid JSON received', 'details': response.text}, status=500)

    return JsonResponse({
        'company': companyname,
        'category': categoryname,
        'products': data
    })



def get_product_details(request, categoryname, productid):
    api_url = f"http://20.244.56.144/{categoryname}/products/{productid}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        product_details = response.json()
        return JsonResponse(product_details)
    except requests.exceptions.RequestException as e:
       
        error_message = {"error": f"Failed to fetch data from external API: {str(e)}"}
        return JsonResponse(error_message, status=500)  
    except ValueError as e:
        # Handle JSON decoding errors
        error_message = {"error": f"Failed to decode JSON response: {str(e)}"}
        return JsonResponse(error_message, status=500)  # Internal Server Error