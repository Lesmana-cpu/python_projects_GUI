import pygame as pg


# init
pg.init()
isRun = True
# membuat display
window_L = 700
window_P = 500
window = pg.display.set_mode((window_L,window_P))

# object game
# posisi
x = 355   # <-- makin  kecil angkanya makin kekiri
y = 280   # <-- makin kecil angkanya makin ke atas

# ukuran
panjang = 20
lebar = 20

# movement speed
speed = 10


while isRun:
    pg.time.delay(10)
    
# user input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("DON'T CLOSEEEE")
            isRun = False

    # ambil semua key press
    keys = pg.key.get_pressed()
    
    # ambil kekiri
    if keys[pg.K_LEFT] and x > 0:
        x -= speed
        
    if keys[pg.K_RIGHT] and x < window_L-lebar:
        x += speed

    if keys[pg.K_DOWN] and y < window_P-panjang:
        y += speed

    if keys[pg.K_UP] and y > 0:
        y -= speed
        
    #update asset
    window.fill((255,255,255))
    pg.draw.rect(window,(255,0,0),(x,y,panjang,lebar))
    # render to display
    pg.display.update()
pg.quit()