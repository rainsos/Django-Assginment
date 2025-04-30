# urls.py

from django.contrib import admin
from django.urls import path
from django.http import Http404
from django.shortcuts import render
from fake_db import user_db

# 내부 DB 연결
_db = user_db

# 유저 리스트 뷰
def user_list(request):
    names = [{'id': key, 'name': value['이름']} for key, value in _db.items()]
    return render(request, 'user_list.html', {'data': names})

# 유저 상세정보 뷰
def user_info(request, user_id):
    if user_id not in _db:   # 정확한 유저 유무 체크
        raise Http404('User not found')
    info = _db[user_id]
    return render(request, 'user_info.html', {'data': info})

# URL 매핑
urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/', user_info, name='user_info'),
    path('admin/', admin.site.urls),
]
