from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from itsdangerous.url_safe import URLSafeTimedSerializer
from django.conf import settings
from User.serializers import UserSerializer


class UserListCreateView(APIView):
    model = User
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.serializer_class(self.model.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(is_aktive=False)

        token = URLSafeTimedSerializer(settings.SECRET_KEY)
        serialized_token = token.dumps(

            {"email": serializer.data["email"],
             "username": serializer.data["username"]
             }
        )
        print(serialized_token)

        verify_url = f"{settings.BASE_URL}/users/verify_token?token={serialized_token}"

        send_mail(
            "Verification",
            message="",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[serializer.data["email"]],
            html_message=f"<a href={verify_url}>Click To Verify.</a>"
        )

        return Response(serializer.data)


class UserRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserVerification(APIView):

    def get(self, request):
        _token = request.GET.get("token")

        if not _token:
            return Response(
                dict(message="Verification Failed: Token's missing!"),
                status=status.HTTP_400_BAD_REQUEST
            )

        tokenizer = URLSafeTimedSerializer(settings.SECRET_KEY)

        try:
            data = tokenizer.loads(_token, max_age=settings.VERIFICATION_TIME_IN_SECONDS)
        except Exception:
            return Response(
                dict(message="Verification Failed: Token's expired!"),
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = User.objects.get(username=data["username"], email=data["email"])
        except Exception:
            return Response(
                dict(message="Verification Failed: Something bad happened!"),
                status=status.HTTP_400_BAD_REQUEST
            )

        user.is_active = True
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)