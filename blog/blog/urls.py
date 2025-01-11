
from django.contrib import admin
from django.urls import path
from task1.views import main, reg, enter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('reg/', reg, name='registration_page'),
    path('enter/', enter, name='enter_page')

]
