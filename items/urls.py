from django.urls import path

from items.views import ItemApiView, SpecificItemApiView


urlpatterns = [
    path("", ItemApiView.as_view(), name="items"),
    path("<int:pk>/", SpecificItemApiView.as_view(), name="specific_items"),
]



# URLs en API REST
"""

Path: localhost:8000/items/
Recurso: /items/
El recurso define en donde se va a realizar la acción.
El formato del body es un JSON.

    Items:
        GET: /items/
            Nos va a devolver una lista de items.
        
        GET: /items/<int:pk>/
            Nos va a devolver un item en particular.
            Que va a ser el que le indiquemos por la primary key.

        POST: /items/
            Nos va a permitir crear un nuevo item.
            body:
                {
                    "name": "Item 1",
                    "price": 100,
                    "description": "Item 1 description"
                }

        POST: /items/<int:pk>/
            Nos va a permitir hacer acciones sobre ese item.
            Por ejemplo, comprarlo.
            La accion seria contra otra tabla.
            Body:
                {
                    "action": "buy"
                }

        Alternativa al POST anterior es la siguiente:
            /transactions/items/<int:pk>/
            body:
                {
                    "buyer": 1,
                    "action": "buy"
                }
            response:
                {
                    "redirect": "https://mercadopago.com/nueva_compra"
                }

        GET: /transactions/<int:pk>/
        Nos devuelve una transaccion por ID.


        PUT: /items/<int:pk>/
            body:
                {
                    "name": "Item 1",
                }
        PATCH: /items/<int:pk>/
            body:
                {
                    "name": "Item 1",
                    "price": 100
                }

        DELETE: /items/<int:pk>/

    Obtener la categoría de un item.
    GET: /items/<int:pk>/category/

    PATCH: /items/<int:pk>/category/
        Cambio la categoria del item.

    Delete: /items/<int:pk>/category/
        Elimino la categoria del item y lo dejo sin categoría.


"""