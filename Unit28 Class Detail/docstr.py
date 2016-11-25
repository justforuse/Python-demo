# coding=utf-8
# 函数的第一个逻辑行的字符串是那个函数的文档字符串

"I am: docstr.__doc__"


def func(args):
    "I am: docstr.func.__doc__"
    pass


class spam:

    "I am spam.__doc__ or docstr.spam.__doc___"

    def method(self, arg):
        "I am spam.method.__doc__ or self.method.__doc__"
        pass
