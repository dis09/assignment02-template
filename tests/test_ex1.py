from exercises import ex1
import pytest
from pytest import approx


@pytest.mark.points(5)
def test_n_zdf():
    assert ex1.n_zdf == 117


@pytest.mark.points(5)
def test_n_rt():
    assert ex1.n_rt == 55


@pytest.mark.points(5)
def test_mean_likes_zdf():
    assert ex1.mean_likes_zdf == approx(510.4615, abs=1e-2)


@pytest.mark.points(5)
def test_mean_likes_rt():
    assert ex1.mean_likes_rt == approx(508.3455, abs=1e-2)


@pytest.mark.points(15)
def test_test_likes():
    assert (ex1.test_likes == approx((-0.0205, 0.9837), abs=1e-2) or ex1.test_likes == approx((0.0205, 0.9837), abs=1e-2))


@pytest.mark.points(5)
def test_test_views():
    assert (ex1.test_views == approx((-3.5215, 0.0006), abs=1e-2) or ex1.test_views == approx((3.5215, 0.0006), abs=1e-2))


@pytest.mark.points(5)
def test_test_comments():
    assert (ex1.test_comments == approx((2.5031, 0.0133), abs=1e-2) or ex1.test_comments == approx((-2.5031, 0.0133), abs=1e-2))
