from django.http import JsonResponse
from django.db.models import Sum, F

from django_forest.resources.views.list import ListView
from django_forest.utils.views.action import ActionView
from django_forest.utils.collection import Collection

# from django.http import QueryDict


# Considered as no possible
class ProductsView(ListView):
    def get(self, request, *args, **kwargs):
        # the redefinition of the search param
        request.GET._mutable = True
        request.GET["sort"] = request.GET["sort"].replace("price", "total")
        request.GET["sort"] = request.GET["sort"].replace("reference", "label")
        request.GET._mutable = False
        # request.GET['sort'] = request.GET['sort'].replace($smart_field_name, sorting_field)

        return super().get(request)
    #     response = super().get(request)
    #     return response

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, "products", *args, **kwargs)

    # def enhance_queryset(self, queryset, Model, params, request, apply_pagination=True):
    #     # scopes + filter + search
    #     queryset = self.filter_queryset(queryset, Model, params, request)

    #     # queryset = queryset.annotate(total=Sum(F("price") + F("price")))
    #     # sort
    #     if "sort" in params:
    #         queryset = queryset.order_by(params["sort"].replace(".", "__"))

    #     # segment
    #     if "segment" in params:
    #         collection = Collection._registry[Model._meta.db_table]
    #         segment = next(
    #             (x for x in collection.segments if x["name"] == params["segment"]), None
    #         )
    #         if segment is not None and "where" in segment:
    #             queryset = queryset.filter(segment["where"]())

    #     # limit fields
    #     queryset = self.handle_limit_fields(params, Model, queryset)

    #     # pagination
    #     if apply_pagination:
    #         queryset = self.get_pagination(params, queryset)

    #     return queryset


class ProductSmartActionHook(ActionView):
    def post(self, request, *args, **kwargs):
        return JsonResponse({"success": "fail successfully !"})


class ProductSmartActionHookLoad(ActionView):
    def post(self, request, *args, **kwargs):
        return JsonResponse({"success": "fail successfully !"})
