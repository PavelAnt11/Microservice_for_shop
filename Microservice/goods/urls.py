from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
# Следующий шаг – добавить ссылку на goods.urls в главной конфигурации URL-ов.