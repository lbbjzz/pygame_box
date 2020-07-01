import turtle

# 创建窗口
window = turtle.Screen()
window.setup(550, 650, 200, 0)
window.bgcolor('#C0C0C0')
window.title('Python期末项目--推箱子小游戏')
window.register_shape('wall.gif')
window.register_shape('o.gif')
window.register_shape('p.gif')
window.register_shape('box.gif')
window.register_shape('boxdone.gif')
# 立即执行 无需等待作图
window.tracer(0)


# 游戏主体
# C表示关卡的外部
# X表示表示墙壁
# O箱子正确的放置位置
# B表示箱子目前所在的位置
# P表示玩家所在的位置
# 游戏关卡类
def level_list():
    # 第一关
    level_1 = [
        'CCXXXCCC',
        'CCXOXCCC',
        'CCX XXXX',
        'XXXB BOX',
        'XO BPXXX',
        'XXXXBXCC',
        'CCCXOXCC',
        'CCCXXXCC']
    # 第二关
    level_2 = [
        'CXXXXCCC',
        'CX OXXXX',
        'XXO    X',
        'XOO XX X',
        'X B  B X',
        'XX BBXXX',
        'CXP  XCC',
        'CXXXXXCC'
    ]
    # 第三关
    level_3 = [
        'CCXXXXXXCC',
        'CCX    XXX',
        'CCX B    X',
        'XXX B XX X',
        'XOOO B   X',
        'XOOOBXB XX',
        'XXXX X B X',
        'CCCX  P  X',
        'CCCXXXXXXX'
    ]
    # 第四关
    level_4 = [
        'CCCXXXXXX',
        'XXXXO  PX',
        'X  BBB  X',
        'XOXXOXXOX',
        'X   B   X',
        'X  BOX XX',
        'XXXX   XC',
        'CCCXXXXXC'
    ]
    # 第五关
    level_5 = [
        'CXXXXXXXC',
        'XX     XX',
        'X  BOB  X',
        'X BXOXB X',
        'XXOOPOO X',
        'X BXOXB X',
        'X  BOB  X',
        'X   X  XX',
        'XXXXXXXXC'
    ]
    levels = []
    levels.append(level_1)
    levels.append(level_2)
    levels.append(level_3)
    levels.append(level_4)
    levels.append(level_5)
    return (levels)


levels = level_list()


