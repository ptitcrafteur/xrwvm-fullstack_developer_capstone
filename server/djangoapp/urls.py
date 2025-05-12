# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
    path(route='login', view=views.login_user, name='login'),

    # path for logout
    path("logout", views.logout_request, name="logout"),

    # path for register
    path("register", views.registration, name="register"),
    
    # path for dealer reviews view

    # path for add a review view

    #path to get cars
    path('get_cars', view=views.get_cars, name ='getcars'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
