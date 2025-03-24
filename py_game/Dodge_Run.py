import pygame as pg
import random

# Inisialisasi Pygame
pg.init()

# Membuat window game
window_L = 700  # Lebar window
window_P = 500  # Tinggi window
window = pg.display.set_mode((window_L, window_P))
pg.display.set_caption("Game Pygame")

# Font untuk skor
font = pg.font.SysFont("Arial", 30)

# Warna yang digunakan dalam game
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Fungsi untuk menampilkan teks di tengah layar
def tampilkan_teks(teks, ukuran_font, warna, posisi):
    font_obj = pg.font.SysFont("Arial", ukuran_font)
    teks_render = font_obj.render(teks, True, warna)
    teks_rect = teks_render.get_rect(center=posisi)
    window.blit(teks_render, teks_rect)

# Fungsi untuk menampilkan layar game over dengan tombol klik
def game_over_screen(skor):
    button_rect = pg.Rect(window_L//2 - 75, window_P//2 + 50, 150, 50)
    while True:
        window.fill(WHITE)
        tampilkan_teks(f"Game Over!", 50, RED, (window_L // 2, window_P // 3))
        tampilkan_teks(f"Skor Akhir: {skor}", 40, BLACK, (window_L // 2, window_P // 2))
        
        # Tombol untuk mengulangi permainan
        pg.draw.rect(window, BLUE, button_rect)
        tampilkan_teks("ULANGI", 30, WHITE, button_rect.center)

        pg.display.update()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

def main():
    isRun = True
    x, y = 100, 250  # Posisi awal pemain
    panjang, lebar = 15, 15  # Ukuran pemain (kotak merah)
    speed = 5  # Kecepatan gerak pemain

    rintangan_speed = 3  # Kecepatan awal rintangan
    rintangan_w, rintangan_h = 40, 40  # Ukuran rintangan (kotak biru)
    rintangan = []  # List untuk menyimpan rintangan
    persentase_rintangan = 2  # Persentase kemunculan rintangan

    skor = 0  # Skor awal
    waktu_mulai = pg.time.get_ticks()  # Waktu mulai permainan
    waktu_terakhir_tambah_persen = waktu_mulai  # Waktu terakhir peningkatan kesulitan
    
    jejak = []  # Efek jejak pemain
    max_jejak = 20  # Jumlah maksimum jejak

    # Fungsi untuk membuat rintangan baru
    def buat_rintangan():
        rintangan.append([window_L, random.randint(0, window_P - rintangan_h)])

    buat_rintangan()

    while isRun:
        pg.time.delay(10)
        waktu_sekarang = pg.time.get_ticks()
        
        # Menambah skor setiap detik dan meningkatkan kecepatan rintangan
        if waktu_sekarang - waktu_mulai >= 1000:
            skor += 1
            waktu_mulai = waktu_sekarang
            rintangan_speed = min(10, 3 + skor // 10)
        
        # Meningkatkan persentase kemunculan rintangan setiap 7 detik
        if waktu_sekarang - waktu_terakhir_tambah_persen >= 7000:
            persentase_rintangan = min(50, persentase_rintangan + 0.5)
            waktu_terakhir_tambah_persen = waktu_sekarang

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False

        # Kontrol pergerakan pemain
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and x > 0:
            x -= speed
        if keys[pg.K_RIGHT] and x < window_L - lebar:
            x += speed
        if keys[pg.K_DOWN] and y < window_P - panjang:
            y += speed
        if keys[pg.K_UP] and y > 0:
            y -= speed

        # Pergerakan rintangan
        for r in rintangan:
            r[0] -= rintangan_speed

        # Menghapus rintangan yang keluar dari layar
        rintangan = [r for r in rintangan if r[0] > -rintangan_w]

        # Menambahkan rintangan baru berdasarkan persentase
        if random.randint(1, 100) <= persentase_rintangan:
            buat_rintangan()

        # Deteksi tabrakan dengan rintangan
        for r in rintangan:
            if (x < r[0] + rintangan_w and x + panjang > r[0]) and (y < r[1] + rintangan_h and y + lebar > r[1]):
                return skor
        
        # Menyimpan jejak pemain untuk efek bayangan
        jejak.append((x, y))
        if len(jejak) > max_jejak:
            jejak.pop(0)

        window.fill(WHITE)
        
        # Menampilkan efek jejak pemain
        for i, (jx, jy) in enumerate(jejak):
            alpha = int(255 * ((i + 1) / max_jejak))
            size_factor = 1 + (i / max_jejak)
            shadow = pg.Surface((int(panjang * size_factor), int(lebar * size_factor)), pg.SRCALPHA)
            shadow.fill((255, 0, 0, alpha))
            window.blit(shadow, (jx - (panjang * (size_factor - 1) / 2), jy - (lebar * (size_factor - 1) / 2)))
        
        # Menampilkan pemain (kotak merah)
        pg.draw.rect(window, RED, (x, y, panjang, lebar))
        
        # Menampilkan rintangan (kotak biru)
        for r in rintangan:
            pg.draw.rect(window, BLUE, (r[0], r[1], rintangan_w, rintangan_h))

        # Menampilkan skor di layar
        teks_skor = font.render(f"Skor: {skor}", True, BLACK)
        window.blit(teks_skor, (10, window_P - 40))

        pg.display.update()

# Loop utama untuk menjalankan game
while True:
    hasil_skor = main()
    if hasil_skor is False:
        break
    game_over_screen(hasil_skor)
