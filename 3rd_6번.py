# 사용자로부터 두 점을 입력받아서 터틀 그래픽을 이용하여 두 점을 연결하는 직선을 그린다. 직선의 끝점에 직선의 길이를 계산하여 출력해보자.
import turtle  # turtle 라이브러리 불러오기
t = turtle.Turtle()  # 변수 t에 turtle.Turtle() 선언
t.shape("turtle")  # turtle 모양 불러오기

x1 = int(input("x1: "))  # 사용자에게 변수 x1의 값을 받아옴
y1 = int(input("y1: "))  # 사용자에게 변수 y1의 값을 받아옴
x2 = int(input("x2: "))  # 사용자에게 변수 x2의 값을 받아옴
y2 = int(input("y2: "))  # 사용자에게 변수 y2의 값을 받아옴

dist = ((x1-x2)**2+(y1-y2)**2)**0.5  # 식을 통해 dist 변수의 값을 구함

t.goto(x1, y1)  # (x1,y2) 점으로 이동
t.goto(x2, y2)  # (x2,y2) 점으로 이동

t. write("점의 길이="+str(dist))  # 거북이 옆에 점의 길이(텍스트)가 나오도록 함
t._screen.exitonclick()  # 마우스로 클릭을 해야 화면이 종료됨
