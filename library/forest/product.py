from django.db.models import Q
from django_forest.utils.collection import Collection
from django_forest.resources.utils.queryset.filters.utils import OPERATORS

from library.models import Products


class ProductsFieldsMixin:
    def load_fields(self):
        return [
            {
                "field": "reference",
                "type": "String",
                "get": self.get_reference,
                "set": self.set_reference,
                "search": self.search_reference,
                "is_filterable": True,
                "filter": self.filter_reference,
                "is_sortable": True,
                # notImplemented, see View Inheritance instead
                # "sort": self.sort_reference,
            }
        ]

    @staticmethod
    def _unsplit_ref(value):
        price, label = "".join(reversed(value)).split("-", 1)
        label = "".join(reversed(label))
        price = "".join(reversed(price))
        try:
            price = float(price)
        except ValueError:
            price = None
        return (label, price)

    def get_reference(self, obj):
        return f"{obj.label}-{obj.price}"

    def set_reference(self, obj, value):
        label, price = ProductsForest._unsplit_ref(value)

        obj.label = label
        obj.price = price
        return obj

    def search_reference(self, search):
        ret = Q(label__icontains=search)
        if "-" in search:
            label, price = ProductsForest._unsplit_ref(search)
            ret |= Q(label__icontains=label)
            if price is not None:
                ret |= Q(price=price)
        else:
            try:
                ret |= Q(price=int(search))
            except ValueError:
                pass
        return ret

    def filter_reference(self, operator, value):
        label, price = ProductsForest._unsplit_ref(value)
        label_kwargs = {f"label{OPERATORS[operator]}": label}

        is_negated = operator.startswith("not")
        if is_negated:
            return ~Q(Q(**label_kwargs))
        return Q(Q(**label_kwargs))


class ProductActionsMixin:
    def load_actions(self):
        return [
            {
                "type": "single",
                "name": "smartActionHook",
                "fields": [
                    {
                        "field": "token",
                        "type": "string",
                        "is_required": True,
                    },
                    {
                        "field": "foo",
                        "type": "string",
                        "is_required": True,
                        "hook": "onFooChange",
                    },
                ],
                "hooks": {
                    "load": self.load_smart_action_hook,
                    "change": {"onFooChange": self.onFooChange},
                },
            },
            {
                "type": "single",
                "name": "smartActionHookLoad",
                "fields": [
                    {
                        "field": "country",
                        "type": "Enum",
                        "is_required": True,
                        "enums": ["Ukraine", "Poland", "Latvia"],
                    },
                ],
            },
        ]

    def load_smart_action_hook(self, fields, request, *args, **kwargs):
        token = next((x for x in fields if x["field"] == "token"), None)
        token["value"] = "default"
        return fields

    def onFooChange(self, fields, request, changed_field, *args, **kwargs):
        token = next((x for x in fields if x["field"] == "token"), None)
        token["value"] = "Test onChange Foo"
        return fields


class ProductsForest(ProductActionsMixin, ProductsFieldsMixin, Collection):
    def load(self):
        self.fields = self.load_fields()
        self.actions = self.load_actions()


Collection.register(ProductsForest, Products)
