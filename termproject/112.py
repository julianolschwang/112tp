from cmu_graphics import *
import random

def onAppStart(app):
    app.stepCount = 0
    app.stepsPerSecond = 30
    app.score = 0
    app.width = 800
    app.height = 600
    app.ground = 100
    app.obstacleWidth = 40
    app.player = Player(app)
    app.obstacles = []

def drawLabels(app):
    drawLabel('Geometry Dash: Julian Edition', app.width//2, 40, font = 'arial', size = 40, bold = True, fill = 'lightGray')
    drawLabel('Press space to jump!', app.width//2, 100, size = 30, fill = 'lightGray')
    drawLabel(f'Score: {app.score}', 70, app.height - 40, size = 20, fill = 'lightGray', bold = True)

def drawGround(app):
    drawRect(0, 0, app.width, app.height, fill = 'blue')
    drawRect(0, app.height - app.ground, app.width, app.ground, fill = 'black')

def drawObstacles(app):
    if app.stepCount % 50 == 0:
        app.obstacles.append(Obstacle(app))
    for elem in app.obstacles:
        elem.draw()
        
def updateObstacles(app):
    for elem in app.obstacles:
        elem.update()

class Player:
    def __init__(self, app):
        self.r = 40
        self.cx = app.width // 4
        self.cy = app.height - app.ground - self.r
        self.velocity = 0
        self.acceleration = -5
        
    def update(self, app):
        self.velocity += self.acceleration
        self.cy -= self.velocity
        if self.cy >= app.height - app.ground - self.r:
            self.cy = app.height - app.ground - self.r
            self.velocity = 0

    def draw(self):
        drawCircle(self.cx, self.cy, self.r, fill = 'lightGreen')
        drawLabel(':)', self.cx + 7, self.cy + 2, rotateAngle = 90, size = 80)
        
class Obstacle:
    def __init__(self, app):
        self.startTime = app.stepCount
        self.width = 40
        self.height = random.random() * 100
        self.topX = app.width
        self.topY = app.height - app.ground - self.height
    
    def draw(self):
        drawRect(self.topX, self.topY, self.width, self.height, fill = 'red')
        
    def update(self):
        self.topX -= 10
    
def redrawAll(app):
    drawGround(app)
    drawLabels(app)
    app.player.draw()
    drawObstacles(app)
        
def onStep(app):
    app.stepCount += 1
    app.score = app.stepCount // 5
    app.player.update(app)
    updateObstacles(app)

def onKeyPress(app, key):
    if key == 'space' and app.player.cy == app.height - app.ground - app.player.r:
        app.player.velocity = 50

def main():
    runApp()

main()