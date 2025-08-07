from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Product, Cart, CartItem, Order
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    CartSerializer,
    CartItemSerializer,
    OrderSerializer
)

# ---------------------- Category ViewSet ----------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  # Anyone can view categories

# ---------------------- Product ViewSet -----------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  # Products are public

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category']             # Filter by category id
    ordering_fields = ['price', 'name']         # Sort by price or name
    ordering = ['name']                         # Default sorting

# ---------------------- Cart ViewSet --------------------------
class CartViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]      # Authenticated users only

# ---------------------- CartItem ViewSet ----------------------
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]      # Authenticated users only

# ---------------------- Order ViewSet -------------------------
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]      # Authenticated users only
