import pyautogui
import pyautogui as pp


#pyautogui.dragTo(300,300)

weight,height = pyautogui.size()
print(weight,height)

#获取鼠标的当前位置
mouseX,mouseY = pp.position()
print(mouseX,mouseY)

X,Y = pp.position()
pp.rightClick(X-100,Y+100)

