from rest_framework import generics
from rest_framework.response import Response

from .models import GeoDataPacket
from .serializers import GeoDataPacketSerializer


class GetGeoDataPacketsByDev(generics.GenericAPIView):
    queryset = GeoDataPacket.objects.all()
    serializer_class = GeoDataPacketSerializer

    def get(self, request, *args, **kwargs):
        dev = self.kwargs.get("dev")
        datas = GeoDataPacket.objects.filter(dev=dev)
        return Response(GeoDataPacketSerializer(datas, many=True).data)

