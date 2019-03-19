from django.urls import path
from . import views

urlpatterns=[
	path('',views.post_list,name='post_list'),
	path('post/<int:num>/',views.post_detail,name='post_detail'),
	path('post/new/',views.post_new,name='post_new'),
	path('post/<int:num>/edit/',views.post_edit,name='post_edit'),
	path('post/drafts/',views.post_draft_list,name='post_draft_list'),
	path('post/<int:num>/publish/',views.post_publish,name='post_publish'),
	path('post/<int:num>/remove/',views.post_remove,name='post_remove'),
	path('post/<int:num>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
	path('comment/<int:num>/approve/',views.comment_approve,name='comment_approve'),
	path('comment/<int:num>/remove/',views.comment_remove,name='comment_remove'),
]