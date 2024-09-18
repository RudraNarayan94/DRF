import json
from django.http import JsonResponse



def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON data
    data = {}
    print(request.GET) # url query params
    print(request.POST)
    try:
        data = json.loads(body) # string of JSON data -> python Dict
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['Content-Type'] = request.content_type
    return JsonResponse(data)