import json

from django.apps import apps
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder


class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument('app_model', type=str,
                            help='the model name to dump data from')
        parser.add_argument('--order', type=str, default='pk',
                            help='field by which dumpped data is ordered')
        parser.add_argument('--fields', type=str,
                            help='list of fields to include in dumpped data',
                            default='*')
        parser.add_argument('--exclude_fields', type=str,
                            help='list of fields to exclude from dumpped data',
                            default=''

                            )
        parser.add_argument(
            '--filter', type=str, help='key/value pairs to apply as filter on dumpped data',
            default=''
            )
        parser.add_argument('--limit', type=int,
                            help='an integer to limit number of records',default=None)
        parser.add_argument('--database', type=str,
                            help='database name to dump data from',default='default')
        parser.add_argument('--format', type=str,default='json',
                            help='the output format of dumpped data e.g: json')

    def handle(self, *args, **options):

        app_model = options['app_model']
        fields = options['fields']
        exclude_fields = options['exclude_fields']
        order = options['order']
        filters = self.normalize_filter_string(options['filter'])
        limit = options['limit']
        database = options['database']
        format = options['format']

        Model = apps.get_model(app_model)

        if fields == '*':
            fields = self.get_model_all_fields(Model)
        else:
            fields = fields.split(',') if fields is not None else []
        if exclude_fields:
            exclude_fields = exclude_fields.split(
                ',') if exclude_fields is not None else []
            for field in exclude_fields:
                if field in fields:
                    fields.remove(field)

        if 'pk' not in fields:
            fields.append('pk')

        records = Model.objects.using(database).all()
        if filters:
            records = records.filter(**filters)

        order_by = self.normalize_order_string(order)

        records = records.order_by(*order_by)
        records = records.values(*fields)
        if limit:
            records = records[:limit]

        dump_structure = self.get_dump_structure(
            app_model, records, fields, Model
        )
        result = json.dumps(dump_structure, cls=DjangoJSONEncoder)
        return result

    def normalize_filter_string(self, filter_string):
        filters = {}
        if filter_string:
            pairs = filter_string.split(',')
            for pair in pairs:
                key, value = pair.split('=')
                filters[key] = value

        return filters

    def normalize_order_string(self, order):
        return order.split(",")

    def get_model_all_fields(self, Model):
        return [field.name for field in Model._meta.fields]

    def get_dump_structure(self, app_model, records, Model, format):
        results = []
        for record in records:
            values = {}
            for key, value in record.items():
                if key != "pk":
                    values[key] = value

            record_structrue = {
                "model": app_model,
                "pk": record.get("pk"),
                "fields": values
            }
            results.append(record_structrue)

        return results
