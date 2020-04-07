from django.test import TestCase
import unittest
# Create your tests here
class Animal(object):
    def run(self):
        print('i can run')

    @classmethod
    def a(cls):
        print('sss')
#类方法可以通过类访问
Animal.a()
dog=Animal()
dog.a()
class Test(unittest):
    def test_1(self):
        print('ceshi')