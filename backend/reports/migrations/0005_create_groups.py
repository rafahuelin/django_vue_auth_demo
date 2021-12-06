from django.db import migrations, models
import logging

logger = logging.getLogger(__name__)


def create_groups(apps, schema_editor):
    group_names = ['gold', 'silver', 'bronze']

    try:
        Group = apps.get_model('auth', 'Group')
        for group_name in group_names:
            group, created = Group.objects.get_or_create(name=group_name)
            logger.info(f'Successfully created group {group_name}') if created else None
    except Exception as e:
        logger.warning(f'Error in migration creating Groups: {e}')


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20211206_1114'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
