from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import Articleserializer

# Create your views here.

@csrf_exempt
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = Articleserializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Articleserializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def article_details(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExit:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Articleserializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data =  JSONParser().parse(request)
        serializer = Articleserializer(Article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)








