# test_app.py
from app import check_system_status

def test_system_healthy():
    # เราคาดหวังว่า ถ้า CPU 45% มันต้องตอบว่า "HEALTHY"
    assert check_system_status(45) == "HEALTHY"

def test_system_danger():
    # เราคาดหวังว่า ถ้า CPU 95% มันต้องตอบว่า "DANGER"
    assert check_system_status(95) == "DANGER"