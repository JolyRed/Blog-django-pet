from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def main(request):
    return render(request, 'main.html')

def reg(request):
    info = {}  # Словарь для сообщений об ошибках
    username = email = password = confirm_password = None  # Инициализация переменных значениями None
    
    if request.method == 'POST':
        # Получаем данные из формы
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Проверка на существование пользователя
        if User.objects.filter(username=username).exists():
            info['error'] = 'Такой пользователь уже существует'
        elif User.objects.filter(email=email).exists():
            info['error'] = 'Пользователь с такой почтой уже существует'
        elif password != confirm_password:
            info['error'] = 'Пароли не совпадают'
        else:
            # Хешируем пароль перед сохранением в базе данных
            hashed_password = make_password(password)

            # Создаем нового пользователя
            user = User.objects.create(username=username, email=email, password=hashed_password)

            # Редиректим на страницу с приветствием
            return HttpResponse(f'Добро пожаловать, {user.username}')

    # Возвращаем форму регистрации с ошибками, если они есть
    return render(request, 'registration_page.html', {'info': info})


def enter(request):
    return render(request, 'enter_page.html')