from django.contrib import admin

from .models import Miningservices
from .models import Users
from .models import RequestService
from .models import Requests


admin.site.register(Miningservices)
admin.site.register(Users)
admin.site.register(RequestService)
admin.site.register(Requests)