from django_forest.utils.collection import Collection


class Comics(Collection):

    is_searchable = True
    is_read_only = True

    def load(self):
        self.name = 'comics'
        self.fields = [
            {
                'field': 'id',
                'type': 'Number',
                'is_sortable': True
            },
            {
                'field': 'label',
                'type': 'String'
            },
            {
                'field': 'price',
                'type': 'Number'
            },
        ]


Collection.register(Comics)
