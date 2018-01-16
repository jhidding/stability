from pytest import approx
from cubic import cubic_roots


def test_cubic_root():
    roots = cubic_roots(1, 0, -1, 0)

    for r in roots:
        assert r.imag == approx(0.0), "all roots should be real"

    assert sorted(roots) == approx([-1.0, 0.0, 1.0])
