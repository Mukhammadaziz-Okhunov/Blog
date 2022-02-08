from django.contrib import admin
from django.urls import path
from blog1.views import home, about, blog, maqola

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('blog/', blog),
    path('maqola/<int:son>', maqola),
]
