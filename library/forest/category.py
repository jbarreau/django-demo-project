from django.db.models import Q
from django_forest.utils.collection import Collection

from library.models import Categories

class CategoryForest(Collection):
    def load(self):
        self.segments = [{"name": "bestNames", "where": self.best_names}]

    def best_names(self):
        return Q(label="Benedict Bruen MD")

Collection.register(CategoryForest, Categories)