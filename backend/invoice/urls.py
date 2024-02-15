from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="LoginView"),
    path("invoices/",InvoiceView.as_view(),name="All-invoice"),
    path("invoices/new/",InvoiceView.as_view(),name="Post-invoice"),
    path("invoices/<int:id>/",SpecificInvoice.as_view(),name="Post-invoice"),
    path("invoices/<int:id>/items/",AddItem.as_view(),name="Post-invoice"),
]
