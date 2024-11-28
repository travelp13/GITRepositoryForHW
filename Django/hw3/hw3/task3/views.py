from django.http import HttpResponse


def custom_file_response(request):
    response = HttpResponse("Here is your file", content_type="text/plain")
    response.status_code = 227
    return response
