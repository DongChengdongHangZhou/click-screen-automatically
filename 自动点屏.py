import pyautogui as pg
import time
# while(1):
#     x, y = pg.position()
#     print(x,y)


for i in range(1000):
    print(i)
    pg.click(716,652)
    pg.click(1100,955)
    pg.click(980,760)
    time.sleep(1)
    pg.mouseDown(881,158)
    time.sleep(1)
    im = pg.screenshot('./screen_shot_arch/my_screenshot'+str(i)+'.png',region=(655,0,840,1015))
    time.sleep(1)
    pg.mouseUp()
    pg.click(1000,952)