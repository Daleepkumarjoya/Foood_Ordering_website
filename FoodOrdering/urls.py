
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
admin.site.site_header = "DK FoodShop Admin"
admin.site.site_title = "DK FoodShop Admin Panel"
admin.site.index_title = "Welcome to DK FoodShop Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("FoodShopWebsite.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

