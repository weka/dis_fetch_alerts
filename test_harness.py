from pprint import pprint

import wekarestapi
from wekarestapi.rest import ApiException


def main():
    config = wekarestapi.Configuration(hostname="vweka01")

    # create an instance of the API class
    api_client = wekarestapi.ApiClient(config)

    try:
        # login to weka system
        api_response = wekarestapi.LoginApi(api_client).login(
            wekarestapi.LoginBody(username="admin", password="Weka.io123", org="root"))
        #    pprint(api_response)
        config.auth_tokens = api_response.data
    except ApiException as e:
        print("Exception when calling LoginApi->login: %s\n" % e)

    try:
        # get alerts
        api_response = wekarestapi.AlertsApi(api_client).get_alerts()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertsApi->get_alerts: %s\n" % e)

if __name__ == '__main__':
    main()

