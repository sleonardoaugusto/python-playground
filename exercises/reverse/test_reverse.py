from exercises.reverse.reverse import reverse_alpha


def test_reverse_alpha():
    assert reverse_alpha('a.b*d') == 'd.b*a'
    assert reverse_alpha('.ab') == '.ba'
    assert reverse_alpha('a...') == 'a...'
    assert reverse_alpha('a...b') == 'b...a'
    assert (
        reverse_alpha('a*b,c@d#eaffeqw)2a*a#31&$*@abe')
        == 'e*b,a@a#awqeffa)2e*d#31&$*@cba'
    )
