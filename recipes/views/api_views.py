from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
 
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
 
 
class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
 
    def get_queryset(self):
        if self.request.user.is_staff:
            return Recipe.objects.all()
 
        if self.request.user.is_authenticated:
            return Recipe.objects.filter(
                Q(author=self.request.user) |
                Q(is_published=True)
            )
 
        return Recipe.objects.filter(is_published=True)
 
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
 