from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import RegisterSerializer, ItemListSerializer, ItemDetailSerializer
from items.models import Item
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .permissions import IsOwner

class Register(CreateAPIView):
	serializer_class = RegisterSerializer



class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    search_fields = ['name']
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsOwner]
