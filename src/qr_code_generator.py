import qrcode
import loguru


class QRCodeGenerator:
    def __init__(self, string_to_convert: str):
        self._string_to_convert = string_to_convert

    def generate_qr_code(self, input: str) -> bool:
        if input is None:
            return False
        else:
            try:
                img = qrcode.make(input)

                print(type(img))
                print(img.size)

                img.save("data/qr_code.png")
                return True
            except Exception as e:
                loguru.logger.error(e)
                return False
