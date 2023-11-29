from django.shortcuts import render
from datetime import date
from bmstu_lab.models import Miningservices
from django.db.models import Q
import psycopg2
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Ваш остальной код здесь


# Определите массив заказов как отдельную переменную
orders_data = [
    {'title': 'Геологоразведочные работы', 'id': 1, 'image': 'images/3.jpg', 'worker': 'геолог',
     'info': 'Геологическое картирование для определения структуры и состава горных пород'},
    {'title': 'Бурение и скважины', 'id': 2, 'image': 'images/2.jpg', 'worker': 'бурильщик',
     'info': 'Бурение нефтяных и газовых скважин геотермальных скважин угольных шахт.'},
    {'title': 'Обработка и переработка', 'id': 3, 'image': 'images/1.jpg', 'worker': 'инженер',
     'info': 'Обогащение и обработка сырья для извлечения ценных компонентов'},
    {'title': 'Горная добыча', 'id': 4, 'image': 'images/4.jpg', 'worker': 'шахтер',
     'info': 'Добыча угля и других полезных ископаемых из шахт и карьеров.Добыча минералов, таких как золото, железо, медь и др'},
    {'title': 'Экологические исследования и мониторинг', 'id': 5, 'image': 'images/6.jpg', 'worker': 'эколог',
     'info': 'Оценка воздействия на окружающую среду и разработка мер по снижению негативного воздействия'},
]






def GetMinings(request):
    minings = Miningservices.objects.filter(mining_status__exact=True).order_by('-idservice')
    query_minings = request.GET.get('query_minings')

    if query_minings:
        filtered_data = minings.filter(
            Q(nameservice__icontains=query_minings)
        )
    else:
        filtered_data = minings.all()
        query_minings = ""
    #print("Filtered Data:", filtered_data)  # Вывод значений в консоль

    #
    return render(request, "mining.html", {'filtered_data': filtered_data, 'search_value': query_minings})



def GetMining(request, id):
    data_by_id = get_object_or_404(Miningservices, idservice=id, mining_status=True)
    return render(request, "miningcard.html", {'minings': data_by_id})


def delete_mining(request, id):
    conn = psycopg2.connect(dbname="miningservices", host="localhost", user="postgres", password="1234", port="5433")
    cursor = conn.cursor()
    cursor.execute("UPDATE \"miningservices\" SET mining_status=\'false\' WHERE idservice = %s", [id])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('minings')












# def GetOrders(request):
#     substanses = Miningservices.objects.filter(sub_status=True).order_by('-sub_id')
#     input_text = request.GET.get('text')
#
#     # Определите переменную для отфильтрованных заказов
#     matching_orders = orders_data
#     services = Miningservices.objects.all()
#
#
#     for service in services:
#         print(f"ID: {service.idservice}, Name: {service.nameservice}")
#
#     if input_text:
#         # Фильтруем данные, учитывая поле "title"
#         matching_orders = [it for it in orders_data if input_text.lower() in it['title'].lower()]
#
#     context = {
#         'current_date': date.today(),
#         'orders': matching_orders,
#         'show_search_button': True,
#         'search_value': input_text,
#         'services': Miningservices.objects.all()
#     }
#
#     return render(request, 'mining.html', {'data': context})
#
#
# def GetOrder(request, id):
#     order = None
#     for item in orders_data:
#         if item['id'] == id:
#             order = item
#             break
#
#     return render(request, 'miningcard.html', {'data': {
#         'current_date': date.today(),
#         'id': id,
#         'title': order['title'],
#         'image': order['image'],
#         'worker': order['worker'],
#         'info': order['info'],
#         'services': Miningservices.objects.all()
#     }})
#


    # Здесь вы можете вернуть данные в вашем представлении
