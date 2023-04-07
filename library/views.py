import json

from django.http import JsonResponse, HttpResponse
from django.views import generic, View
from django.db.models import F
from django_forest.utils.schema.json_api_schema import JsonApiSchema
from django_forest.resources.utils.queryset.pagination import PaginationMixin
from django_forest.resources.utils.queryset.search import SearchMixin

from library.models import Books, Categories
class ComicsView(PaginationMixin, SearchMixin, generic.ListView):

    def get(self, request, *args, **kwargs):
        params = request.GET.dict()

        # queryset
        queryset = Books.objects.filter(difficulty="easy")

        # annotate
        queryset = queryset.annotate(price=F('amount'))  # select price as amount

        # search
        if "search" in params:
            queryset = queryset.filter(self.get_search(params, Books))

        # pagination
        queryset = self.get_pagination(params, queryset)

        # use automatically generated Schema or use your own thanks to marshmallow-jsonapi
        Schema = JsonApiSchema.get('comics')
        data = Schema().dump(queryset, many=True)

        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        post_params = json.loads(request.body.decode("utf-8"))
        attribute = post_params['data']['attributes']
        book = Books.objects.create(
            amount=attribute["price"],
            label=attribute["label"],
            comment="created as comic",
            difficulty="easy",
            active=True,
            options={"foo":"foo"},
            category=Categories.objects.order_by('?').first()
        )

        Schema = JsonApiSchema.get('comics')
        data = Schema().dump(book)

        return JsonResponse(data, safe=False)

    def delete(self, request, *args, **kwargs):
        post_params = json.loads(request.body.decode("utf-8"))

        Books.objects.filter(id__in=post_params["data"]["attributes"]["ids"]).delete()
        return HttpResponse(status=204)


class ComicsDetailView(PaginationMixin, View):
    def get(self, request, pk, *args, **kwargs):
        book = Books.objects.annotate(price=F('amount')).get(id=pk)

        Schema = JsonApiSchema.get('comics')
        data = Schema().dump(book)

        return JsonResponse(data, safe=False)


    def delete(self, request, pk, *args, **kwargs):
        Books.objects.filter(id=pk).delete()
        return HttpResponse(status=204)

    def put(self, request, pk, *args, **kwargs):
        post_params = json.loads(request.body.decode("utf-8"))
        attribute = post_params['data']['attributes']

        book = Books.objects.get(id=pk)

        book.label = attribute.get("label", book.label)
        book.amount = attribute.get("price", book.amount)
        book.save()

        Schema = JsonApiSchema.get('comics')
        data = Schema().dump(book)

        return JsonResponse(data)