from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Product
from api.models import Category
from django.http.response import HttpResponse


#
#
# def hello4(request, product_id):
#   return HttpResponse(f'hello worls :{product_id}')
#
# products = []
# for  i in range(8):
#  products.append(
#   {
#     'id':i,
#     'name':f'product:{i} ',
#     'price':i*1000+253
#   }
#
# )

# list_of_categories(request,id ,products):
# return HttpResponse(f'hello :{id} :{products}' )



def product_list(request):
    products = Product.objects.all()

    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request ,product_id):
   try:
     product = Product.objects.get(id = product_id)
   except Product.DoesNotExist as e:
       return JsonResponse({'error no obejct by this id':str(e)})
   return JsonResponse(product.to_json())




def get_category(request, p_id):
  try:
   categor = Category.objects.get(id= p_id)
  except Product.DoesNotExist as e:
    return JsonResponse({'error no obejct by this id': str(e)})
  return JsonResponse(categor.to_json())


def categories_list(request):
    category = Category.objects.all()
    category_json = [category1.to_json() for category1 in category]
    return JsonResponse(category_json, safe = False)





def list_of (request ,product_id, prod_id):
    cat1 = Product.objects.get(prod_id)
    try:
      listt = Category.objects.get(id=cat1)
    except Product.DoesNotExist as e:
      return JsonResponse({'error no obejct by this id': str(e)})
    return JsonResponse(listt.to_json())
