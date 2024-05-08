# from django.http import JsonResponse
# import requests

# # Initialize a list to store numbers
# numbers = []

# def calculate_average(request, number_id):
#     global numbers
#     test_server_url = f"http://127.0.0.1:9876/{number_id}"  # Adjust with actual server URL
#     response = requests.get(test_server_url)
#     new_numbers = response.json()  # Assuming the server returns a JSON list of numbers

#     # Update numbers list while maintaining the window size and uniqueness
#     numbers = list(set(numbers + new_numbers))[-10:]  # Adjust `10` to your desired window size

#     # Calculate average
#     average = sum(numbers) / len(numbers) if numbers else 0

#     return JsonResponse({
#         'windowPrevState': numbers,  # or manage a separate state if needed
#         'windowCurrState': numbers,
#         'avg': average
#     })


# import requests
# from django.http import JsonResponse

# def calculate_average(request, number_id):
#     global numbers
#     try:
#         test_server_url = f"http://127.0.0.1:9876/{number_id}"  # Ensure this is the correct URL
#         response = requests.get(test_server_url, timeout=10)  # Includes a timeout for the request
        
#         # Print or log the response for debugging
#         print("Status Code:", response.status_code)
#         print("Response Body:", response.text)  # Check what the actual response is

#         # Now attempt to decode JSON only if the content is not empty
#         if response.text:
#             new_numbers = response.json()
#             numbers = list(set(numbers + new_numbers))[-10:]  # Adjust the window size as needed
#             average = sum(numbers) / len(numbers) if numbers else 0
#         else:
#             return JsonResponse({'error': 'Empty response from server'}, status=500)

#     except requests.exceptions.JSONDecodeError:
#         return JsonResponse({'error': 'Invalid JSON received'}, status=500)
#     except requests.exceptions.RequestException as e:
#         return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({
#         'numbers': numbers,
#         'windowPrevState': numbers,
#         'windowCurrState': numbers,
#         'avg': average
#     })

from django.http import JsonResponse
import requests

# Global variable to store the current state of the window
current_window = []

# def calculate_average(request, number_id):
#     global current_window
#     try:
#         # Endpoint of the external server providing numbers
#         test_server_url = f"http://127.0.0.1:9876/{number_id}"
#         response = requests.get(test_server_url, timeout=10)
#         new_numbers = response.json()  # Assumes the response is a list of numbers

#         # Save the previous state before updating
#         previous_window = current_window.copy()

#         # Update the current window with new numbers, maintaining uniqueness and window size
#         current_window = list(set(current_window + new_numbers))[-10:]  # Adjust window size as needed

#         # Calculate the average of the current window
#         average = sum(current_window) / len(current_window) if current_window else 0

#         # Prepare the response
#         response_data = {
#             "windowPrevState": previous_window,
#             "windowCurrState": current_window,
#             "avg": round(average, 2)  # Round average to two decimal places
#         }

#     except requests.exceptions.RequestException as e:
#         return JsonResponse({'error': str(e)}, status=500)
#     except ValueError:  # includes JSONDecodeError
#         return JsonResponse({'error': 'Invalid JSON received'}, status=500)

#     return JsonResponse(response_data)

# from django.http import JsonResponse
# import requests

# def calculate_average(request, number_id):
#     global current_window
#     print(f"numberid{number_id}")
#     try:
#         # Endpoint of the external server providing numbers
#         test_server_url = f"http://127.0.0.1:9876/{number_id}"
#         response = requests.get(test_server_url, timeout=10)
        
#         # Check if the response is empty or not in JSON format
#         if response.status_code != 200:
#             return JsonResponse({'error': 'Bad response from server', 'status_code': response.status_code}, status=500)
        
#         if not response.text.strip():  # Check if the response body is empty
#             return JsonResponse({'error': 'Empty response from server'}, status=500)

#         new_numbers = response.json()  # Assumes the response is a list of numbers

#         # Save the previous state before updating
#         previous_window = current_window.copy()

#         # Update the current window with new numbers, maintaining uniqueness and window size
#         current_window = list(set(current_window + new_numbers))[-10:]  # Adjust window size as needed

#         # Calculate the average of the current window
#         average = sum(current_window) / len(current_window) if current_window else 0

#         # Prepare the response
#         response_data = {
#             "windowPrevState": previous_window,
#             "windowCurrState": current_window,
#             "avg": round(average, 2)  # Round average to two decimal places
#         }

#     except requests.exceptions.RequestException as e:
#         return JsonResponse({'error': str(e)}, status=500)
#     except ValueError as e:  # includes JSONDecodeError
#         return JsonResponse({'error': 'Invalid JSON received', 'details': str(e), 'response_body': response.text}, status=500)

#     return JsonResponse(response_data)

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

