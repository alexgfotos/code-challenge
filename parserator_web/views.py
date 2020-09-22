import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        
        if request.method == 'GET':
            r = requests.get('api/parse/', params=request.POST)
        if r.status_code == 200:
            return Response('Yay, it worked')
        return Response('Could not save data')
       
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        # 
        return Response({})

    def parse(self, address):
        usaddress.tag(address)
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        
        return address_components, address_type

