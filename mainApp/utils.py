from .models import PlotHistory
from rest_framework import status
from django.contrib.auth.models import User
import json

def add_plot_or_400(request):
    params=request.data
    obj=PlotHistory.objects.create(user=request.user, points=json.loads(params['points']))
    obj.save()
    return [event,status.HTTP_201_CREATED]


def delete_plot_or_404(request):
    params=request.data
    if('all' in params and params['all'].lower()=="true"):
        PlotHistory.objects.filter(user=request.user).delete()
        return status.HTTP_200_OK
    else:
        if('plot_id' in params):
            if(PlotHistory.objects.filter(user=request.user, pk=params['plot_id']).count()>0):
                PlotHistory.objects.get(user=request.user, pk=params['plot_id']).delete()
                return status.HTTP_200_OK
            else:
                return status.HTTP_404_NOT_FOUND
        else:
            return status.HTTP_400_BAD_REQUEST
