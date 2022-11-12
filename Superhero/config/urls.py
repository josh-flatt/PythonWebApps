from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from hero.views_hero import *
from hero.views_accounts import *
from hero.views_investigator import *
from hero.views_articles import *

urlpatterns = [
    
    #Accounts
    path('accounts/',                include('django.contrib.auth.urls')),
    path('accounts/<int:pk>',        UserUpdateView.as_view(), name='account_edit'),
    path('accounts/<int:pk>/',       UserUpdateView.as_view(), name='account_edit'),
    path('accounts/signup',          SignUpView.as_view(), name='signup'),
    path('accounts/signup/',         SignUpView.as_view(), name='signup'),
    path('accounts/login',           LoginView.as_view(), name='login'),
    path('accounts/login/',          LoginView.as_view(), name='login'),
    #path('accounts/logout',         LogoutView.as_view(), name='logout'),
    #path('accounts/logout/',        LogoutView.as_view(), name='logout'),
    path('admin/',                   admin.site.urls),

    #Investigator
    path('investigator',                   InvestigatorListView.as_view(), name='investigator_list'),
    path('investigator/',                  InvestigatorListView.as_view(), name='investigator_list'),
    path('investigator/add',               InvestigatorCreateView.as_view(), name='investigator_add'),
    path('investigator/add/',              InvestigatorCreateView.as_view(), name='investigator_add'),
    path('investigator/home',              InvestigatorHomeView.as_view(), name='investigator_home'),
    path('investigator/home/',             InvestigatorHomeView.as_view(), name='investigator_home'),
    path('investigator/<int:pk>',          InvestigatorDetailView.as_view(), name='investigator_detail'),
    path('investigator/<int:pk>/',         InvestigatorDetailView.as_view(), name='investigator_detail'),
    path('investigator/<int:pk>/edit',     InvestigatorUpdateView.as_view(), name='investigator_update'),
    path('investigator/<int:pk>/edit/',    InvestigatorUpdateView.as_view(), name='investigator_update'),
    path('investigator/<int:pk>/delete',   InvestigatorDeleteView.as_view(), name='investigator_delete'),
    path('investigator/<int:pk>/delete/',  InvestigatorDeleteView.as_view(), name='investigator_delete'),
    
    #Hero
    path('',                        RedirectView.as_view(url='hero')),
    path('hero',                    HeroListView.as_view(),    name='hero_list'),
    path('hero/',                   HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',           HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/<int:pk>/',          HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',                HeroCreateView.as_view(),  name='hero_add'),
    path('hero/add/',               HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/edit',      HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/edit/',     HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete',    HeroDeleteView.as_view(),  name='hero_delete'),
    path('hero/<int:pk>/delete/',   HeroDeleteView.as_view(),  name='hero_delete'),

    #Article
    path('article',                   ArticleListView.as_view(), name='article_list'),
    path('article/',                  ArticleListView.as_view(), name='article_list'),
    path('article/add',               ArticleCreateView.as_view(), name='article_add'),
    path('article/add/',              ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:pk>',          ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/',         ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/edit',     ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/edit/',    ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete',   ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<int:pk>/delete/',  ArticleDeleteView.as_view(), name='article_delete')
]
