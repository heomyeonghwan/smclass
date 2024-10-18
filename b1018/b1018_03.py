class Car:
  def __init__(self,color,tire,gear,speed):
    self.color = color
    self.tire = tire
    self.gear = gear
    self._speed = speed

  def upSpeed(self,value):
    if value > 0: self._speed += value
    else:
      raise "값을 잘못 넣었습니다."

  def downSpeed(self,value):
    self._speed -= value

c1 = Car("흰색",4,"auta",0)
c1.color = "블루"
print(c1.color)
c1.speed = 300
print(c1.speed)


# #클래스 사용하려면 클래스 선언!!을해야함
# c1 = Car()
# c1.speed = 300
# print(c1.color)
# print(c1.tire)

# c2 = Car()
# c2.color = "빨강"
# print(c2.color)
# print(c1.color)
## 속도 = 0 -> 100

# #speed 변수에 직접 값을 할당
# c1.speed = 100
# print(c1.speed)

#함수를 활용해서 값을 할당
# c1.upSpeed(100)
# print(c1.speed)