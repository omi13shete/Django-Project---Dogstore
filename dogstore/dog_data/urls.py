from django.contrib import admin
from django.urls import path
from dog_data import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("pricing",views.pricing,name="pricing"),
    path("contactus",views.contact,name="contactus"),
    path("login",views.loginuser,name="login"),
    path("logout",views.logoutuser,name="contactus"),
    path("signup",views.signup,name="signup"),
    path("paymenthandler", views.paymenthandler, name='paymenthandler'),
    path("addpet",views.addpet,name="addpet"),
    path("petdetails",views.petdetails,name="petdetails"),
    path("updatedetails",views.updatedetails,name="updatedetails"),
    path("updatedrecord",views.updatedrecord,name="updatederecord"),
    path("deletedetails",views.deletedetails,name="deletedetails")

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




    

