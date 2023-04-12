import uuid

from django.views import generic
from django.http import JsonResponse
from django.db.models import F, Min, Count

from library.models import Books


def _render_chart_data(value):
    return {
        "data": {
            "attributes": {"value": value},
            "type": "stats",
            "id": uuid.uuid4(),
        }
    }


def render_chart_value(value):
    return _render_chart_data({"countCurrent": value})


def render_chart_pie(data):
    return _render_chart_data(data)


def render_chart_line(data):
    return _render_chart_data(data)


def render_chart_objective(value, objective):
    return _render_chart_data(
        {
            "value": value,
            "objective": objective,
        }
    )


def render_chart_leader_board(data):
    return _render_chart_data(data)


# examples


class ValueChartView(generic.ListView):
    def post(self, request, *args, **kwargs):
        book = Books.objects.get(id=1)
        return JsonResponse(render_chart_value(book.amount), safe=False)


class PieChartView(generic.ListView):
    def post(self, request, *args, **kwargs):
        data = [
            *Books.objects.annotate(key=F("label"), value=F("amount"))[:3].values(
                "key", "value"
            )
        ]
        res = render_chart_pie(data)
        return JsonResponse(res, safe=False)


class LineChartView(generic.ListView):
    def post(self, request, *args, **kwargs):
        data = [
            {"label": book["label"], "values": {"value": book["value"]}}
            for book in Books.objects.filter(id__lte=5)
            .order_by("id")
            .extra(select={"label": "id", "value": "amount"})
            .values("label", "value")
        ]
        return JsonResponse(render_chart_line(data), safe=False)


class ObjectiveChartView(generic.ListView):
    def post(self, request, *args, **kwargs):
        data = Books.objects.filter(amount__lt=100, amount__gt=10).aggregate(
            amount=Min("amount")
        )
        return JsonResponse(render_chart_objective(data["amount"], 100), safe=False)


class LeaderBoardChartView(generic.ListView):
    def post(self, request, *args, **kwargs):
        data = [
            *Books.objects.filter(amount__gt=0, amount__lt=1000)
            .order_by("-amount")
            .extra(select={"key": "id", "value": "amount"})
            .values("key", "value")[:5]
        ]
        return JsonResponse(render_chart_leader_board(data), safe=False)


# more reals example


class NbBookByCategoryChartView(generic.ListView):
    def post(self, request, *args, **kwargs):
        data = [
            *Books.objects.select_related("category")
            .order_by("category__label")
            .values("category__label")
            .annotate(value=Count("category__label"), key=F("category__label"))
            .values("key", "value")
        ]
        res = render_chart_pie(data)
        return JsonResponse(res, safe=False)
