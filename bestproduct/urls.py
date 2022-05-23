from django.urls import path 
from . import views 

from .models import Products , Category 
urlpatterns = [
    path ('', views.products ,name = 'products' ) ,
    # path('/#<int:categoryid>', views.category , name = 'category'), 
    path('shop.html/<int:categoryid>', views.category  , name = 'shopCategory'),
    path('product-details.html/<int:proid>' , views.product , name="product"),
    path('shop.html/product-details.html/<int:proid>',views.product_shop  ),
    path("index.html", views.products),
    path('login.html', views.login),

    path('cart.html/<int:proid>', views.cart  , name ="cart"), 

   
    path('cart.html/', views.cartitem, name='cartitem'),
    path('deleteitem/<int:proid>/', views.deleteitem, name='delete'),



]