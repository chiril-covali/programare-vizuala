import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPen, QColor, QBrush
import math

class FunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Function Plotter')
        self.setGeometry(100, 100, 800, 600)

        # Create graphics scene and view
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        # Set up coordinate system parameters
        self.scale = 50  # pixels per unit
        self.x_min, self.x_max = -10, 10
        self.y_min, self.y_max = -5, 5

        # Draw coordinate system and plot function
        self.drawCoordinateSystem()
        self.plotFunction()

    def drawCoordinateSystem(self):
        # Draw axes
        pen = QPen(Qt.black, 2)
        
        # X axis
        self.scene.addLine(-400, 0, 400, 0, pen)
        # Y axis
        self.scene.addLine(0, -300, 0, 300, pen)

        # Draw grid and labels
        grid_pen = QPen(QColor(200, 200, 200), 1)
        text_pen = QPen(Qt.black)

        # Vertical grid lines and X labels
        for x in range(int(self.x_min), int(self.x_max) + 1):
            if x != 0:  # Skip zero as it's the axis
                self.scene.addLine(x * self.scale, -300, x * self.scale, 300, grid_pen)
                self.scene.addText(str(x)).setPos(x * self.scale - 10, 10)

        # Horizontal grid lines and Y labels
        for y in range(int(self.y_min), int(self.y_max) + 1):
            if y != 0:  # Skip zero as it's the axis
                self.scene.addLine(-400, y * self.scale, 400, y * self.scale, grid_pen)
                self.scene.addText(str(-y)).setPos(10, y * self.scale - 10)

    def plotFunction(self):
        pen = QPen(QColor(255, 0, 0), 2)
        step = 0.1
        points = []

        # Calculate function points
        x = self.x_min
        while x <= self.x_max:
            try:
                # Calculate y = 2*sin(x)*exp(x/5)
                y = 2 * math.sin(x) * math.exp(x/5)
                if self.y_min <= y <= self.y_max:
                    points.append(QPointF(x * self.scale, -y * self.scale))
            except (ValueError, OverflowError):
                pass
            x += step

        # Draw function curve
        if len(points) > 1:
            for i in range(len(points) - 1):
                self.scene.addLine(points[i].x(), points[i].y(),
                                 points[i+1].x(), points[i+1].y(), pen)

def main():
    app = QApplication(sys.argv)
    plotter = FunctionPlotter()
    plotter.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()