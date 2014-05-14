#! /usr/env/python
# coding=utf-8
__author__ = 'gengjie'
from HTMLParser import HTMLParser
import re


class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        HTMLParser.handle_starttag(self, tag, attrs)
        if tag == 'meta':
            for (K, V) in attrs:
                print K, ':', V

    def handle_data(self, data):
        HTMLParser.handle_data(self, data)
        if re.match('.*百度.*', data):
            print data
        elif re.match('.*ICP.*', data):
            print data

    def handle_comment(self, data):
        HTMLParser.handle_comment(self, data)
        print data


htm = open('/home/gengjie/index.html')
str = htm.read()
parser = Parser()
parser.feed(str)
htm.close()