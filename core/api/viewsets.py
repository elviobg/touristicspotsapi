from rest_framework import viewsets
from touristic_spots.core.models import Spot
from touristic_spots.core.api.serializers import SpotSerializer


class SpotViewSet(viewsets.ModelViewSet):
    # queryset = Spot.objects.all().order_by('-id')
    serializer_class = SpotSerializer

    def get_queryset(self):
        params = self.request.query_params
        pk = params.get('id', None)
        name = params.get('name', None)
        description = params.get('description', None)
        querySet = Spot.objects.all().filter(approved=True)

        if pk:
            querySet = querySet.filter(pk=pk)
        if name:
            querySet = querySet.filter(name__icontains=name)
        if description:
            querySet = querySet.filter(description__icontains=description)
        return querySet

    # método de sobrescrita das chamadas padrão
    # list, create, destroy, retrieve, update, partial_update
    def list(self, request, *args, **kwargs):
        return super(SpotViewSet, self).list(request, *args, **kwargs)
