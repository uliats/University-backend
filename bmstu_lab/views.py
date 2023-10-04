from django.shortcuts import render
from datetime import date

# Определите массив заказов как отдельную переменную
orders_data = [
    {'title': 'Геологоразведочные работы', 'id': 1, 'image': 'images/3.jpg', 'worker' :'геолог' ,
     'info': 'Геологическое картирование для определения структуры и состава горных пород'},
    {'title': 'Бурение и скважины', 'id': 2, 'image': 'images/2.jpg','worker' :'бурильщик',
     'info': 'Бурение нефтяных и газовых скважин геотермальных скважин угольных шахт.', 'worker' :'геолог' ,},
    {'title': 'Обработка и переработка', 'id': 3, 'image': 'images/1.jpg', 'worker' :'геолог' ,
     'info': 'Обогащение и обработка сырья для извлечения ценных компонентов'},
    {'title': 'Горная добыча', 'id': 4, 'image': 'images/4.jpg', 'worker' :'шахтер' ,
     'info': 'Добыча угля и других полезных ископаемых из шахт и карьеров.Добыча минералов, таких как золото, железо, медь и др'},
    {'title': 'Экологические исследования и мониторинг', 'id': 5, 'image': 'images/6.jpg', 'worker' :'эколог' ,
     'info': 'Оценка воздействия на окружающую среду и разработка мер по снижению негативного воздействия'},
]

def GetOrders(request):
    query_orders = request.GET.get('query_orders')

    if query_orders:
        # Фильтруем данные, учитывая как поле "type", так и поле "price"
        filtered_data = [it for it in orders_data if
                         query_orders.lower() in it['title'].lower() or query_substances.lower() in it[
                             'worker'].lower()]
    else:
        filtered_data = orders_data
        query_orders = ""

    return render(request, "orders.html", {'filtered_data': filtered_data, 'search_value': query_orders})

    #return render(request, 'orders.html', {'data': {
   #     'current_date': date.today(),
    #    'orders': orders_data , # Используйте определенную переменную
    #    'show_search_button': True,
   # }})

def GetOrder(request, id):
    order = None
    for item in orders_data:
        if item['id'] == id:
            order = item
            break

    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        'title': order['title'],  # Добавьте title в контекст
        'image': order['image'],
        'worker' : order['worker'],# Добавьте изображение в контекст
        'info': order['info'],     # Добавьте информацию в контекст
    }})


from django.http import HttpResponse

def sendText(request):
    input_text = request.POST.get('text', '')

    # Получите список заказов, которые начинаются с введенного текста
    matching_orders = []

    for order in orders_data:  # Используйте определенную переменную
        if order['title'].lower().startswith(input_text.lower()):
            matching_orders.append(order)

    # Возвращаем HTML-страницу с элементами, которые начинаются с введенного текста
    return render(request, 'orders.html', {'data': {'current_date': date.today(), 'orders': matching_orders}})
