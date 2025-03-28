import random
class Vehicle:
    def __init__(self):
        self.speed = 0
        self.x = 0
        self.y = 0

    def accelerate(self, amount):
        """加速方法"""
        self.speed = max(0, self.speed + amount)
        print(f"加速 → 当前速度: {self.speed} km/h")

    def brake(self, amount):
        """刹车方法"""
        self.speed = max(0, self.speed - amount)
        print(f"刹车 → 当前速度: {self.speed} km/h")

    def move(self):
        """根据速度更新位置"""
        self.x += self.speed * 0.1  # 模拟简单移动
        self.y += self.speed * 0.1
        print(f"位置更新 → X: {self.x:.1f}, Y: {self.y:.1f}")

class Autopilot:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def check_traffic_light(self):
        """模拟交通灯信号（随机生成红绿灯状态）"""
        return random.choice(["RED", "GREEN"])

    def control_vehicle(self):
        """根据交通灯状态控制车辆"""
        light = self.check_traffic_light()
        if light == "RED" and self.vehicle.speed > 0:
            print("发现红灯开始刹车")
            self.vehicle.brake(10)
        elif light == "GREEN" and self.vehicle.speed < 60:
            print("发现绿灯可以加速")
            self.vehicle.accelerate(10)
        self.vehicle.move()

car = Vehicle()
autopilot = Autopilot(car)

print("=== 自动驾驶模拟开始 ===")
for _ in range(5):
    autopilot.control_vehicle()


class RoutePlanner:
    def __init__(self):
        self.waypoints = [(10, 10), (20, 20), (30, 30)]  # 预设路径点

    def next_waypoint(self):
        """获取下一个路径点（简单弹出队列）"""
        if self.waypoints:
            return self.waypoints.pop(0)
        return None

class SmartVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        self.route_planner = RoutePlanner()
        self.current_target = None

    def update_target(self):
        """更新行驶目标点"""
        self.current_target = self.route_planner.next_waypoint()
        if self.current_target:
            print(f"新目标点 → X: {self.current_target[0]}, Y: {self.current_target[1]}")

    def avoid_obstacle(self):
        """模拟避障（随机生成障碍物检测）"""
        return random.choice([True, False])  # True 表示检测到障碍物

    def autonomous_drive(self):
        """自动驾驶主逻辑"""
        if not self.current_target:
            self.update_target()

        # 模拟避障逻辑
        if self.avoid_obstacle():
            print("检测到障碍物! 紧急刹车")
            self.brake(self.speed)  # 刹停
        else:
            self.accelerate(5)
            self.move()

        # 简单判断是否到达目标点
        if self.current_target and self.x >= self.current_target[0]:
            print(f"到达目标点 {self.current_target}!")
            self.update_target()

# 测试代码
smart_car = SmartVehicle()
smart_car.update_target()

print("\n=== 智能路径规划模拟 ===")
for _ in range(8):
    smart_car.autonomous_drive()