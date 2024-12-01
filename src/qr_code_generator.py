import qrcode
from PIL import Image
import loguru


class QRCodeGenerator:
    def generate_qr_code(
        self,
        input_str: str = "https://xn--grne-mhnesee-9ib3f.de/",
        image: str = "assets/Sonnenblume_RGB_gelb.png",
        format: str = "RGBA",
        output: str = "data/qr_code.png",
        fill_color: str = "#005437",
        back_color: str = "#f2faf6",
    ) -> bool:
        if input_str is None:
            return False
        else:
            try:
                icon = Image.open(image)
                icon.thumbnail((icon.size[0] // 16, icon.size[1] // 16))

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4,
                )

                qr.add_data(input_str)
                qr.make(fit=True)

                img_qr = qr.make_image(fill_color=fill_color, back_color=back_color)

                pos = (
                    (img_qr.size[0] - icon.size[0]) // 2,
                    (img_qr.size[1] - icon.size[1]) // 2,
                )

                img_qr = img_qr.convert(format)

                temp_image = Image.new(format, img_qr.size)
                temp_image.paste(img_qr, (0, 0))
                temp_image.paste(icon, pos, icon)
                temp_image.save(output)
                return True
            except Exception as e:
                loguru.logger.error(f"Error generating QR code: {e}")
                return False
