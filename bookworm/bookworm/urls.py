from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('bookworm.bookstore.urls')),
	path('blog/', include('bookworm.blog.urls')),
	path('', include('bookworm.bookworm_auth.urls')),
	path('account/', include('bookworm.account.urls')),
	path('cart/', include('bookworm.cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
