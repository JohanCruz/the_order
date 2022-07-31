from itertools import product
from unicodedata import category
from django.shortcuts import render, redirect
from .models import Category, Restaurant, Product, Order, ProductOrder
from django.http import JsonResponse


def menu(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/menu.html', {'restaurants':restaurants})

def menu_order(request, pk):    
    restaurant = Restaurant.objects.get(pk = pk)
    categories = [] 
    if restaurant:
        categories = Category.objects.filter(restaurant = pk, visible = True)        
        products = Product.objects.filter(category__restaurant = pk, visible = True)
      
    return render(request, 'restaurant/menu_restaurant.html', {'restaurant':restaurant, 'categories':categories, 'products':products})


def order(request, pk): 
    if request.method == "POST":
        restaurant = Restaurant.objects.get(pk = pk)

        if restaurant :
            order = Order.objects.create(restaurant = restaurant)
            order.description = request.POST.get('description', 'NA')
            order.name = request.POST.get( 'name_of_person', 'NA')
            
            def save_order(count):
                if count == 1 :
                    order.save()
            
            products = Product.objects.filter(category__restaurant = pk)
            number_diferent_products = 0 
                
            for product in products:
                product_quantity = request.POST.get(str(product.pk), 0)
                
                if product_quantity != 0 and product_quantity !='0' :
                    number_diferent_products += 1
                    save_order(number_diferent_products)
                    productOrder = ProductOrder.objects.create(order=order, product=product)
                    productOrder.quantity = product_quantity
                    carry_off = request.POST.getlist('carry_off_'+str(product.pk))
                    productOrder.carry_off = "carry" in carry_off                        
                    productOrder.save()  
    
    response = redirect('/menu/' + str(pk))
    return response


def processing_orders(request, pk):
    restaurant = Restaurant.objects.get(pk = pk)
    
    if restaurant :
        orders = Order.objects.filter(restaurant = pk, state__in = ['ESPERA', 'PREPARACION'] ).order_by('-created_date')
        productOrders = ProductOrder.objects.filter(order__restaurant__pk = pk, order__state__in = ['ESPERA', 'PREPARACION']  )


    return render(request, 'restaurant/processing_orders.html', {'orders':orders, 'productOrders':productOrders, 'restaurant':restaurant})



def change_status(request, pk, status,restaurant):
    
    productOrder = ProductOrder.objects.get(pk= pk)
    if productOrder:
        productOrder.state = status
        if status in ['ESPERA', 'PREPARACION', 'FINALIZADO']:
            productOrder.save()
            response = redirect('/processing/' + str(restaurant))
            return response
            
        else :
            return JsonResponse({'message':'status incorrect'})    
    
    return JsonResponse({'message':'Something was wrong'})