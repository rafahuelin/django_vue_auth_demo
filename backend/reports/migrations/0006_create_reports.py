from django.db import migrations, models
import logging

logger = logging.getLogger(__name__)


def create_reports(apps, schema_editor):
    levels = ['gold', 'silver', 'bronze']

    try:
        Report = apps.get_model('reports', 'Report')
        for level in levels:
            report, created = Report.objects.get_or_create(
                title=f'{level} report',
                content=f'{level} content',
                minimum_access_level=level,
            )
            logger.info(f'Successfully created report {level}') if created else None
    except Exception as e:
        logger.warning(f'Error in migration creating Reports: {e}')


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_create_groups'),
    ]

    operations = [
        migrations.RunPython(create_reports),
    ]
