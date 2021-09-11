from django.urls import path

from . import views

app_name = 'pybo'   #네임스페이스 지정 , 앱이 여러개일때 같은 url 별칭쓰면 에러나기 때문에 네임스페이스 사용

urlpatterns = [
    path('', views.index, name='index'),  #views에서 index 함수  #name='index' URL별칭 지정
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create')
]
