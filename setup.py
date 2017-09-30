# coding: utf-8
from setuptools import setup, find_packages
from MarkcvChain import __author__, __version__, __license__
 
setup(
        name             = 'MarcvChain',
        version          = __version__,
        description      = 'Yahooの形態素解析とマルコフ連鎖を使用して、文章の自動生成をするライブラリ',
        license          = __license__,
        author           = __author__,
        author_email     = '',
        url              = 'https://github.com/nozomi0966/MarkcvChain',
        keywords         = 'MarkcvChain',
        packages         = find_packages(),
        install_requires = [],
        )
