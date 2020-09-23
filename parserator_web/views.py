import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError
from django.http import JsonResponse

addr = "215 N norton ave tucson az 85719"
print(usaddress.tag(addr))


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request): 
        query = request.GET.get('address')
        addressComponents = usaddress.parse(query)
        print(addressComponents)
        # This will call the parse method when request is sent from the index.html form    
       
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        # 
        return Response(addressComponents)

    def parse(self, address):
        
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        
        # this should receieve an address from the GET request, parse the address, and return JSON using serializer
        
        usaddress.tag(address)
        #and then serialize?

        return address_components, address_type

