# -*- coding: utf-8 -*-

import unittest
from unittest.mock import Mock, patch, MagicMock
import requests

from qiita import Qiita


class QiitaTest(unittest.TestCase):

    def setUp(self):
        self.access_token = 'test_token'
        self.qiita = Qiita(self.access_token)

    def tearDown(self):
        pass

    def test_my_self_items_url(self):
        self.assertEquals('https://qiita.com/api/v2/authenticated_user/items?page=1&per_page=1', self.qiita.myself_items_url(1, 1))

    def test_comments_url(self):
        self.assertEqual('https://qiita.com/api/v2/items/random/comments', self.qiita.comments_url('random'))

    def test_post_item_url(self):
        self.assertEqual('https://qiita.com/api/v2/items', self.qiita.post_item_url())

    def test_access_token(self):
        self.assertEqual('Bearer ' + self.access_token, self.qiita.access_token())

    def test_authorization_header(self):
        self.assertEqual({
            'Authorization': 'Bearer ' + self.access_token
        }, self.qiita.authorization_header())

    def test_json_request_header(self):
        self.assertEqual({
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }, self.qiita.json_request_header())

    def test_url_encode(self):
        self.assertEqual('query=qiita+user%3Ayaotti', self.qiita._urlencode('qiita user:yaotti'))

    def test_url_encode_empty_str(self):
        self.assertEqual('query=', self.qiita._urlencode(''))

    def test_get_items(self):
        class ReturnValue(object):
            def __init__(self):
                self.text = """
                    [{"render_body": "test1"}, {"render_body": "test2"}]
                """
                self.status_code = 200

        requests.get = MagicMock(return_value=ReturnValue())
        self.assertEqual([{"render_body": "test1"}, {"render_body": "test2"}], self.qiita.get_items(1, 3))

    def test_get_comment(self):
        class ReturnValue(object):
            def __init__(self):
                self.text = """
                    [{"render_body": "test1"}, {"render_body": "test2"}]
                """
                self.status_code = 200

        requests.get = MagicMock(return_value=ReturnValue())
        self.assertEqual([{"render_body": "test1"}, {"render_body": "test2"}], self.qiita.get_comment('comment_id'))



