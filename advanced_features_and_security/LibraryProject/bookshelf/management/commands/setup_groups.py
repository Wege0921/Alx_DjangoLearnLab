from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Set up user groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        editors_group, created = Group.objects.get_or_create(name='Editors')
        viewers_group, created = Group.objects.get_or_create(name='Viewers')
        admins_group, created = Group.objects.get_or_create(name='Admins')

        # Assign permissions to Editors group
        can_edit = Permission.objects.get(codename='can_edit', content_type__app_label='bookshelf', content_type__model='book')
        can_create = Permission.objects.get(codename='can_create', content_type__app_label='bookshelf', content_type__model='book')
        editors_group.permissions.add(can_edit, can_create)

        # Assign permissions to Viewers group
        can_view = Permission.objects.get(codename='can_view', content_type__app_label='bookshelf', content_type__model='book')
        viewers_group.permissions.add(can_view)

        # Assign all permissions to Admins group
        can_delete = Permission.objects.get(codename='can_delete', content_type__app_label='bookshelf', content_type__model='book')
        admins_group.permissions.add(can_view, can_create, can_edit, can_delete)

        self.stdout.write(self.style.SUCCESS('Groups and permissions have been set up successfully.'))

