#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import urllib3
import facebook
import requests


def main():

    # app_id = '491508931423378'
    # app_secret = 'a8742d4708468e9f683db65f1de8b686'
    # user_short_token = 'EAAGZCBldC7JIBAA2az4UbWi71ByKyXzdIVYRYc2IRLXfzsVuvMeZA2o6fJz2IilZAMr8OFVwitOb0Tdt8pYnd6CyS71FhagNv9GUZAwK6GxADHkdG0QxQjaX0nU4eS1pcCXeF21XqCXslKA7E8oBNg4YZBd1ZAKsKiXaZAnTZA8NkgZDZD'
    # access_token_url =  "https://graph.facebook.com/oauth/access_token?client_id={}&client_secret={}&grant_type=client_credentials".format(app_id, app_secret)

    # r = requests.get(access_token_url)

    # access_token_info = r.json()
    # access_token = access_token_info['access_token']

    # url_get_page = " https://graph.facebook.com/v3.3/wualuanluan/posts?access_token={}".format(access_token)

    # r_page = requests.get(url_get_page)
    # page_info =r_page.json()
    # print(page_info)




    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfolio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    


if __name__ == '__main__':
    main()
