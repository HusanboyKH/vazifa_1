from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import BookModel,AuthorModel
from rest_framework.response import Response
from .serializers import BookSerializer,AuthorSerializer
# Create your views here.
from rest_framework import status
class AllBookView(APIView):

    def get(self,request,*args,**kwargs):
        all_book = BookModel.objects.all()
        serializer = BookSerializer(all_book,many=True)
        return Response(serializer.data)

class DetailBookView(APIView):
    def get(self,request,*args,**kwargs):
        book = get_object_or_404(BookModel,pk=kwargs['book_id'])
        serializer = BookSerializer(book)
        return Response(serializer.data)

class CreateBookView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'massage':'error'})

class UpdateBookView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(BookModel,pk=kwargs['book_id'])
        serializer = BookSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage':'success'},status=status.HTTP_200_OK)
        return Response({'massage':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class DeleteBookView(APIView):
    def delete(self,request,*args,**kwargs):
        instance = get_object_or_404(BookModel,pk=kwargs['book_id'])
        instance.delete()
        return Response({'massage':'success'},status=status.HTTP_204_NO_CONTENT)
class AllAuthorView(APIView):

    def get(self,request,*args,**kwargs):
        all_Author = AuthorModel.objects.all()
        serializer = AuthorSerializer(all_Author,many=True)
        return Response(serializer.data)

class DetailAuthorView(APIView):
    def get(self,request,*args,**kwargs):
        Author = get_object_or_404(AuthorModel,pk=kwargs['Author_id'])
        serializer = AuthorSerializer(Author)
        return Response(serializer.data)

class CreateAuthorView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class UpdateAuthorView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(AuthorModel,pk=kwargs['Author_id'])
        serializer = AuthorSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class DeleteAuthorView(APIView):
    def delete(self,request,*args,**kwargs):
        instance = get_object_or_404(AuthorModel,pk=kwargs['Author_id'])
        instance.delete()
        return Response({'massage':'success'},status=status.HTTP_204_NO_CONTENT)


