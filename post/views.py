from django.http import JsonResponse
from django.db.models import Q
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def search_post(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"error": "No query parameter provided"}, status=status.HTTP_400_BAD_REQUEST)

