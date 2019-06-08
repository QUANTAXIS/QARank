import codecs
import io
import os
import re
import sys
import webbrowser
import platform

try:
    from setuptools import setup
except:
    from distutils.core import setup


NAME = "quantaxis_rank"
"""
名字，一般放你包的名字即可
"""
PACKAGES = ["QARank"]
"""
包含的包，可以多个，这是一个列表
"""

DESCRIPTION = "QUANTAXIS RANK: Rank for Accounts/Traders"
KEYWORDS = ["quantaxis", "quant", "finance", "Backtest", 'Framework']
AUTHOR_EMAIL = "yutiansut@qq.com"
AUTHOR = 'yutiansut'
URL = "https://github.com/yutiansut/quantaxis_unicorn"


LICENSE = "MIT"

setup(
    name=NAME,
    version='1.0',
    description=DESCRIPTION,
    long_description='rank for trader/accounts',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    install_requires=['pika', 'quantaxis>=1.1.10.dev2'],
    entry_points={
        'console_scripts': [
        ]
    },
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True
)