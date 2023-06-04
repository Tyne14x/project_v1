from django.urls import path
from app_iso import views #ดึงฟังก์ชันจาก views มา
#iso

urlpatterns = [
    path('',views.HomePage,name='home-page'),
    path('news',views.NewsBlog,name='news-page'),
    path('register/',views.Register,name='register-page'),
    path('contact',views.Contact,name="contact"),
    path('document',views.Document,name="document"),
]