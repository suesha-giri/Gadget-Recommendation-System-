from django.urls import path
from . import views 

urlpatterns=[
    path('smartwatches/', views.smartwatch, name='smartwatch'),
    path('laptops/', views.laptop, name='laptop'),
    path('smartphones/', views.smartphone, name='smartphone'),
    path('specs/', views.specification, name='specification'),
    path('specs/<int:id>/', views.specification, name='specification'),        
    path('addComment/',views.addComment, name='addComment'),   
    path('addComment/<int:id>/',views.addComment, name='addComment'),
]