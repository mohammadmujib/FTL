
# views 
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from . serializers import  MemberSerializer,ActivitySerializer


class ListCreateMember(generics.ListCreateAPIView):
    queryset = models.Member.objects.all()
    serializer_class = MemberSerializer


class RetrieveUpdateDestroyMember(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Member.objects.all()
    serializer_class = MemberSerializer

class ListCreateActivity(generics.ListCreateAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return self.queryset.filter(member_id=self.kwargs.get('member_pk'))

    def perform_create(self, serializer):
        member = get_object_or_404(models.Member,
                                   pk=self.kwargs.get('member_pk'))
        serializer.save(member=member)


class RetrieveUpdateDestroyActivity(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(),
                                 member_id=self.kwargs.get('member_pk'),
                                 pk=self.kwargs.get('pk'))

