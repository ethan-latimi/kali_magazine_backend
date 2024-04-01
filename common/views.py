from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/v1/businesses/',
        'api/v1/businesses/pk',
        'api/v1/businesses/categories',
        'api/v1/foods/',
        'api/v1/foods/pk',
        'api/v1/foods/categories',
        'api/v1/lifestyles/',
        'api/v1/lifestyles/pk',
        'api/v1/lifestyles/categories',
        'api/v1/travels/',
        'api/v1/travels/pk',
        'api/v1/travels/categories',
        'api/v1/users/',
        'api/v1/users/pk',
        'admin/',
    ]
    return Response(routes)
