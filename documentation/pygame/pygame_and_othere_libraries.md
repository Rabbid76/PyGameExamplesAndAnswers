[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# PyGame in combination with other libraries

## PySimpleGUI

[PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)

Related Stack Overflow questions:

- [Changing the volume when moving the slider](https://stackoverflow.com/questions/59775588/changing-the-volume-when-moving-the-slider/59775888#59775888)

  :scroll: **[Minimal example - Slider change volume](../../examples/pygame_pysimplegui/pysimplegui_minimal_slider_volume.py)**

## PygameMenu

[pygame-menu](https://pygame-menu.readthedocs.io/en/4.1.3/)

## MathPlotLib

[mathplotlib](https://matplotlib.org/)

Related Stack Overflow questions:

- [How can I integrate a Line Chart Viewer in PyGame?](https://stackoverflow.com/questions/70493951/how-can-i-integrate-a-line-chart-viewer-in-pygame/70494476#70494476)  
  ![How can I integrate a Line Chart Viewer in PyGame?](https://i.stack.imgur.com/iL9v5.png)

  :scroll: **[Minimal example - MAth plot lib](../../examples/minimal_examples/pygame_minimal_mathplotlib_1.py)**

## PyQt

Related Stack Overflow questions:

- [Closing Pygame which was run from a QThread stop responding](https://stackoverflow.com/questions/74090650/closing-pygame-which-was-run-from-a-qthread-stop-responding/74090702#74090702)  

- [Pygame not returning events while embedded in PyQt](https://stackoverflow.com/questions/59723683/pygame-not-returning-events-while-embedded-in-pyqt/70326025#70326025)

Do not mix frameworks. The frameworks may interact poorly with each other or conflict completely. If it works on your (operating) system, that doesn't mean it will work on another (operating) system or with a different version of one of the frameworks. Mixing frameworks always means some kind of undefined behavior.  

In your example your create an image ([pygae.Surface](https://www.pygame.org/docs/ref/surface.html)) with the _Pygame_ library and display it in `QWidget`.
You never create a _Pygame_ window. Therefore the _Pygame_ event handling cannot work. You need to use Qts event handling.  

Anyway, if you just want to do some image processing or draw some pictures and display them in a Qt application, I suggest using [OpenCV](https://opencv.org/) ([cv2](https://pypi.org/project/opencv-python/)). This library is designed for powerful image manipulation and the images can be viewed nicely using a Qt user interface.
