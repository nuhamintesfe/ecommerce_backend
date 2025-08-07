from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .models import Category, Product, Cart, CartItem, Order
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    CartSerializer,
    CartItemSerializer,
    OrderSerializer
)

# ---------------------- Pagination ----------------------
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# ---------------------- Category ViewSet ----------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
# ---------------------- Product ViewSet -----------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    # Correct and complete filter backends
    filter_backends = [
        DjangoFilterBackend,  # Enables `filterset_fields`
        filters.SearchFilter,  # Enables `search_fields`
        filters.OrderingFilter  # Enables `ordering_fields`
    ]

    # Filtering
    filterset_fields = ['category']  # Enables ?category=<id>

    # Searching
    search_fields = ['name', 'description', 'category__name']  # Enables ?search=...

    # Ordering
    ordering_fields = ['price', 'name', 'stock']  # Enables ?ordering=price or ?ordering=-price
    ordering = ['name']  # Default ordering

    # Pagination
    pagination_class = StandardResultsSetPagination

# ---------------------- Cart ViewSet --------------------------
class CartViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

# ---------------------- CartItem ViewSet ----------------------
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

# ---------------------- Order ViewSet -------------------------
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
