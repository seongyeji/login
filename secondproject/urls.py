from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('blog/<int:blog_id>', blog.views.detail, name='detail'),
        # 패스컴버터
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create', blog.views.create, name='create'),
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
    path('accounts/signup' , accounts.views.signup,name="signup"),
    path('accounts/login' , accounts.views.login,name="login"),
    path('accounts/logout/', accounts.views.logout, name='logout'),
    # path('accounts/', include('accounts.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)