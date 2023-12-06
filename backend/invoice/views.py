from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .data import *
import jwt


# Create your views here.
class SignupView(APIView):
    def post(self, request):
        data = request.data
        data["user_id"] = len(user_data) + 1
        serializers = UserSerializer(data=data)
        if serializers.is_valid():
            user_data.append(serializers.data)
            return Response({"message": "accoint created"}, status=201)
        return Response(serializers.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        for val in user_data:
            if val["email"] == data["email"] and val["password"] == data["password"]:
                token = jwt.encode(
                    {"email": val["email"], "user_id": val["user_id"]},
                    "secret",
                    algorithm="HS256",
                )
                return Response(
                    {"message": "Login successful", "token": str(token)}, status=200
                )
            return Response({"message": "credentails are not valid"}, status=401)


class InvoiceView(APIView):
    def get(self, request):
        serializer = InvoiceSerializer(invoices_data, many=True).data
        return Response(serializer)

    def post(self, request):
        data = request.data
        data["invoice_id"] = len(invoices_data) + 1
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            invoices_data.append(serializer.data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SpecificInvoice(APIView):
    def get(self, request, id):
        for val in invoices_data:
            if val["invoices_id"] == id:
                serializer = InvoiceSerializer(val).data
                return Response(serializer)
            return Response({"message": "invoice not found"}, status=404)


class AddItemView(APIView):
    def post(self, request, invoice_id):
        for val in invoices_data:
            if val["invoice_id"] == invoice_id:
                data = request.data
                serializer = itemSerializer(data=data)
                if serializer.is_valid():
                    val["items"].append(serializer.data)
                    return Response(serializer.data, status=201)
                return Response(serializer.errors, status=400)
