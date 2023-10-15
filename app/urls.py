from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('formview',views.form_view,name='form_view'),
    path('formsubmit',views.form_submit,name='formsubmit'),
    path('userlogin',views.user_login,name='userlogin'),
    path('userlogout',views.user_logout,name='userlogout'),
    path('pdfdownload',views.pdf_download,name='pdfdownload'),
    path('bills',views.bills,name='bills'),
    path('billview/<int:i>',views.bill_view_pdf,name='billview')
]