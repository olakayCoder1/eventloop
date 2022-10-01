import environ
import requests
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str , force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode
import requests
from .serializers import (  
    EventCentreSerializer,RegisterSerializer , 
    ResetPasswordRequestEmailSerializer,SetNewPasswordSerializer,
    ChangePasswordSerializer , EventCentreCategorySerializer ,
    BookingSerializer,UserLoginSerializer,PaymentTransactionSerializer
    
    )
from centre.models import (
    EventCentre , EventCentreCategory ,
    Booking
)
from account.models import CustomUser 
from payment.models import PaymentTransaction
from rest_framework import generics  
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .functions import send_reset_mail
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.




# This view handle user registration
class UserRegistrationApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


# This view handle user login
class UserLogin(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = request.data.get('email')
            password = request.data.get('password') 
            user = CustomUser.objects.get(email=email)
            if user.check_password(password) :
                if user :
                    token , created = Token.objects.get_or_create(user=user)
                    return Response(
                        { 
                            'token' : token.key,
                            'email' : user.email,
                            'first_name' : user.first_name
                        }, 
                        status=status.HTTP_200_OK
                    )
        return Response({ 'error':'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        

# This view handle password reset link email sending on click on forget password
class ResetPasswordRequestEmailApiView(generics.GenericAPIView):
    serializer_class = ResetPasswordRequestEmailSerializer

    def post(self, request):
        email = request.data['email']
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = CustomUser.objects.get(email=email)
                uuidb64 = urlsafe_base64_encode(force_bytes(user.id))
                token = PasswordResetTokenGenerator().make_token(user)
                mail_send = send_reset_mail(user.email,token ,uuidb64)
                if mail_send:
                    return Response( 
                        {'success':True , 'message': 'Password reset mail sent' },
                        status=status.HTTP_200_OK
                        )
            except:
                return Response( 
                    {'success':True , 'message': 'Password reset mail sent' }, 
                    status=status.HTTP_200_OK
                    )


# This view handle changing of user password on forget password
class SetNewPasswordTokenCheckApi(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    def post(self, request, token , uuidb64 ):
        try:
            id = smart_str(urlsafe_base64_decode(uuidb64))
            user = CustomUser.objects.get(id=id)
            if PasswordResetTokenGenerator().check_token(user, token):
                data = request.data
                serializer = self.serializer_class(data=data)
                serializer.is_valid(raise_exception=True)
                user.set_password(serializer.validated_data['password'])
                user.save() 
                return Response({'success':True , 'message':'Password updated successfully'}, status=status.HTTP_200_OK)
            return Response({'error':'Token is not valid, try again'}, status=status.HTTP_401_UNAUTHORIZED)
        except DjangoUnicodeDecodeError as identifier:
            return Response({'error': 'Token is not valid'}, status=status.HTTP_401_UNAUTHORIZED)



#  This view handle password update within app ( authenticated user)
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [ IsAuthenticated ] 
    model = CustomUser
    permission_classes= (IsAuthenticated,)

    def get_object(self,queryset=None):
        obj = self.request.user
        return obj
        
    def update(self, request, *args, **kwargs):
        self.object=self.get_object()
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'ola_password': ['wrong password']}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response={
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully','data':[]
                }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EventCentreSearchAPIView(generics.ListAPIView):  
    queryset = EventCentre.objects.all()
    serializer_class = EventCentreSerializer

    def get_queryset(self, *args , **kwargs):
        qs = super().get_queryset( *args , **kwargs)
        q = self.request.GET.get("q")
        if q == None :
            return None
        result = qs.search(q)

        return result



class EventCentreCategoriesApiView(generics.ListCreateAPIView):
    queryset = EventCentreCategory.objects.all()
    serializer_class = EventCentreCategorySerializer 


class EventCentreApiView(generics.ListCreateAPIView):
    queryset = EventCentre.objects.all()
    serializer_class = EventCentreSerializer

class EventCentreCreateApiView(APIView):
    def post(self , request):
        data = request.data
        images = data.pop('images')
        serializer = EventCentreSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_centre = serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)


class EventCentreBookingApiView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PaymentTransactionApiView(APIView):
    def post(self,request):
        serializer = PaymentTransactionSerializer(
            data = request.data, context={'request':request}
        )
        serializer.is_valid(raise_exception=True)
        res = serializer.save()
        return Response(res)
  


class PaymentTransactionApiView(APIView):
    def get(self,request , reference):
        env = environ.Env()
        environ.Env.read_env()
        payment = PaymentTransaction.objects.get( payment_reference=reference , book__user__id=request.user.id )
        reference = payment.payment_reference
        url = 'https://api.paystack.co/transaction/verify/{}'.format(reference)
        paystack_key = env('settings.PAYSTACK_SECRET_KEY')
        headers = {
            {'authorization': f'Bearer { paystack_key }' }
        }
        r = requests.get(url , headers=headers)
        response = r.json()
        if response['data']['status'] == 'success':
            amount = response['data']['amount'] 
            payment.status = 'success'
            payment.amount = amount

            payment.save()

            return Response(response)
        return Response(response)
 