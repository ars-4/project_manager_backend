from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



def get_or_create_token(user):
    user = User.objects.get(username=user)
    token = Token.objects.filter(user=user)
    if len(token) > 0:
        return token[0]
    else:
        token = Token.objects.create(user=user)
        return token
