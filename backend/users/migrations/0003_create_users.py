from django.db import migrations, models
from django.contrib.auth.hashers import make_password
import logging

logger = logging.getLogger(__name__)


def create_profile(user, apps):
    Profile = apps.get_model('users', 'Profile')
    Profile.objects.create(user=user)
    logger.info(f'Created profile for user {user.username}')


def add_user_to_group(user, level, apps):
    Group = apps.get_model('auth', 'Group')
    level_group = Group.objects.get(name=level)
    level_group.user_set.add(user)
    logger.info(f'Successfully added user {user.username} to group {level}')


def create_users(apps, schema_editor):
    levels = ['gold', 'silver', 'bronze']

    try:
        User = apps.get_model('auth', 'User')
        for level in levels:
            user = User.objects.create(
                username=f'{level}', 
                password=make_password(f'{level}')
            )
            logger.info(f'Successfully created user {level}')
            create_profile(user, apps)
            add_user_to_group(user, level, apps)
    except Exception as e:
        logger.warning(f'Error in migration creating Users: {e}')


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_create_reports'),
        ('users', '0002_auto_20200114_1142'),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
