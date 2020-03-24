from django.urls import path

from api.views import product_list, product_detail, categories_list, get_category, list_of

urlpatterns =[
  # path('products/',hello2),
  # path('products/<int:product_id>', hello4),
  path('categories/', categories_list),
  path('categories/<int:p_id>', get_category),
  path('products/', product_list),
  path('products/<int:product_id>', product_detail),
  path('products/<int:product_id>/<int:prod_id>/', list_of)

]

