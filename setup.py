# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='qiita_api_wrapper',
    version='0.1.0',
    description='Qiita API V2 wrapper for Python',
    long_decsciption='Qiita API V2 wrapper for Python. detail link https://qiita.com/api/v2/docs#%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%88',
    url='https://github.com/nittyan/QiitaAPI',
    author='nittyan',
    author_email='kaziotore@gmail.com',
    keywords=['qiita qpi web'],
    license='MIT',
    py_modules=['qiita', 'builders'],
    install_requires=['requests'],
    classifiles=[
        'Development Status :: 4 - Beta',
        'Licence :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4'
    ]
)
