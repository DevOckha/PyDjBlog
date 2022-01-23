from unicodedata import name
from django.urls import path
from .views import HomePageView, AboutPageView, CategoryListView, PostDeailView, SearcListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),# class tabanlı olarak tanımladığımız görünümlerimize as_view() eklememizim sebebi django'nun url
    path('index/', HomePageView.as_view(), name='index'), # çözümleyicisinin class tabanlı görünümleri çözümleyememesinden kaynaklanmaktadır. as_view() ile view class'ından görünüm işlevi çağrılır.
    path('about/', AboutPageView.as_view(), name='about'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='to_category'),
    path('post/<slug:slug>/', PostDeailView.as_view(), name='to_post'),
    path('search/', SearcListView.as_view(), name='search'),
]