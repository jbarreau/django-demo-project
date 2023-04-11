import json
import tempfile

from django.http import JsonResponse, HttpResponse
from django.views import generic

from django_forest.utils.views.action import ActionView
from django_forest.resources.utils.queryset import PaginationMixin
from django_forest.utils import get_token
from django_forest.utils.schema.json_api_schema import JsonApiSchema

from library.models import Books, Users, Bookstores


class BooksActionSingleView(ActionView):
    def post(self, request, *args, **kwargs):
        ids = self.get_ids_from_request(request, self.Model)
        book = Books.objects.get(id=ids[0])  # because it is a single action
        book.active = True
        book.save()

        return JsonResponse({"success": f"{book.id} is now active !"})


class BooksActionBulkView(ActionView):
    def post(self, request, *args, **kwargs):
        ids = self.get_ids_from_request(request, self.Model)
        books = Books.objects.filter(id__in=ids)  # because it is a bulk action

        nb = books.update(other="update with smart action bulk")

        return JsonResponse({"success": f"{nb} books updated"})


class BooksActionGlobalView(ActionView):
    def post(self, request, *args, **kwargs):
        books = Books.objects.filter(
            active=True
        )  # because it is a global action, no ids

        nb = books.update(active=False)

        return JsonResponse({"success": f"active books({nb}) are now inactive"})


class BooksActionDownloadView(ActionView):
    def post(self, request, *args, **kwargs):
        with tempfile.TemporaryFile() as fp:
            fp.write('{"headers":{}}'.encode("utf8"))
            fp.seek(0)
            response = HttpResponse(fp.read(), content_type="application/json")
        response["Content-Disposition"] = "inline; filename=file.json"
        return response


class BooksAddCommentView(ActionView):
    def post(self, request, *args, **kwargs):
        ids = self.get_ids_from_request(request, self.Model)
        params = json.loads(request.body.decode("utf8"))
        token = get_token(request)
        book = Books.objects.get(id=ids[0])  # because it is a single action
        book.comments_set.create(
            body=params["data"]["attributes"]["values"]["body"],
            user=Users.objects.get_or_create(
                email=token["email"],
                defaults={"name": f"{token['first_name']} {token['last_name']}"},
            )[0],
        )

        return JsonResponse(
            {"success": "Comment created", "refresh": {"relationship": ["comments"]}}
        )

class SmartBookStoreView(PaginationMixin, generic.ListView):
    def get(self, request, pk, *args, **kwargs):
        params = request.GET.dict()
        queryset = Bookstores.objects.filter(company__book_id=pk).distinct()

        # pagination
        queryset = self.get_pagination(params, queryset)

        # json api serializer
        Schema = JsonApiSchema.get('bookstores')
        data = Schema().dump(queryset, many=True)

        return JsonResponse(data, safe=False)