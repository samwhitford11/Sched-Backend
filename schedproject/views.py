from schedules.models import Sched
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SchedSerializer


class SchedViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Sched.objects.all()
    # The serializer class for serializing output
    serializer_class = SchedSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]