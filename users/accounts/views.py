from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail

from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .models import CustomUser 
from .serializers import UserSerializer



user = get_user_model() # get CustomUser


class UserLoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] # user=email
        token,created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key},status=status.HTTP_200_OK)


class UserLogoutAPI(APIView):

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ChangePasswordAPI(APIView):
    def put(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        if not user.chack_password(data.get('old_password')):
            return Response({'message':'old password was wrong'},status=status.HTTP_400_BAD_REQUEST)
        
        # update password
        user.set_password(data.get('new_password'))
        user.save()
        return Response({'message':' password was chages succesfully'},status=status.HTTP_200_OK)
        

class ResendActivationCodeAPI(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            user = user.object.get(email=email)
        except Exception as e:
            return Response({'error':e},status=status.HTTP_400_BAD_REQUEST)

        if user.is_activate:
            return Response({'error':'user account is already activeted'},status=status.HTTP_400_BAD_REQUEST)

        # activation link
        current_site = get_current_site(request) # get domain
        mail_subject = 'Activate Your Account'
        
        # render email content in html template
        message = render_to_string('accounts/activate_email.html',{
            'user':user,
            'domain':current_site.domain,
            'uid':urlsafe_base64_decode(force_bytes(user.id)),
            'token':default_token_generator.make_token(user)
        })
        to_email = user.email
        send_mail(mail_subject,message,'ahmedalgohary1170@gmail.com',[to_email])
        return Response({'success':'User was registered successfully , please check your email'},status=status.HTTP_201_CREATED)


class ResetPasswordAPI(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            user = user.object.get(email=email)
        except Exception as e:
            return Response({'error':e},status=status.HTTP_400_BAD_REQUEST)


        # activation link
        current_site = get_current_site(request) # get domain
        mail_subject = 'Reset your password'
        
        # render email content in html template
        message = render_to_string('accounts/password_reset_email.html',{
            'user':user,
            'domain':current_site.domain,
            'uid':urlsafe_base64_decode(force_bytes(user.id)),
            'token':default_token_generator.make_token(user)
        })
        to_email = user.email
        send_mail(mail_subject,message,'ahmedalgohary1170@gmail.com',[to_email])
        return Response({'success':'User was registered successfully , please check your email'},status=status.HTTP_201_CREATED)


class UserSingupAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()

            # activation link
            current_site = get_current_site(request) # get domain
            mail_subject = 'Activate Your Account'
            
            # render email content in html template
            message = render_to_string('accounts/activate_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_decode(force_bytes(user.id)),
                'token':default_token_generator.make_token(user)
            })
            to_email = user.email
            send_mail(mail_subject,message,'ahmedalgohary1170@gmail.com',[to_email])
            return Response({'success':'User was registered successfully , please check your email'},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)

        return Response(serializer.data,status=status.HTTP_200_OK)

