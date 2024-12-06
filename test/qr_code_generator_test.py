import pytest
from qr_code_generator import QRCodeGenerator


def test_generate_qr_code():
    qr_code_generator = QRCodeGenerator()
    assert qr_code_generator.generate_qr_code("Hello World")


def test_generate_qr_code_with_none():
    qr_code_generator = QRCodeGenerator()
    assert not qr_code_generator.generate_qr_code(None)
