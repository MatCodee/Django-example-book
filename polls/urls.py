from django.urls import path
from .views import polls_list, polls_detail

#from .apiviews import PollDetail,PollList,ChoiceList,CreateVote

'''
urlpatterns = [
    path("polls/", polls_list, name="polls_list"),

    # misma vista sin DRF
    path("polls/<int:pk>/", polls_detail, name="polls_detail"),
    
    # con DRF
    path("api/polls/",PollList.as_view(),name="polls_list_class"),
    path("api/polls/<int:pk>",PollDetail.as_view(),name='polls_details_class'),
    
    path("api/choices/", ChoiceList.as_view(), name="choice_list"),
    path("api/vote/", CreateVote.as_view(), name="create_vote"),
]
'''
from .apiviews import ChoiceList,CreateVote,UserCreate,LoginView,PollViewSet
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

# podemos hacer que nuestras vistas sean mas intuitivas 
urlpatterns = [
    path("api/polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("api/polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("api/users/", UserCreate.as_view(), name="user_create"),
    
    #path("api/login/", LoginView.as_view(), name="login"), # definida en base a la funcion que retorna tl token
    path("api/login/", views.obtain_auth_token, name="login"),
]
urlpatterns += router.urls