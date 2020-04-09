from .models import PlotHistory
from rest_framework import status
from django.contrib.auth.models import User
import json

def add_plot_or_400(request):
    params=request.POST
    obj=PlotHistory.objects.create(user=request.user, points=json.loads(params['points']))
    obj.save()
    return [obj,status.HTTP_201_CREATED]


def delete_plot_or_404(request):
    params=request.body
    params = json.loads(params.decode('utf-8'))

    # Delete all history
    if('all' in params and params['all'].lower()=="true"):
        PlotHistory.objects.filter(user=request.user).delete()
        return status.HTTP_200_OK
    # Delete according to the query
    else:
        if('plot_id' in params):
            if(PlotHistory.objects.filter(user=request.user, pk=params['plot_id']).count()>0):
                PlotHistory.objects.get(user=request.user, pk=params['plot_id']).delete()
                return status.HTTP_200_OK
            else:
                return status.HTTP_404_NOT_FOUND
        else:
            return status.HTTP_400_BAD_REQUEST
