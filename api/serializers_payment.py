import requests
import environ
from rest_framework import serializers
from .models import *
from payment.models import PaymentTransaction









class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = ['id','book','amount', 'payment_reference', 'status' ,'created_at']

    def save(self):
        env = environ.Env()
        environ.Env.read_env()
        url = 'https://api.paystack.co/tarnsaction/initialize'
        paystack_key = env('settings.PAYSTACK_SECRET_KEY')
        header = {
            { 'authorization': f'Bearer  { paystack_key } ' } 

        }
        data = {
            'amount':self.validated_data['amount'],
            'email': self.context['request'].user.email
        }
        r = requests.post(url, headers=header , data=data)
        response = r.json()

        PaymentTransaction.objects.create(
            status = 'pending',
            book = self.validated_data['book'],
            amount = data['amount'],
            payment_reference = response['data']['reference']
        )
        return response

