from django.http import JsonResponse
import requests

def get_top_products(request, companyname, categoryname):
    n = request.GET.get('top', 10)
    min_price = request.GET.get('minPrice', 0)
    max_price = request.GET.get('maxPrice', float('inf'))

    api_url = f"http://20.244.56.144/test/companies/{companyname}/categories/{categoryname}/products?top={n}&minPrice={min_price}&maxPrice={max_price}"
    response = requests.get(api_url)

    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch data from external API', 'status_code': response.status_code}, status=500)

    try:
        data = response.json()
    except ValueError:
        return JsonResponse({'error': 'Invalid JSON received'}, status=500)

    return JsonResponse({
        'company': companyname,
        'category': categoryname,
        'products': data
    })




# def get_product_details(request, categoryname, productid):
#     api_url = f"http://20.244.56.144/{categoryname}/products/{productid}"
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()  # Raise exception for HTTP errors
#         product_details = response.json()
#         return JsonResponse(product_details)
#     except requests.exceptions.RequestException as e:
#         # Handle request exceptions such as connection errors, timeouts, etc.
#         error_message = {"error": f"Failed to fetch data from external API: {str(e)}"}
#         return JsonResponse(error_message, status=500)  # Internal Server Error
#     except ValueError as e:
#         # Handle JSON decoding errors
#         error_message = {"error": f"Failed to decode JSON response: {str(e)}"}
#         return JsonResponse(error_message, status=500)  # Internal Server Error