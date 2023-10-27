from roman import RomanNumeral


def test_to_roman():
    expected = 'MMMCMXCVIII'
    rn = RomanNumeral(3998)

    assert rn.to_roman() == expected


def test_to_arabic():
    expected = 3998
    rn = RomanNumeral('MMMCMXCVIII')

    assert rn.to_arabic() == expected
