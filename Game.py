import pygame#引用模块

pygame.init()#初始化
window = pygame.display.set_mode((820,820))#设置窗口
pygame.display.flip()#刷新
pygame.display.set_caption("Game")#修改标题
ttc = pygame.font.SysFont('microsoftyaheiui',80)#设置字体

fps = pygame.time.Clock()#设置帧数
move = [0,0]#设置移速
装逼 = False
die = False
win_x = window.get_size()[0]
win_y = window.get_size()[1]
home = [int(win_x/2-10),int(win_y/2-10)]
snake = [home]
Debug = False
FPS = 8

def 随机数(min,mix):
    import random
    return random.randint(min, mix)

def set_apple():return (随机数(0,win_x/20-8)*20,随机数(0,win_y/20-8)*20)

def 绘制矩形(颜色,x,y,w,h,l=0):pygame.draw.rect(window,颜色,(x,y,w,h),l)

def snake_head(xy):绘制矩形("black",xy[0],xy[1],20,20)

def snake_body(xy):
    绘制矩形("black",xy[0]+1,xy[1]+1,18,18,1)
    if 装逼 :绘制矩形((随机数(0,255),随机数(0,255),随机数(0,255)),xy[0]+2,xy[1]+2,16,16)

def red_apple(xy):绘制矩形("red",xy[0]+1,xy[1]+1,18,18)

apple = set_apple()

while True :

    fps.tick(FPS)
    window.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:move = [0,-20]
            if event.key == pygame.K_s:move = [0,20]
            if event.key == pygame.K_a:move = [-20,0]
            if event.key == pygame.K_d:move = [20,0]
            if event.key == pygame.K_END:move = [0,0]
            if event.key == pygame.K_HOME:snake[0]=home
            if event.key == pygame.K_b:装逼 = True
            if event.key == pygame.K_x:装逼 = False
            if event.key == pygame.K_PAGEUP:snake.append((-20,-20))
            if event.key == pygame.K_PAGEDOWN and len(snake) > 1:snake.pop()
            if event.key == pygame.K_DELETE:die = True
            if event.key == pygame.K_TAB:die = False
            if event.key == pygame.K_UP:FPS += 1
            if event.key == pygame.K_DOWN and FPS > 1 :FPS -= 1
            if event.key == pygame.K_F3 :Debug = True

    i = len(snake) - 1

    red_apple(apple)


    while i > 0:
        snake[i] = snake[i-1]
        i-=1

    snake[0]=snake[0][0]+move[0],snake[0][1]+move[1]

    i=0

    if snake[0] == apple :
        apple = set_apple()
        snake.append([-20,-20])

    while i < len(snake):
        snake_body(snake[i])
        i+=1

    snake_head(snake[0])

    window.blit(ttc.render(str(len(snake)-1),True,"black","white"),(0,0))

    if snake[0][0] < 0 or snake[0][1] < 0 or snake[0][0] > win_x or snake[0][1] > win_y and not Debug:die = True

    if die:
        window.fill("white")
        die_text = ttc.render("你死了",True,"black","white")
        die_x,die_y = die_text.get_size()
        window.blit(die_text,(win_x/2-die_x/2,win_y/2-die_y/2))
        snake = [home]
        move = [0,0]

    pygame.display.update()