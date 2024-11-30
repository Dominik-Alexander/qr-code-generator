from qr_code_generator import QRCodeGenerator


def main():
    qr_code_generator = QRCodeGenerator("Hello World")
    qr_code_generator.generate_qr_code("Hello World")


if __name__ == "__main__":
    main()
