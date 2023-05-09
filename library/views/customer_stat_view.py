from django.http import JsonResponse
from django.views import generic
from django.db.models import Sum, Count

from django_forest.utils.schema.json_api_schema import JsonApiSchema
from django_forest.resources.utils.queryset.pagination import PaginationMixin
from django_forest.resources.utils.queryset.search import SearchMixin

from library.models import Users

class CustomerStatsView(PaginationMixin, SearchMixin, generic.ListView):

    def get(self, request, *args, **kwargs):
        params = request.GET.dict()

        # queryset
        queryset = Users.objects.all()

        # annotate
        # queryset = queryset.annotate(total_amount=Sum('product__prices'))
        # queryset = queryset.annotate(orders_count=Count('orders'))

        # search
        # queryset = queryset.filter(self.get_search(params, Users)).only("id", "email")
        queryset = queryset.filter().only("id", "email")

        # pagination
        queryset = self.get_pagination(params, queryset)

        # use automatically generated Schema or use your own thanks to marshmallow-jsonapi
        Schema = JsonApiSchema.get('CustomerStat')
        data = Schema().dump(queryset, many=True)

        return JsonResponse(data, safe=False)

