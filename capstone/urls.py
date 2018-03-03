"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from pages import views as p_views
from key_generator import views as k_views
from accounts import views as a_views
from learning_modules import views as l_views
from tuner import views as t_views
from tonegenerator import views as t_g_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', p_views.index, name='home'),
    url(r'^about/?$', p_views.about, name='about'),
    url(r'^contact/?$', p_views.contact, name='contact'),
    url(r'^theory/?$', p_views.theory, name='theory'),
    url(r'^circle_of_fifths/?$', k_views.circle_of_fifths_selector, name='circle_of_fifths'),
    url(r'^tuner/?$', t_views.tuner, name='tuner'),
    url(r'^register/?$', a_views.register, name='register'),
    url(r'^dashboard/(?P<mbr>[-\w\D]+)/?$', a_views.dashboard, name='dashboard'),
    url(r'^login/?$', p_views.log_in, name='login'),
    url(r'^logout/?$', p_views.logout_view, name='logout'),
    url(r'^tone_generator/?$', t_g_views.tone_generator, name='tone generator'),
    url(r'^lesson1_1/?$', l_views.lesson1_1, name='lesson1.1'),
    url(r'^lesson1_2/?$', l_views.lesson1_2, name='lesson1.2'),
    url(r'^lesson1_3/?$', l_views.lesson1_3, name='lesson1.3'),
    url(r'^lesson2_1/?$', l_views.lesson2_1, name='lesson2.1'),
    url(r'^lesson3_1/?$', l_views.lesson3_1, name='lesson3.1'),
    url(r'^lesson3_2/?$', l_views.lesson3_2, name='lesson3.2'),
    url(r'^lesson4_1/?$', l_views.lesson4_1, name='lesson4.1'),
    url(r'^lesson4_2/?$', l_views.lesson4_2, name='lesson4.2'),
    url(r'^lesson4_3/?$', l_views.lesson4_3, name='lesson4.3'),
    url(r'^lesson4_4/?$', l_views.lesson4_4, name='lesson4.4'),
    url(r'^lesson5_1/?$', l_views.lesson5_1, name='lesson5.1'),
    url(r'^lesson6_1/?$', l_views.lesson6_1, name='lesson6.1'),
    url(r'^lesson6_2/?$', l_views.lesson6_2, name='lesson6.2'),
    url(r'^lesson6_3/?$', l_views.lesson6_3, name='lesson6.3'),
    url(r'^lesson7_1/?$', l_views.lesson7_1, name='lesson7.1'),
    url(r'^lesson8_1/?$', l_views.lesson8_1, name='lesson8.1'),
    url(r'^lesson9_1/?$', l_views.lesson9_1, name='lesson9.1'),
    url(r'^lesson10_1/?$', l_views.lesson10_1, name='lesson10.1'),
    url(r'^lesson10_2/?$', l_views.lesson10_2, name='lesson10.2'),
    url(r'^lesson10_3/?$', l_views.lesson10_3, name='lesson10.3'),
    url(r'^lesson11_1/?$', l_views.lesson11_1, name='lesson11.1'),
    url(r'^lesson11_2/?$', l_views.lesson11_2, name='lesson11.2'),
    url(r'^lesson11_3/?$', l_views.lesson11_3, name='lesson11.3'),
    url(r'^lesson12_1/?$', l_views.lesson12_1, name='lesson12.1'),
    url(r'^lesson13_1/?$', l_views.lesson13_1, name='lesson13.1'),
    url(r'^lesson13_2/?$', l_views.lesson13_2, name='lesson13.2'),
    url(r'^lesson13_3/?$', l_views.lesson13_3, name='lesson13.3'),
    url(r'^lesson13_4/?$', l_views.lesson13_4, name='lesson13.4'),
    url(r'^lesson14_1/?$', l_views.lesson14_1, name='lesson14.1'),
    url(r'^lesson14_2/?$', l_views.lesson14_2, name='lesson14.2'),
    url(r'^lesson14_3/?$', l_views.lesson14_3, name='lesson14.3'),
    url(r'^lesson14_4/?$', l_views.lesson14_4, name='lesson14.4'),
    url(r'^lesson14_5/?$', l_views.lesson14_5, name='lesson14.5'),
    url(r'^lesson14_6/?$', l_views.lesson14_6, name='lesson14.6'),
    url(r'^lesson14_7/?$', l_views.lesson14_7, name='lesson14.7'),
    url(r'^tuner2/?$', t_views.tuner2, name='Test Tuner'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
