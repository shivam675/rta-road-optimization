"""Tests for the main module."""

from rta_road_optimization.main import main


def test_main():
    """Test that main function runs without error."""
    try:
        main()
        assert True
    except Exception:
        assert False, "main() should not raise an exception"
