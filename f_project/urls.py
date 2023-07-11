"""
URL configuration for f_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_app import urls as my_app_urls
from users import urls as users_urls
from my_app.views import index_my_app, login  ## index_main
from f_project import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index_my_app),
    #path('', index_main),
    path('admin/', admin.site.urls),
    path('my_app/', include(my_app_urls)),    # Вложеный список маршрутов
    path('my_app/', include(users_urls)),
    path('login/', login, name='login'),
]

if settings.DEBUG:  ##  Делается для того, чтобы использовать статику (картинки, медиа) в режиме отладки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  ## В "Боевом режиме запускается на другом вэб-сервере"
