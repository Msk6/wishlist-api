from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import RegisterSerializer, ItemListSerializer, ItemDetailSerializer
from items.models import Item
from rest_framework.filters import SearchFilter, OrderingFilter


class Register(CreateAPIView):
	serializer_class = RegisterSerializer



class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	search_fields = ['name']
	filter_backends = [SearchFilter, OrderingFilter]


class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
