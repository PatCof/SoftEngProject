from django.contrib.auth.backends import BaseBackend
from .models import Teachers


class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Teachers.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except Teachers.DoesNotExist:
            return None