from django.urls import path, include
from rest_framework import routers
from rest_accounts.api.views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"mpesa/b2c", MpesaB2Cviewset, "mpesa_b2c")
router.register(r"mpesa/c2b", MpesaC2Bviewset, "mpesa_c2b")
router.register(r"mpesa/account_balance", MpesaAccountBalanceviewset, "mpesa_account_balance")
router.register(r"mpesa/transaction_status", TransactionStatusviewset, "mpesa_transaction_status")
router.register(r"mpesa/reversal", MpesaReversalsviewset, "mpesa_reversal")



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include("rest_accounts.api.urls")),
]
