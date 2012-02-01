from models import RequestsLogItem


class RequestsLogMiddleware():
    def process_request(self, request):
        r = RequestsLogItem(
                path=request.path,
                method=request.method,
                META=request.method
                )
        r.save()
        return None
