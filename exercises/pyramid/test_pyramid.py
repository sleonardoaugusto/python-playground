from textwrap import dedent

from exercises.pyramid.pyramid import build_pyramid


def test_build_pyramid_height_1():
    assert build_pyramid(1) == '0'


def test_build_pyramid_height_2():
    assert build_pyramid(2) == dedent(
        '''\
        0
        00'''
    )


def test_build_pyramid_height_4():
    assert build_pyramid(4) == dedent(
        '''\
        0
        00
        000
        0000'''
    )
