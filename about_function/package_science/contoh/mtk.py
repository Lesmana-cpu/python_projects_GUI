def bagi(pembilang, *penyebut):
    for data in penyebut:
        pembilang /= data
    hasil = int(pembilang)
    return hasil