import logging

logger = logging.getLogger(__name__)


class loggingmiddleware:

    def __init__(self, get_response):
        # This is called only once when the server starts
        self.get_response = get_response
        print("Hello")

    def __call__(self, request):
        # This method is called for every request before the view is called
        logger.info(
            f"Request Method: {request.method} | Request URL: {request.path}")
        print("chalraha he bhai !!!")

        response = self.get_response(request)

        # You can modify the response object here if needed
        logger.info(f"Response Status Code: {response.status_code}")
        print("Response pe bhi chal raha !!!")

        return response


# Function based middleware:

# def my_custom_middleware(get_response):
#     def middleware(request):
#         # Code to execute for each request before the view (and later middleware) are called.
#         print("Before the view")

#         response = get_response(request)

#         # Code to execute for each request/response after the view is called.
#         print("After the view")

#         return response

#     return middleware
