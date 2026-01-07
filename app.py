from __future__ import print_function

from pprint import pprint
import time
import urllib3

import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException

urllib3.disable_warnings()

# configure cluster connection: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.host = 'https://<NODE_IP>:8080'
configuration.username = 'root'
configuration.password = 'a'
configuration.verify_ssl = False

# create an instance of the API class
api_client = isilon_sdk.v9_12_0.ApiClient(configuration)
api_instance = isilon_sdk.v9_12_0.ProtocolsApi(api_client)

# get all exports
sort = 'description'
limit = 50
order = 'ASC'
try:
    api_response = api_instance.list_nfs_exports(sort=sort, limit=limit, dir=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)
