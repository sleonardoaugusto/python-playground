from textwrap import dedent

from pyramid.pyramid import pyramid


def test_pyramid_height_1():
    assert pyramid(1) == '0'


def test_pyramid_height_2():
    assert pyramid(2) == dedent(
        '''\
        0
        00'''
    )


def test_pyramid_height_4():
    assert pyramid(4) == dedent(
        '''\
        0
        00
        000
        0000'''
    )
