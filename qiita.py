# -*- coding: utf-8 -*-

import json
import requests
import urllib


class Qiita(object):

    error_codes = [400, 401, 403, 404, 500]
    url = 'https://qiita.com/api/v2'

    def __init__(self, access_token):
        self._access_token = access_token

    def access_token(self):
        return 'Bearer {}'.format(self._access_token)

    def myself_items_url(self, page, per_page):
        """
            post item list take url

            Args
                page: int
                per_page: int

            Returns:
                url: str
        """
        return (Qiita.url + '/authenticated_user/items?page={}&per_page={}').format(page, per_page)

    def _urlencode(self, query):
        """
            Args:
                query: str
        """
        return urllib.parse.urlencode({'query': query})

    def comments_url(self, comment_id):
        """
            post item related comment take url

            Args
                comment_id: int

            Returns:
              url: str
        """
        return (Qiita.url + '/items/{}/comments').format(comment_id)

    def tags_items_url(self, tag_id, page, per_page):
        return Qiita.url + '/tags/{}/items?page={}&per_page={}'.format(tag_id, page, per_page)

    def post_item_url(self):
        return Qiita.url + '/items'

    def stocks_url(self, user_id):
        return (Qiita.url + '/users/{}/stocks').format(user_id)

    def authenticated_user_url(self):
        return Qiita.url + '/authenticated_user'

    def stocks_url(self, user_id, page, per_page):
        return Qiita.url + '/users/{}/stocks?page={}&per_page={}'.format(user_id, page, per_page)

    def authorization_header(self):
        return {
          'Authorization': self.access_token()
        }

    def json_request_header(self):
        header = self.authorization_header()
        header['Content-Type'] = 'application/json'
        return header

    def get_request(self, url, header):
        response = requests.get(url, headers=header)
        self._check_error(response)
        parsed_json = json.loads(response.text)
        return [item for item in parsed_json]

    def get_items(self, page=1, per_page=1):
        """
            Args:
                page: int
                per_page: int
            Returns:
                items: list[dict]
        """
        return self.get_request(self.myself_items_url(page, per_page), self.authorization_header())

    def get_comment(self, comment_id):
        """
            Args:
                comment_id: str
            Returns:
                comments: list[dict]
        """
        return self.get_request(self.comments_url(comment_id), self.authorization_header())

    def get_comments(self, comment_ids):
        """
            Args:
                comment_id: list[str]
            Returns:
                comments: list[dict]
        """
        comments = []
        for comment_id in comment_ids:
            comments.extend(self.get_comment(comment_id))

        return comments

    def get_tags_items(self, tag_id, page=1, per_page=1):
        return self.get_request(self.tags_items_url(tag_id, page, per_page), self.json_request_header())

    def get_stocks(self, user_id):
        return self.get_request(self.stocks_url(user_id), self.authorization_header())

    def get_authenticated_user(self):
        return self.get_request(self.authenticated_user_url(), self.authorization_header())

    def get_stocks(self, user_id, page=1, per_page=1):
        return self.get_request(self.stocks_url(user_id, page, per_page), self.authorization_header())

    def post_item(self, data):
        response = requests.post(self.post_item_url(), headers=self.json_request_header(), data=data)
        self._check_error(response)

    def _check_error(self, response):
        if response.status_code in Qiita.error_codes:
            raise Exception(response.text)

