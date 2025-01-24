import pytest
from device_selector.device_selector import select_best_device, check_or_select_device

def test_select_best_device():
    device = select_best_device()
    assert device in ["cuda", "mps", "cpu"]

def test_check_or_select_device():
    # If user requests "cpu", we always get "cpu"
    device = check_or_select_device("cpu")
    assert device == "cpu"
