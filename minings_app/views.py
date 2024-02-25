


from django.db.models import Q
import psycopg2

from django.shortcuts import render, redirect, get_object_or_404
from minings_app.models import Service, Order, OrderServices

def GetServices(request):
    services = Service.objects.filter(status=1).order_by('-id')
    query_service = request.GET.get('query_service')

    if query_service:
        filtered_services = services.filter(
            name__icontains=query_service
        )
    else:
        filtered_services = services.all()
        query_service = ""

    return render(request, "service.html", {'filtered_services': filtered_services, 'search_value': query_service})

def GetService(request, id):
    service = get_object_or_404(Service, id=id, status=1)
    return render(request, "servicecard.html", {'service': service})

def delete_service(request, id):
    service = get_object_or_404(Service, id=id)
    service.status = 2  # Помечаем услугу как удаленную
    service.save()
    return redirect('services')





# def add_to_cart(request, id):
#     service = get_object_or_404(Service, id=id)
#     draft_order = Order.objects.create(status=1)  # Create a draft order
#     draft_order.services.add(service)  # Add the service to the draft order
#
#     # Pass the draft_order to the cart template
#     return render(request, 'cart.html', {'draft_order': draft_order})


def add_to_cart(request, id):
    service = get_object_or_404(Service, id=id)
    draft_order = Order.objects.filter(status=1).first()
    if not draft_order:
        draft_order = Order.objects.create(status=1)
        print(" Новая заявка:", draft_order.id)
    draft_order.services.add(service)
    print("Добавлена услуга", service.name, "в заявку", draft_order.id)

    return redirect('services')

def cart_view(request):

    draft_order = Order.objects.filter(status=1).last()
    return render(request, 'cart.html', {'draft_order': draft_order})

from django.http import HttpResponseRedirect



def clear_cart(request):

    draft_order = Order.objects.filter(status=1).last()

    if draft_order:

        draft_order.status = 5  # 5 - статус "Удалён"
        draft_order.save()

    # Перенаправляем на страницу корзины
    return HttpResponseRedirect('/cart/')
