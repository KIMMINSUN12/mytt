from django.urls import path, include
from .views import InfoDetail, InfoList
#InfoDetail.as_view()
urlpatterns = [
    path('info/', InfoDetail.as_view(), name='detail'),
    #url(r'<int:pk>/', views.MovieDetail.as_view()) # 정규표현식 에러
    path('info2/', InfoList.as_view(), name='infos')
]
#<![CDATA[]>></script><p></p>
#<p style="line-height: 2;"><span style="font-size: 12pt;">다음으로 장고 프로젝트 URL에 movie 앱 url을 추가합니다.</span></p>
#<script type="syntaxhighlighter" class="brush: python">


#from .views import HelloAPI

#urlpatterns = [
    #path("hello/", HelloAPI),
#]