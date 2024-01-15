from django.contrib import admin
from django.urls import path
from .views import backend,create,emp,edit,show,update,hlo
from .views import backend,create,emp,edit,show,destroy,update,desk,abhi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('h123',backend),
    path("abhishek/",create),
    path('emp/',emp),
    path('show/',show),
    path('edit/<int:id>',edit),
    path('update/<int:id>',update),
    # path('delete/<int:id>',destroy)
    path("h/",hlo),
    path('delete/<int:id>',destroy),
    path("desk/",desk),
    path("abhi/",abhi),
    
]
