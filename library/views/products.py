from django.http import JsonResponse

from django_forest.resources.views.list import ListView
from django_forest.utils.views.action import ActionView
from django.http import QueryDict


# Considered as no possible
class ProductsView(ListView):
    def get(self, request, *args, **kwargs):
        request.GET._mutable = True
        # the redefinition of the search param
        request.GET['sort'] = request.GET['sort'].replace("reference", "label")
        request.GET._mutable = False

        # query_dict = QueryDict('', mutable=True)
        # query_dict.update(params)
        # request.GET = query_dict

        response = super().get(request)
        return response

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, "products", *args, **kwargs)


class ProductSmartActionHook(ActionView):
    def post(self, request, *args, **kwargs):
        return JsonResponse({'success': 'fail successfully !'})

class ProductSmartActionHookLoad(ActionView):
    def post(self, request, *args, **kwargs):
        return JsonResponse({'success': 'fail successfully !'})