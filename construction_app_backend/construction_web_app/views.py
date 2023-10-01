from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
from .models import Material, Favorite, User
from django.db.models import Q
from django.forms.models import model_to_dict
import json
from django.shortcuts import get_object_or_404


def home(request):
    return JsonResponse({"message": "Bienvenidos User!"})

def material_list(request):
    query = request.GET.get('search')
    if query:
        materials = Material.objects.filter(Q(name__icontains=query) | Q(unit_price__icontains=query))
    else:
        materials = Material.objects.all()
    material_data = list(materials.values())
    return JsonResponse(material_data, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def favorite_material(request):
    data = json.loads(request.body)  # <-- Change this line
    user_id = data.get('user_id')  # <-- And this line
    material_id = data.get('material_id')  # <-- And this line

    user = User.objects.get(pk=user_id)
    material = Material.objects.get(pk=material_id)

    favorite = Favorite.objects.create(user=user, material=material)

    return JsonResponse({"status": "success"}, status=201)

def get_user_favorites(request):
    user_id = request.GET.get('user_id')
    user = User.objects.get(pk=user_id)

    favorites = Favorite.objects.filter(user=user).select_related('material')

    favorite_list = [{'id': favorite.id, 'material': model_to_dict(favorite.material)} for favorite in favorites]

    return JsonResponse(favorite_list, safe=False)  # return as JSON


@csrf_exempt
def favorite_material_detail(request, id):
    favorite = get_object_or_404(Favorite, id=id)

    if request.method == 'GET':
        # You can implement a GET method if you wish
        pass
    elif request.method == 'PUT':
        # And a PUT method
        pass
    elif request.method == 'DELETE':
        favorite.delete()
        return JsonResponse({'message': 'Favorite deleted'}, status=204)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)

