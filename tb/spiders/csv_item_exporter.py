from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter


class CustomCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        fields_to_export = [
            'goods_url',
            'goods_title',
            'nickname',
            'content',
            'append_comment',
            'videos',
            'photos'
        ]
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter

        kwargs['fields_to_export'] = fields_to_export

        super(CustomCsvItemExporter, self).__init__(*args, **kwargs)
