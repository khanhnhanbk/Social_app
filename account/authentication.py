from django.contrib.auth.models import User

from .models import Profile


class EmailAuthBackend:
    """Authenticate using an e-mail address"""

    def authenticate(self, request, username=None, password=None):
        """Authenticate a user"""
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Get a User object from the user_id"""
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def create_profile(backend, user, *args, **kwargs):
    """Create a user profile when a new user account is created"""
    Profile.objects.get_or_create(user=user)
