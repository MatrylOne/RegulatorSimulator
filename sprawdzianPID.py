import helpers.animationHelper as ah
import helpers.modelHelper as mh
import helpers.issAnimation as anim
import helpers.issPlot as mpt
import pygame

# GŁÓWNE METODY
def model(T, h, y0, u0, d):
    # Inicjacja tablic

    a = -0.5
    histereza = 0.05

    times = mh.createArray(0, T, h)

    ys = [y0]
    es = [d - y0]
    us = [u0]

    isRising = es[0] < 0

    # Symulacja wypełniająca tablice
    for i in range(0, len(times) - 1):
        ys.append(ys[i] + h * (a * ys[i] + us[i]))
        es.append(d - ys[i])

        # Jeśli ma rosnąć
        if isRising:
            # Włącz
            # Jeśli rośnie, próg zadziałania ma być powyżej zadanej wartości
            if es[i] + histereza > 0:
                us.append(1)
                isRising = True
            # Wyłącz
            # Jeśli rośnie próg wyłaczenia ma być poniżej zadanej wartości
            elif es[i] - histereza <= 0:
                us.append(0)
                isRising = False
            # Nie podejmuj akcji
            # Jeśli nie przekraczasz wartości progowych, przyjmij ostatnią wartość
            else:
                us.append(us[i])

        # Jeśli ma maleć
        else:
            # Włącz
            # Jeśli maleje, próg zadziałania ma być poniżej zadanej wartości
            if es[i] - histereza > 0:
                us.append(1)
                isRising = True
            # Wyłącz
            # Jeśli maleje próg wyłaczenia ma być powyżej zadanej wartości
            elif es[i] + histereza <= 0:
                us.append(0)
                isRising = False
            else:
                us.append(us[i])

    return (times, ys, es, us)

def generateModels(T, h, xRange, yRange, iterations):
    # Inicjacja tablicy wyników
    datas = []
    # Losowanie
    for i in range(0, iterations):
        datas.append(model(T, h, mh.randomRange(xRange), mh.randomRange(yRange)))
    return datas

# WYWOŁYWANIE METOD
print("generating data")
data = [model(20, 0.01, 0, 0, 0.5)]
plot = mpt.IssPlot(data)
plot.pointPlot(1)
plot.pointSub(1)
plot.statePlot([0, 1], False, False)
plot.pointSub(2)
plot.statePlot([0, 2], False, False)
plot.pointSub(3)
plot.statePlot([0, 3], False, False)
plot.show()