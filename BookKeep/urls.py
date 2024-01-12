from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.views import home,landingPage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingPage,name="landing_page"),
    path('home/', home,name="home"),
    # path('home/<slug:cat_id>/', home,name="book_cat"),
    path('home/<slug:cat_id>/',home,name='book_cat'),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
