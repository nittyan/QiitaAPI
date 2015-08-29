# -*- coding: utf-8 -*-

import json
import requests


class Qiita(object):

    error_codes = [400, 401, 403, 404, 500]
    url = 'https://qiita.com/api/v2'

    def __init__(self, access_token):
        self._access_token = access_token

    def access_token(self):
        return 'Bearer {}'.format(self._access_token)

    def items_url(self, page, per_page):
        """
            post item list take url

            Args
                page: int
                per_page: int

            Returns:
                url: str
        """
        return (Qiita.url + '/items?page={}&per_page={}').format(page, per_page)

    def comments_url(self, comment_id):
        """
            post item related comment take url

            Args
                comment_id: int

            Returns:
              url: str
        """
        return (Qiita.url + '/items/{}/comments').format(comment_id)

    def post_item_url(self):
        return Qiita.url + '/items'

    def authorization_header(self):
        return {
          'Authorization': self.access_token()
        }

    def json_request_header(self):
        header = self.authorization_header()
        header['Content-Type'] = 'application/json'
        return header

    def get_items(self, page, per_page):
        """
            Returns:
                items: list[dict]
        """
        response = requests.get(self.items_url(page, per_page), headers=self.authorization_header())
        parsed_json = json.loads(response.text)
        return [item for item in parsed_json]

    def get_comment(self, comment_id):
        """
            Args:
                comment_id: str
            Returns:
                comments: list[dict]
        """
        response = requests.get(self.comments_url(comment_id), headers=self.authorization_header())
        parsed_json = json.loads(response.text)
        return [comment for comment in parsed_json]

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

    def post_item(self, data):
        response = requests.post(self.post_item_url(), headers=self.json_request_header(), data=data)
        if response.status_code in Qiita.error_codes:
            raise Exception(response.text)

