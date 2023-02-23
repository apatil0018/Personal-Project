from django.urls import path
from .views import index, enquiryView, personalDetailView, showEnquiryView, showPersonalDetailView, Pre_Loan_DetaildView, occupation, boccupation,confirm,guaranteer,Document_uploadView, addressView, twostepView, lconfirm, bankdetailfView,register,login_view,logoutView, home, rmanager, omanager, submission,approveView,deleteView1
urlpatterns = [
    path('', index, name='indexurl'),
    path('ev/',enquiryView, name='enquiryurl'),
    path('pdv/',personalDetailView, name='personaldetailurl'),
    path('se/',showEnquiryView, name='showenquiryurl'),
    path('spd/',showPersonalDetailView,name='showpersonaldetailurl'),
    path('pld/',Pre_Loan_DetaildView, name='preloanurl'),
    path('ov/', occupation, name='occupationurl'),
    path('bov/', boccupation, name='boccupationurl'),
    path('cv/',confirm, name='confirmurl'),
    path('gv/',guaranteer, name='guaranteerurl'),
    path('duv/', Document_uploadView, name='documenturl'),
    path('av/',addressView, name='addressurl'),
    path('verify/',twostepView, name='verifyurl'),
    path('lcv/',lconfirm, name='lconfirmurl'),
    path('bv/',bankdetailfView, name='bankurl'),
    path('lv/',login_view,name='loginurl'),
    path('rv/',register, name='registerurl'),
    path('hv/', home, name='homeurl'),
    path('rm/', rmanager, name='rmanagerurl'),
    path('om/', omanager, name='omanagerurl'),
    path('lov/', logoutView, name='logout'),
    path('sm/',submission, name='sm'),
    path("approve/<str:mail>/",approveView, name="approve"),
    path("delete/<str:mail>/", deleteView1, name="delete1"),

]
