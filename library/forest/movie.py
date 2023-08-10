from django.db.models import Q
from django_forest.utils.collection import Collection

from library.models import Movies, Categories


class MovieForest(Collection):
    def load(self):
        self.fields = [
            {
                "field": "book_category",
                "type": "String",
                "reference": "categories.id",
                "get": self.book_category
            }
        ]

    def book_category(self, obj):
        if obj.book:
            return obj.book.category
        return None


Collection.register(MovieForest, Movies)
