# Game URL: https://simple.game/play/kick-colored-balls/

#import cv2, pyautogui, np
import cv2, pyautogui, numpy as np

# Globals
CAPTURE_REGION = (790, 335, 360, 530)

ORANGE_LOWER = [15, 0, 0]
ORANGE_UPPER = [25, 255, 255]
DRAW_ORANGE_COLOR = (0, 0, 255)

BLUE_LOWER = [85, 0, 0]
BLUE_UPPER = [145, 255, 255]
DRAW_BLUE_COLOR = (0, 255, 0)

ORANGE_CLICK_POS = [850, 830]
BLUE_CLICK_POS = [1050, 830]

BALLS_X = 182.5
CLICK_ZONE_Y = 480

while True:
    #take a screenshot with a box around the colored balls
    screenshot = pyautogui.screenshot(region=CAPTURE_REGION)

    #convert the screenshot to real colors
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    #declare balls list
    balls = []

    #find the balls with the orange color
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
    lower_ball = np.array(ORANGE_LOWER)
    upper_ball = np.array(ORANGE_UPPER) 
    mask = cv2.inRange(hsv, lower_ball, upper_ball)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #apply the contours to the screenshot
    cv2.drawContours(screenshot, contours, -1, DRAW_ORANGE_COLOR, 3)

    #append the location of the balls to balls list
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        #only append the ball when the width is 39 and the x coordinate is BALLS_X
        if w == 39 and x + w / 2 == BALLS_X:
            balls.append((x + w / 2, y + h / 2, "orange"))

    #find the balls with the blue color
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
    lower_ball = np.array(BLUE_LOWER)
    upper_ball = np.array(BLUE_UPPER)
    mask = cv2.inRange(hsv, lower_ball, upper_ball)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #apply the contours to the screenshot
    cv2.drawContours(screenshot, contours, -1, DRAW_BLUE_COLOR, 3)

    #append the location of the balls to balls list
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        #only append the ball when the width is 39 and the x coordinate is BALLS_X
        if w == 39 and x + w / 2 == BALLS_X:
            balls.append((x + w / 2, y + h / 2, "blue"))

    #sort the balls by their y coordinate
    balls.sort(key=lambda x: x[1])

    #if the length of the balls list is less than 15 and is more than two
    if len(balls) < 15 and len(balls) > 2:
        #store the last ball
        last_ball = balls[-1]

        #if the last ball's y coordinate is greater than CLICK_ZONE_Y
        if last_ball[1] > CLICK_ZONE_Y:
            #if the ball is orange
            if last_ball[2] == "orange":
                #click at ORANGE_CLICK_POS
                pyautogui.click(ORANGE_CLICK_POS[0], ORANGE_CLICK_POS[1]) 
            else:
                #click at BLUE_CLICK_POS
                pyautogui.click(BLUE_CLICK_POS[0], BLUE_CLICK_POS[1])

    #continuosly show the screenshot as Game Window
    cv2.imshow('Game Window', screenshot)

    #if the user presses the 'q' key destroy the window
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break