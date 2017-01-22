# coding=utf-8

V0 = 0
Vmax = 10
deltaT = 1


class vehicle: # 汽车类
    def __init__(self):
        self.id = ''        #
        self.R = 0          #半径
        self.l = 0          #长度
        self.w = 0          #宽度
        self.a_plus = 0         #加速
        self.a_normalbrake = 0  #正常刹车
        self.a_brake = 0        #碰撞刹车
        self.Vcurrent = V0      #当前速度
        self.Sbrake = 0         #刹车距离
        self.Treaction = 1
        self.x = 0
        self.y = 0


def State_Transition(vehicle):
    if Exist_Accident(vehicle):
        Brake(vehicle)
    else:
        Forward(vehicle)

def Exist_Accident(vehicle):
    pass

def Brake(vehicle):
    pass

def Forward(vehicle):
    if vehicle.Vcurrent < Vmax:  # 小于Vmax,以a+加速
        vehicle.Vcurrent += vehicle.a_plus * deltaT
    if vehicle.Vcurrent > Vmax:  # 最大加速到Vmax
        vehicle.Vcurrent = Vmax

def Caculate_a_brake(vehicle):
    if vehicle.Sbrake > vehicle.Vcurrent * vehicle.Treaction:
        vehicle.Vcurrent