from rest_framework import serializers ,status
from api.serializers_account import CustomUserSerializer
from centre.models import( 
    Booking, EventCentre, EventCentreCategory,
    EventCentreImage  , Hall , HallImage , 
)
from .models import *
from account.models import CustomUser


"""
    !!! INLINE MODEL SERIALIZER
    Let start to create Inline serialization for the model fields 
"""
class EventCentreImageInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCentreImage
        fields = ['image']


class HallImageInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallImage 
        fields= ['image']


class HallInlineSerializer(serializers.ModelSerializer):
    images = HallImageInlineSerializer(read_only=True , many=True) 
    class Meta:
        model = Hall
        fields = ['public_id','name','price', 'is_active', 'status' , 'images']


class EventCentreInlineSerializer(serializers.ModelSerializer):
    images = EventCentreImageInlineSerializer(read_only=True , many=True)   
    class Meta:
        model = EventCentre
        fields = ['public_id','name','slug','location','description','stars','is_active', 'images']

        extra_kwargs = {
            'slug':{'read_only': True},
            'public_id':{'read_only': True},
        }

"""
    !!! EVENT MODELS SERIALIZER
    The serialization of all the event centre model begins
"""
class EventCentreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCentreCategory
        fields = ['public_id', 'name', 'slug']

        extra_kwargs = {
            'slug':{'read_only': True},
            'public_id':{'read_only': True},
        }


class EventCentreSerializer(serializers.ModelSerializer):
    images = EventCentreImageInlineSerializer(read_only=True , many=True)   
    halls = HallInlineSerializer(read_only=True , many=True)    
    class Meta:
        model = EventCentre
        fields = ['public_id','name','slug','location','description','stars','is_active', 'images' , 'halls' ]


        extra_kwargs = {
            'slug':{'read_only': True},
            'public_id':{'read_only': True},
        }


"""
    !!! HALL MODELS SERIALIZER
    The serialization of all the hall model begins
"""
class HallSerializer(serializers.ModelSerializer):
    images = HallImageInlineSerializer(read_only=True , many=True) 
    event_centre = EventCentreInlineSerializer(read_only=True)
    centre_public_id = serializers.CharField(write_only=True)
    class Meta:
        model = Hall
        fields = ['public_id', 'name' , 'slug' ,'price', 'has_payment_category', 'is_active' , 'status', 'images' , 'event_centre' , 'centre_public_id']


        extra_kwargs = {
            'slug':{'read_only': True}, 
            'public_id':{'read_only': True}, 
            'centre_public_id':{'write_only': True}, 
        }


    def create(self , validated_data):
        hall_name = validated_data['name']
        has_payment_category = validated_data['has_payment_category']
        is_active = validated_data['is_active']
        status = validated_data['status']
        price = validated_data['price']
        centre_public_id = validated_data['centre_public_id']

        if EventCentre.objects.filter(public_id=centre_public_id).exists():
            hall_centre_object = EventCentre.objects.get(public_id=centre_public_id)
            new_hall = Hall(name=hall_name ,price=price,status=status , is_active=is_active , event_centre=hall_centre_object)
            new_hall.save()
            return new_hall  
        raise serializers.ValidationError({'error' : 'Hall centre does not exist'})

 

class BookingSerializer(serializers.ModelSerializer): 
    hall_public_id = serializers.CharField(write_only=True)
    hall = HallInlineSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = [ 'public_id' , 'access_ref' , 'event_date','payment_status','hall' ,'hall_public_id' , 'user' ]

        extra_kwargs = {
            'access_ref':{'read_only': True}, 
            'public_id':{'read_only': True}, 
            'payment_status' :{'read_only': True}, 
            'user':{'read_only': True}, 
        }


    def create(self, validated_data):
        request = self.context.get('request')
        hall_public_id = validated_data.get('hall_public_id', None)
        date = validated_data.get('event_date', None)
        try :
            user = CustomUser.objects.get(id=request.user.id)
        except :
           raise serializers.ValidationError({'error' : 'Authentication credentials not provided'}) 
        try:
            hall =  Hall.objects.get(public_id=hall_public_id)
        except:
            raise serializers.ValidationError({'error' : 'Hall  does not exist'})

        has_booked = Booking.objects.filter(event_date=validated_data['event_date'], payment_status=True , hall=hall ).count()
        if has_booked > 0 :
            raise serializers.ValidationError({'error': 'The choosing hall is not open on your booked date','status': status.HTTP_400_BAD_REQUEST})
        new_booking = Booking(user=user , hall=hall , event_date=date)
        new_booking.save()
        return new_booking


        
