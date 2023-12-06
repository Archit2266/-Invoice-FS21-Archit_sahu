from django.urls import path
from .views import *

urlpatterns = [
    path("user/signup", SignupView.as_view(), name="register"),
    path("user/login", LoginView.as_view(), name="login"),
    path("invoices", InvoiceView.as_view(), name="invoices"),
    path("invoices/<int:id>", SpecificInvoice.as_view(), name="SpecificInvoice"),
    path("invoices/<int:invoice_id>/items", AddItemView.as_view(), name="AddItemView"),
]
