from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        # TODO add desc for each args
        parser.add_argument('app_model', type=str)
        parser.add_argument('--order', type=str, default='pk')
        parser.add_argument('--fields', type=str)
        parser.add_argument('--exclude_fields', type=str)
        parser.add_argument('--filter', type=str)
        parser.add_argument('--limit', type=int)
        parser.add_argument('--database', type=str)
        parser.add_argument('--format', type=str)

    def handle(self, *args, **options):
        app_model = options['app_model']
        fields = options['fields']
        exclude_fields = options['exclude_fields']
        order = options['order']
        filters = self.get_filter_dict(options['filter'])
        limit = options['limit']
        database = options['database'] or 'default'
        format = options['format']

    def normalize_filter_string(self, filter_string):
        pass

    def normalize_order_string(self, order):
        pass

    def get_model_fields(self, model):
        pass

    def get_dump_structure(self, app_model, records, Model, format):
        pass
