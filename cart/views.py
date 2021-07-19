from cart.serializers import OfferTypeAndValueSerializer, itemDetailsSerializer, myOrderSerializer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework import status

@csrf_exempt
def totalOrderValue(request):
    slab = {'0' : 50, '1': 100, '2': 500, '3': 500, '4': 500, '5': 1000}
    if request.method == 'POST':

        data = JSONParser().parse(request)
        items_serialized_data = itemDetailsSerializer(data=data['order_items'], many=True)
        offer_serialized_data = OfferTypeAndValueSerializer(data = data['offer'])
        order_serialized_data = myOrderSerializer(data = data)

        if items_serialized_data.is_valid() and offer_serialized_data.is_valid() and order_serialized_data.is_valid():
            total_amount = 0

            # calculating item-total-price
            for item in data['order_items']:
                total_amount += item['quantity'] * item['price']

            # calculating delivery charges
            distance = data['distance']/1000
            temp = int(distance//10)
            if temp >= 5:
                delivery_charges = 1000*100
            else:
                delivery_charges = slab[str(temp)]*100

            # checking offers
            if data['offer']['type'] == 'FLAT':
                offer_value = data['offer']['offerValue']
                amount_without_offer = total_amount + delivery_charges
                final_amount = amount_without_offer - min(amount_without_offer, offer_value)
                total_value = {'order_total':final_amount}
                json_data = JSONRenderer().render(total_value)
                return HttpResponse(json_data, status=status.HTTP_200_OK)

            elif data['offer']['type'] == 'DELIVERY':
                total_value = {'order_value':total_amount}
                json_data = JSONRenderer().render(total_value)
                return HttpResponse(json_data, status=status.HTTP_200_OK)
            else:
                total_value = {'order_value':total_amount + delivery_charges}
                json_data = JSONRenderer().render(total_value)
                return HttpResponse(json_data, status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Invalid Data Entered", status=status.HTTP_400_BAD_REQUEST)

            
        