# 提示信息
class Info(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor('red')
        self.ht()

    def message(self):
        self.goto(0, 290)
        self.write(f'第{num}关', align='center', font=('仿宋', 25, 'bold'))
        self.goto(0, 270)
        self.write('重新开始本关请按回车键', align='center', font=('仿宋', 15, 'bold'))
        self.goto(0, 250)
        self.write('选择关卡请按Tab', align='center', font=('仿宋', 15, 'bold'))

    def show_win(self):
        global num
        if num == len(levels):
            num = 1
            self.goto(0, -250)
            self.write('你已全部过关', align='center', font=('黑体', 30, 'bold'))
            self.goto(0, -300)
            self.write('返回第一关请按空格键', align='center', font=('黑体', 30, 'bold'))
        else:
            num = num + 1
            self.goto(0, -250)
            self.write('恭喜过关', align='center', font=('黑体', 30, 'bold'))
            self.goto(0, -300)
            self.write('进入下一关请按空格键', align='center', font=('黑体', 30, 'bold'))


# # 用海龟作图画出墙壁
# wall =turtle.Turtle()
# # 图片素材
# wall.shape('wall.gif')
# # 去除轨迹
# wall.penup()
#
# # 用海龟作图画出需要推的箱子
# correctBox =turtle.Turtle()
# # 图片素材
# correctBox.shape('o.gif')
# # 去除轨迹
# correctBox.penup()
#
# # 用海龟作图画出人物
# player =turtle.Turtle()
# # 图片素材
# player.shape('p.gif')
# # 去除轨迹
# player.penup()

# 海龟作图类
class Pen(turtle.Turtle):
    def __init__(self, pic):
        super().__init__()
        self.shape(pic)
        self.penup()

        # 箱子移动区域 px,py表示增加的区域

    def move(self, x, y, px, py):
        gox, goy = x + px, y + py
        if (gox, goy) in go_sapce:
            self.goto(gox, goy)
        if (gox + px, goy + py) in go_sapce and (gox, goy) in box_space:
            for i in box_list:
                if i.pos() == (gox, goy):
                    go_sapce.append(i.pos())
                    box_space.remove(i.pos())
                    i.goto(gox + px, goy + py)
                    self.goto(gox, goy)
                    go_sapce.remove(i.pos())
                    box_space.append(i.pos())
                    if i.pos() in corrent_box_space:
                        # 成功推入正确位置
                        i.shape('boxdone.gif')
                    else:
                        # 从正确位置推出
                        i.shape('box.gif')
                    if set(box_space) == set(corrent_box_space):
                        # 通关
                        text.show_win()

    # 箱子向上移动，横坐标不变 纵坐标+50
    def go_up(self):
        self.move(self.xcor(), self.ycor(), 0, 50)

        # 箱子向下移动，横坐标不变 纵坐标-50

    def go_down(self):
        self.move(self.xcor(), self.ycor(), 0, -50)

        # 箱子向左移动，纵坐标不变 横坐标-50

    def go_left(self):
        self.move(self.xcor(), self.ycor(), -50, 0)

        # 箱子向右移动，纵坐标不变 横坐标+50

    def go_right(self):
        self.move(self.xcor(), self.ycor(), 50, 0)


# 游戏界面由8*8个方格组成 每个方格像素为50
# 故第一个方格中心坐标为为（25，25）
# 以此类推 用x表示x轴坐标 y表示y轴的坐标
# 游戏类
class Game():
    def paint(self):
        i_date = len(levels[num - 1])
        j_date = len(levels[num - 1][0])
        for i in range(i_date):
            for j in range(j_date):
                x = -j_date * 25 + 25 + j * 50
                y = i_date * 25 - 25 - i * 50

                # 空白区域
                if levels[num - 1][i][j] == ' ':
                    go_sapce.append((x, y))
                # 坐标为字母为X则画出墙壁
                if levels[num - 1][i][j] == 'X':
                    wall.goto(x, y)
                    # 将墙固定
                    wall.stamp()
                if levels[num - 1][i][j] == 'O':
                    correctBox.goto(x, y)
                    go_sapce.append((x, y))
                    # 将墙固定
                    correctBox.stamp()
                    corrent_box_space.append((x, y))
                    # 人物不能固定
                if levels[num - 1][i][j] == 'P':
                    player.goto(x, y)
                    go_sapce.append((x, y))
                    # 需要推的箱子需要同样个数的海龟作图
                if levels[num - 1][i][j] == 'B':
                    # 调用
                    box = Pen('box.gif')
                    box.goto(x, y)
                    box_list.append(box)
                    box_space.append((x, y))


# 清除上一关卡的turtle内容并重新绘制
def init():
    text.clear()
    wall.clear()
    correctBox.clear()
    for i in box_list:
        i.ht()
        del (i)
    box_list.clear()
    box_space.clear()
    go_sapce.clear()
    corrent_box_space.clear()
    game.paint()
    text.message()


# 切换关卡
def choose():
    global num
    a = window.numinput('选择关卡', '你的选择（请输入1-5）', 1)
    if a is None:
        a = num
    num = int(a)
    init()
    window.listen()


# 关卡
num = 1
# 正确位置的箱子列表
corrent_box_space = []
# 箱子的位置
box_list = []
box_space = []
# 数组表示箱子可以移动的区域
go_sapce = []
# 调用海龟作图类
wall = Pen('wall.gif')
correctBox = Pen('o.gif')
player = Pen('p.gif')
# 游戏类
game = Game()
game.paint()
# 提示信息
text = Info()
text.message()

# 屏幕监听
window.listen()
# 键盘监听
window.onkey(player.go_up, 'Up')
window.onkey(player.go_down, 'Down')
window.onkey(player.go_left, 'Left')
window.onkey(player.go_right, 'Right')
window.onkey(init, 'Return')
window.onkey(init, 'space')
window.onkey(choose, 'Tab')

# 持续更新屏幕
while True:
    window.update()
# 显示窗口
window.mainloop()
