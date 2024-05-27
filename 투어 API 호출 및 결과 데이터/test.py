from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import *


def home(request):
    keyword = request.GET.get('q') # q=검색어
    place_names = []

    if keyword: #에버랜드
        try:
            keyword_objs = Keywords.objects.filter(test_name=keyword)
            if keyword_objs.exists():
                # 검색어가 포함된 여러 개의 키워드가 반환될 수 있으므로 첫 번째 키워드를 선택
                keyword_obj = keyword_objs.first() #17
                place_keywords = PlacesKeywords.objects.filter(test=keyword_obj) # 8 9 15
                place_names = [pk.place.place_name for pk in place_keywords]
            else:
                return HttpResponse('키워드에 대한 여행지가 없습니다. <a href="/">돌아가기</a>')
        except Keywords.DoesNotExist:
            return HttpResponse('키워드에 대한 여행지가 없습니다. <a href="/">돌아가기</a>')

    context = {
        'keyword': keyword,
        'place_names': place_names,
    }

    return render(request, 'home.html', context)