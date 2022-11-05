# 1번 문제에서 계산한 거리가 맞는지, 터틀 그래픽으로 확인해보자. 거북이를 왼쪽으로 45도회전하여 141만큼 전진시킨다. 다시 거북이를 (0,0)으로 이동하고 0도를 가리키게 한 후에 100만큼 전진하고 왼쪽으로 90도 회전하여 100만큼 전진한다. 화면에 그려진 직선이 일치하는가?
import turtle  # turtle 라이브러리를 불러온다.
t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언한다.
t.shape("turtle")  # turtle 모양을 불러온다.

t.left(45)  # 왼쪽으로 45도 회전
t.forward(141)  # 141만큼 전진
t.goto(0, 0)  # (0,0)으로 이동
t.setheading(0)  # 0도를 가리키게 함
t.forward(100)  # 100만큼 전진
t.left(90)  # 왼쪽으로 90도 회전
t.forward(100)  # 100만큼 전진

t._screen.exitonclick()  # 마우스로 클릭해야 화면이 종료됨
