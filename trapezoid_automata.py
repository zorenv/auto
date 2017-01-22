# coding=utf-8

from vehicle import Vehicle
from tollbooth import Tollbooth

class _TA:
	def __init__(self,n_tollbooth):
		# 所有的车 
		self.vehicles = []				
		# 所有的收费站 
		self.tollbooths=[Tollbooth(r=r,id=i,n=n_tollbooth) for i in xrange(n_tollbooth)]


	def main(self):
		self.generate_vehicles()
		self.check_for_accidents()
		self.forward_or_brake()

	def generate_vehicles(self):
		"""产生车辆"""
		for tollbooth in self.tollbooths:
			self._generate_vehicle_for_a_tollbooth(tollbooth)

	def check_for_accidents(slef):
		"""检查所有的车祸"""
		# 确定check order
		self.vehicles.sort(key=lambda v:-v.pos.y)
		for v in self.vehicles:
			self._check_for_accident_for_a_vehicle(v)

	def forward_or_brake(self):
		# 所有车辆前进或者刹车
		for v in self.vehicles:
			self._forward_or_brake_for_a_vehicle(v)

	def _generate_vehicle_for_a_tollbooth(self,tollbooth):
		pass

	def _check_for_accident_for_a_vehicle(self,v):
		pass

	def _forward_or_brake_for_a_vehicle(self,v):
		pass



class TA(_TA):
	def __init__(self,time_interval,n_tollbooth,n_lane,length):
		_TA.__init__(self,n_tollbooth)
		self.time_interval=time_interval # 时间间隔
		self.max_id = 0					 # 为车辆分配的最大id
		self.through_vehicle_num = 0 # 通过的车辆的数目 
		self.accident_count = 0		 # 事故数目
		self.length =length 		 # fan-in区域的纵向长度
		self.lanes = [Lane(id=i,n=n_lane,length=self.length,...) for i in xrange(n_lane)]

	def _generate_vehicle_for_a_tollbooth(self,tollbooth):
		"""每个收费站，产生车辆"""
		if tollbooth.generate_vehicle(): ################################################
			_pos=tollbooth.pos 	  # 收费站的位置
			_init_v = tollbooth.v # 行驶出收费站的初始速度
			_id = self.get_id()   # 车辆的id
			# 产生新的车辆
			new_vehicle = Vehicle(id=_id,pos=pos,v=_init_v,destinations=self.lanes)
			self.vehicles.append(new_vehicle)


	def _check_for_accident_for_a_vehicle(self,v):
		""" 检查 车v 是否会发生车祸 """
		# 得到 r_check
		v.get_radius_check()    ################################################
		v.get_future_pos() 		################################################
		for other_v in self.vehicles:
			# 判断 other_v 是否在 check_zone中;判断 other_v 是否被检查（other_v是否在 v之前）;
			# 判断 other_v 是不是就是v
			if v.inside_check_zone(other_v) and other_v.checked and v.id!=other_v.id:################################################
				# _flag: v 是否将撞上 other_v
				# _brake_distance: 刹车距离: v与 other 之间的距离 !?
				_flag,_brake_distance=v.check_overlap(other_v) ################################################
				if _flag:
					v.brake_flag =True
					if v.brake_distance == -1:
						v.brake_distance=_brake_distance
						v.update_future_pos()			################################################
					else:
						v.brake_distance = min(v.brake_distance,_brake_distance)
						v.update_future_pos()			################################################
				v.checked=True

	def _forward_or_brake_for_a_vehicle(self,v):
		# 车辆v 继续前进或者刹车
		if v.brake_flag:
			accident_flag=v.brake() ################################################
			if accident_flag:
				self.accident_count+=1
			v.brake_flag = False
		else:
			# 车辆继续前进，并判断是否驶出fan-in区域
			exit_flag=v.forward() ################################################
			if exit_flag:
				self.through_vehicle_num+=1
				del v

	def get_result(self,time):
		throughput   = 1.0*self.through_vehicle_num/time,
		accident_rate= 1.0*self.accident_count/self.through_vehicle_num
		return throughput,accident_rate

	def _get_id(self):
		# 为新的车分配id
		self.max_id+=1
		return self.max_id

def get_cost(B,L,length):
	pass

def envalue(B,L,length,n,time_interval):
	ta=TA(  time_interval=time_interval,
			n_tollbooth=B,
			n_lane=L,
			length=length)

	for i in xrange(n):
		ta.main()

	throughput,accident_rate=ta.get_result(n*time_interval)
	cost_area = get_cost(B,L,length)
	return throughput,accident_rate,cost_area

if __name__=="__main__":
	print envalue(4,2,90,3600,1)