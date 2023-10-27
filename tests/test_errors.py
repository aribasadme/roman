import pytest


@pytest.mark.parametrize(
    "exc",
    [
        "OutOfRangeError",
        "NotIntegerError",
        "InvalidRomanNumeralError"
    ],
)
def test_exception_importable(exc):
    import errors as errors

    err = getattr(errors, exc)
    assert err is not None

    # check that we can raise on them
    msg = "^$"
    with pytest.raises(err, match=msg):
        raise err()
