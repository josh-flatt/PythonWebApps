from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from hero.views_hero import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView
from hero.views_accounts import UserUpdateView, LoginView, SignUpView, LogoutView, AuthorRegisterView
from hero.views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorUpdateView, AuthorCreateView, AuthorHomeView
from hero.views_articles import ArticleDeleteView, ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView

urlpatterns = [
    
    #Accounts
    path('accounts/',               include('django.contrib.auth.urls')),
    path('accounts/<int:pk>',       UserUpdateView.as_view(), name='account_edit'),
    path('accounts/signup/',         SignUpView.as_view(), name='signup'),
    path('accounts/login/',          LoginView.as_view(), name='login'),
    #path('accounts/logout',        LogoutView.as_view(), name='logout'),
    path('admin/',                  admin.site.urls),

    #Author
    path('author',                  AuthorListView.as_view(), name='author_list'),
    path('author/add',              AuthorCreateView.as_view(), name='author_add'),
    path('author/home',             AuthorHomeView.as_view(), name='author_home'),
    path('author/<int:pk>',         AuthorDetailView.as_view(), name='author_detail'),
    path('author/<int:pk>/edit',    AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete',  AuthorDeleteView.as_view(), name='author_delete'),
    
    #Hero
    path('',                        RedirectView.as_view(url='hero')),
    path('hero',                    HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',           HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',                HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/edit',      HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete',    HeroDeleteView.as_view(),  name='hero_delete'),

    #Article
    path('article',                  ArticleListView.as_view(), name='article_list'),
    path('article/add',              ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:pk>',         ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/edit',    ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete',  ArticleDeleteView.as_view(), name='article_delete')
]
