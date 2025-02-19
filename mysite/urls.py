"""
Al pareser se van agregando las urls o directorios al "path" dentro de mysite que seria la web donde se muestra la plaocacion polls.
Ver lo de "incluide" parese una funcion que agrega las urls...

La path()función espera al menos dos argumentos: routey view /como no la tiene por que le ponemos otra cosa//. La include()función permite 
hacer referencia a otras URLconfs. 
Siempre que Django encuentra include(), corta cualquier parte de la URL que coincida hasta ese punto y envía la cadena restante a
la URLconf incluida para su posterior procesamiento.

Como es de esperarse admin.site.urls, que es una URLconf predefinida que proporciona Django para el sitio de administración predeterminado.
En todos los demas casos se utiliza  include()
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]