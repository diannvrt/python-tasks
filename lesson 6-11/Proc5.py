#Функция rect_ps(x1, y1, x2, y2) возвращает периметр и площадь прямоугольника со сторонами, 
#параллельными осям, по противоположным вершинам. Найти P и S трёх прямоугольников
def rect_ps(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    P = 2 * (width + height)
    S = width * height
    return(P, S)

for i in range(3):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    P, S = rect_ps(x1, y1, x2, y2)
    print(P)
    print(S)