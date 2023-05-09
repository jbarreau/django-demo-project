from django_forest.utils.collection import Collection


class CustomerStat(Collection):

    is_searchable = True

    def load(self):
        self.name = 'CustomerStat'
        self.fields = [
            {
                'field': 'id',
                'type': 'Number',
            },
            {
                'field': 'email',
                'type': 'String'
            },
            # {
            #     'field': 'orders_count',
            #     'type': 'Number'
            # },
            # {
            #     'field': 'total_count',
            #     'type': 'Number'
            # }
        ]


Collection.register(CustomerStat)