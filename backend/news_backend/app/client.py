from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials

ak = "HPUAUQQWQPYVJIIJ9KHM"
sk = "t5iARoQZk12RBDN5eofHrABp222k38llDaRGqfa8"
project_id = "6351a47e656d44b594d9ed3c0e47b2af"
REGION = Region("cn-north-4","https://iotda.cn-north-4.myhuaweicloud.com")
credentials = BasicCredentials(ak, sk, project_id)
client = IoTDAClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(REGION) \
    .with_http_config(HttpConfig(ignore_ssl_verification=True)) \
    .build()
