from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views

from apps.cart.webhook import webhook
from apps.cart.views import cart_detail, checkout, success
from apps.core.views import frontpage, contact, about, blog, returns_refunds, conditions, delivery_info, faq, brand, filter_data, product_list, load_more_data
from apps.order.views import admin_order_pdf
from apps.store.views import product_detail, category_detail, search
from apps.authentication.views import *

from apps.newsletter.api import api_add_subscriber
from apps.whatsapp.api import api_add_whatsapp
from apps.coupon.api import api_can_use
from apps.store.api import api_add_to_cart, api_remove_from_cart, create_checkout_session, validate_payment

from .sitemaps import StaticViewSitemap, CategorySitemap, ProductSitemap



sitemaps = {'static': StaticViewSitemap, 'product': ProductSitemap, 'category': CategorySitemap}

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('search/', search, name='search'),
    path('cart/', cart_detail, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('hooks/', webhook, name='webhook'),
    path('cart/success/', success, name='success'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('delivery/', delivery_info, name='delivery'),
    path('conditions/', conditions, name='conditions'),
    path('returns/', returns_refunds, name='returns'),
    path('faq/', faq, name='faq'),
    path('brand', brand, name='brand'),
    path('filter-data', filter_data, name='filter_data'),
    path('list', product_list,name='listing'),
    path('load-more-data', load_more_data, name='load_more_data'),
    path('jet/', include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('admin/admin_order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),
    # # path('send_email/', sendEmail),
    # path('email/', include(mail_urls)),

    # Auth

    path('profile/', profile, name='profile'),
    path('coupon/', coupon, name='coupon'),
    path('mysize/', mysize, name='mysize'),
    path('notification', notification, name='notification'),
    path('wallet', wallet, name='wallet'),
    path('myorder/', myorder, name='myorder'),
    path('signup/', register, name='register'),
    path('edit_profile/', editprofile, name='edit'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('activate-user/<uidb64>/<token>', activate_user, name='activate'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # API

    path('api/can_use/', api_can_use, name='api_can_use'),
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('api/validate_payment/', validate_payment, name='validate_payment'),
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),
    path('api/add_whatsapp/', api_add_whatsapp, name='api_add_whatsapp'),

    # Store

    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
