from django.http import JsonResponse
import requests

def calculate_average(request, number_id):
    global current_window
    try:
        response = requests.get(f'http://127.0.0.1:9876/{number_id}', timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        new_numbers = response.json()
        current_window = list(set(current_window + new_numbers))[-10:]  # Maintain last 10 unique numbers
        average = sum(current_window) / len(current_window) if current_window else 0
        response_data = {
            "windowPrevState": current_window,  # Assuming you might want to output this directly
            "windowCurrState": current_window,
            "avg": round(average, 2)
        }
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    except ValueError as e:
        return JsonResponse({'error': 'Invalid JSON received', 'details': str(e)}, status=500)
    except Exception as e:
        # Catching generic exceptions can help identify unexpected errors
        return JsonResponse({'error': 'An unexpected error occurred', 'details': str(e)}, status=500)

