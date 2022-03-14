### What is this?

- Simple Python image processing & automatization project for a simple web based game
- Made using only Github Copilot (except the color and screen values)

# The Game

![](https://img.shields.io/github/stars/SGeri/colored-balls) ![](https://img.shields.io/github/issues/SGeri/colored-balls) ![](https://img.shields.io/github/forks/SGeri/colored-balls) ![](https://img.shields.io/github/license/SGeri/colored-balls)

<img src="https://img.gamedistribution.com/ec1a0c26ad8444e9b2752e47aed5b9d7-512x512.jpeg" alt="Colored Balls" width="250" height="250">

**You can try out the game on [the official website](https://simple.game/play/kick-colored-balls/)!**

### Github Copilot

Yesterday I got access to the technical review of the Copilot. My plan was to make a simple application (including 3rd party libraries etc.) and still only using the Copilot.

In short: I think it is way faster and more efficient than googling everything. The prediction of the comments and code works great, but there are is basic problem with the current system: it is a little bit too agressive.
It was a fun experience using this new technology, but do not worry. It wont replace programmers - at least not yet.

### Used 3rd party libraries

- [OpenCV2](https://pypi.org/project/opencv-python/), [Numpy](https://numpy.org) - Image processing
- [PyAutoGUI](https://pypi.org/project/opencv-python/) - Take screenshots and interacting with the game

### Try it out for yourself!

**Prerequisites**: Python 3.x with the 3rd party libraries

1. Download the repo.
2. Adjust the global variables in the colored_balls.py
   2.1 It is designed for 1920x1080 resolution
3. Run the script with the following command: **python colored-balls.py**
4. Enjoy!
