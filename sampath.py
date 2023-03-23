# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.hashers import make_password

# user = User.objects.get(phone = phone)


# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


# h = make_password("sampath")


# def perform_create(self, serializer):
#        # Hash password but passwords are not required
#        if ('password' in self.request.data):
#             password = make_password(self.request.data['password'])
#             serializer.save(password=password)
#         else:
#             serializer.save()
