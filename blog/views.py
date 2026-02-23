from rest_framework import viewsets, permissions, filters # Add permissions and filters
from .models import Post, Category, Tag
from .serializers import PostSerializer, CategorySerializer, TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    
    # This line makes it so anyone can read, but only logged-in users can write
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'category__name']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]