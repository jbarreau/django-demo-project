from django_forest.utils.collection import Collection

from library.models import Books


class BookForest(Collection):
    def load(self):
        self.search_fields = ["id", "label"]

        self.fields = [
            {
                "field": "smart_bookstores",
                "reference": "bookstores.id",
                'type': ['String'],
            }
        ]

        self.actions = [
            {"type": "single", "name": "action single"},
            {"type": "bulk", "name": "smart action bulk"},
            {"type": "global", "name": "smart action global"},
            {"type": "global", "name": "smart action download", "download": True},
            {
                "type": "single",
                "name": "add-comment",
                "fields": [
                    {"field": "body", "type": "string", "isRequired": True},
                    {
                        "field": "multiple select",
                        "type": ["Enum"],
                        "enums": ["1", "2", "3"],
                        "widget": "checkboxes",
                    },
                ],
            },
        ]


Collection.register(BookForest, Books)
