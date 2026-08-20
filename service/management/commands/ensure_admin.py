import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create or update the Django admin account from environment variables."

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_ADMIN_USERNAME")
        password = os.environ.get("DJANGO_ADMIN_PASSWORD")
        email = os.environ.get("DJANGO_ADMIN_EMAIL", "")

        if not username or not password:
            self.stdout.write(
                self.style.WARNING(
                    "DJANGO_ADMIN_USERNAME or DJANGO_ADMIN_PASSWORD is not set; skipping admin bootstrap."
                )
            )
            return

        User = get_user_model()
        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email},
        )

        if email and user.email != email:
            user.email = email

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        action = "created" if created else "updated"
        self.stdout.write(self.style.SUCCESS(f"Admin user '{username}' {action} successfully."))
