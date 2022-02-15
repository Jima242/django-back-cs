from rest_framework.views import APIView
from rest_framework.response import Response

from primerComponente.models import PrimerModelo

from primerComponente.serializer import PrimerTablaSerializer

# Create your views here.
class PrimerViewList(APIView):
    def get(self, request, format=None):
        querySet = PrimerModelo.object.all()
        serializer = PrimerTablaSerializer(querySet, many=True, context={'request':request})
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Error guardado")
            