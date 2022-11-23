from datetime import *
import time

dogum_tarihi = datetime.strptime(input("Doğum tarihin (Gün.Ay.Yıl) şeklinde yazılmalıdır : "), "%d.%m.%Y")

while True:
    yasanilansaniye = datetime.now() - dogum_tarihi
    print("Şu kadar saniye yaşadın: {} ".format(round(yasanilansaniye.total_seconds(), 0)))

    time.sleep(5)