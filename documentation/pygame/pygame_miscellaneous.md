[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Miscellaneous

## Version issues

Related Stack Overflow questions:

- [ImportError: No module named 'pygame'](https://stackoverflow.com/questions/18317521/importerror-no-module-named-pygame/64494572#64494572)

The current [PyGame](https://www.pygame.org/news) release, 1.9.6 doesn't support Python 3.9. I fyou don't want to wait for PyGame 2.0, you have to use Python 3.8. Alternatively, you can install a developer version by explicitly specifying the version (_2.0.0.dev20_ is the latest release at the time of writing):

```
pip install pygame==2.0.0.dev20
```

or try to install a pre-release version by enabling the `--pre` option:

```
pip install pygame --pre
```

### Windows

Related Stack Overflow questions:

- [Unable to install pygame on Python 3.8 via pip (Windows 10)](https://stackoverflow.com/questions/58489348/unable-to-install-pygame-on-python-3-8-via-pip-windows-10)
- [How to troubleshoot python import error - DLL access denied](https://stackoverflow.com/questions/49127425/how-to-troubleshoot-python-import-error-dll-access-denied)
- [When I try to install pygame using python 3.9 I get an error windows](https://stackoverflow.com/questions/64261106/when-i-try-to-install-pygame-using-python-3-9-i-get-an-error-windows)

### Mac

Related Stack Overflow questions:

- [Problems getting pygame to show anything but a blank screen on Macos Mojave](https://stackoverflow.com/questions/52718921/problems-getting-pygame-to-show-anything-but-a-blank-screen-on-macos-mojave)
- [pygame installation issue in mac os](https://stackoverflow.com/questions/22974339/pygame-installation-issue-in-mac-os)
- [Pygame 1.9.6 not loading in Python 3.8.1](https://stackoverflow.com/questions/59691131/pygame-1-9-6-not-loading-in-python-3-8-1)
- [Pygame not showing anything in the window](https://stackoverflow.com/questions/53182886/pygame-not-showing-anything-in-the-window)
- [Error when installing PyGame on Mac (Catalina) [duplicate]](https://stackoverflow.com/questions/60132717/error-when-installing-pygame-on-mac-catalina)

### Ubuntu

- [Pygame already installed; however, python terminal says “No module named 'pygame' ” (Ubuntu 20.04.1)](https://stackoverflow.com/questions/64016215/pygame-already-installed-however-python-terminal-says-no-module-named-pygame/64016373#64016373)

## File access

Related Stack Overflow questions:

- **[pygame.image.load('sprite/test_bg.jpg'): pygame.error: Couldn't open sprite/test_bg.jpg](https://stackoverflow.com/questions/58177145/pygame-image-loadsprite-test-bg-jpg-pygame-error-couldnt-open-sprite-test)**
- [Error - pygame.error: Couldn't open backround.png. Fix?](https://stackoverflow.com/questions/57836528/error-pygame-error-couldnt-open-backround-png-fix/57836574#57836574)
- [I've got an error when trying to create sound using pygame](https://stackoverflow.com/questions/55784793/ive-got-an-error-when-trying-to-create-sound-using-pygame/55784882#55784882)

The image file path has to be relative to the current working directory. The working directory is possibly different to the directory of the python file.

The name and path of the file can be get by [`__file__`](https://docs.python.org/3/reference/import.html#import-related-module-attributes). The current working directory can be get by [`os.getcwd()`](https://docs.python.org/3/library/os.html) and can be changed by [`os.chdir(path)`](https://docs.python.org/3/library/os.html).

One solution is to change the working directory:

```py
import os

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)
```

An alternative solution is to find the absolute path.
If the image is relative to the folder of the python file (or even in the same folder), then you can get the directory of the file and join ([`os.path.join()`](https://docs.python.org/3/library/os.path.html)) the image filename. e.g.:

```py
import pygame
import os

# get the directory of this file
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# [...]

# join the filepath and the filename
imgPath = os.path.join(sourceFileDir, 'test_bg.jpg')
# imgPath = os.path.join(sourceFileDir, '_pycache_/test_bg.jpg')

surface = pygame.image.load(imgPath)
```

## Math

- [How to draw a rectangle around two points](https://stackoverflow.com/questions/62008684/how-to-draw-a-rectangle-around-two-points/62008841#62008841)
- [I am wondering why it says the distance has to be less than 27? Why less than 27? Where is 27 coming from?](https://stackoverflow.com/questions/62523256/i-am-wondering-why-it-says-the-distance-has-to-be-less-than-27-why-less-than-27/62527566#62527566)  
- [Why is the math of my stacking game not working?](https://stackoverflow.com/questions/64598428/why-is-the-math-of-my-stacking-game-not-working/64598693#64598693)  

## Delete, remove Object

Tag: delete object, remove object, erase object, delete image, remove image, erase image

Related Stack Overflow questions:

- [how to make image/images disappear in pygame?](https://stackoverflow.com/questions/61480115/how-to-make-image-images-disappear-in-pygame/61480380#61480380)
- [How to delete one object from a Surface instance (pygame)?](https://stackoverflow.com/questions/62859831/how-to-delete-one-object-from-a-surface-instance-pygame/62860003)
- [How do I delete rect object from screen once player collides with it?](https://stackoverflow.com/questions/62957899/how-do-i-delete-rect-object-from-screen-once-player-collides-with-it/62958077#62958077)

## Progress bar

Related Stack Overflow questions:

- [How can I display a smooth loading bar in pygame?](https://stackoverflow.com/questions/54502683/how-can-i-display-a-smooth-loading-bar-in-pygame/54502953#54502953)  
  ![rprogress ba](https://i.stack.imgur.com/zRnGM.gif)
- [How to show shields level by changing color of the progress bar](https://stackoverflow.com/questions/57033885/how-to-show-shields-level-by-changing-color-of-the-progress-bar/57033917#57033917)  
  ![progress ba](https://i.stack.imgur.com/XHYP0.gif)

## Motion

Related Stack Overflow questions:

- [How to fix character constantly accelerating in both directions after deceleration Pygame?](https://stackoverflow.com/questions/59832445/how-to-fix-character-constantly-accelerating-in-both-directions-after-decelerati/59846286#59846286)  
  ![scene](https://i.stack.imgur.com/8I8HV.gif)
- [Image rotation while moving](https://stackoverflow.com/questions/57226587/image-rotation-while-moving/57227063#57227063)  
  ![scene](https://i.stack.imgur.com/XWNPt.gif)
- [make multiple objects automatically move for how many objects have been specified in pygame](https://stackoverflow.com/questions/55723064/make-multiple-objects-automatically-move-for-how-many-objects-have-been-specifie/55723441#55723441)  
  ![scene](https://i.stack.imgur.com/JxNz3.gif)
- [Is it possible to use simple rotation matrices to simulate circular orbits in pygame?](https://stackoverflow.com/questions/58667567/is-it-possible-to-use-simple-rotation-matrices-to-simulate-circular-orbits-in-py/58669192#58669192)  
  ![Is it possible to use simple rotation matrices to simulate circular orbits in pygame?](https://i.stack.imgur.com/UQh3R.gif)
- [Implementing smooth motion in 2d space in Pygame](https://stackoverflow.com/questions/59104823/implementing-smooth-motion-in-2d-space-in-pygame/59107333#59107333)  
  ![Implementing smooth motion in 2d space in Pygame](https://i.stack.imgur.com/XNhzy.gif)
- [Pygame game help: Easing/Acceleration](https://stackoverflow.com/questions/59629452/pygame-game-help-easing-acceleration/59629532#59629532)  
  ![Pygame game help: Easing/Acceleration](https://i.stack.imgur.com/uWHyo.gif)
- [Pygame smooth movement](https://stackoverflow.com/questions/60461011/pygame-smooth-movement/60462904#60462904)
- [How do I make smooth movement + rotation in pygame?](https://stackoverflow.com/questions/62599851/how-do-i-make-smooth-movement-rotation-in-pygame/62600299#62600299)  
  ![How do I make smooth movement + rotation in pygame?](https://i.stack.imgur.com/adDP9.gif)
- [How to make a realistic 2D player movement (jump, fluidity…)](https://stackoverflow.com/questions/63752585/how-to-make-a-realistic-2d-player-movement-jump-fluidity/63753496#63753496)

## Gravity and jump

Related Stack Overflow questions:

- [How to simulate Jumping in Pygame for this particular code](https://stackoverflow.com/questions/54595777/how-to-simulate-jumping-in-pygame-for-this-particular-code/54596624#54596624)  
  ![scene](https://i.stack.imgur.com/XEAF8.gif)
- [Projectile motion and gravity in pygame only sometimes working](https://stackoverflow.com/questions/55822116/projectile-motion-and-gravity-in-pygame-only-sometimes-working/55836374#55836374)  
  ![scene](https://i.stack.imgur.com/MxE2C.gif)
- [python, pygame - jumping too fast?](https://stackoverflow.com/questions/58474204/python-pygame-jumping-too-fast/58474280#58474280)
- [How to make a circular object jump using pygame?](https://stackoverflow.com/questions/62822322/how-to-make-a-circular-object-jump-using-pygame/62822601#62822601)  
  ![How to make a circular object jump using pygame?](https://i.stack.imgur.com/6BPnL.gif)

## Grid

[Image loading using pygame](https://stackoverflow.com/questions/60617748/image-loading-using-pygame/60622756#60622756)

[Blitting images onto a tile that is part of a grid in pygame](https://stackoverflow.com/questions/59121989/blitting-images-onto-a-tile-that-is-part-of-a-grid-in-pygame/59124520#59124520)  
![scene](https://i.stack.imgur.com/9WgWJ.png)

[Pygame lags after drawing full window grid](https://stackoverflow.com/questions/61650325/pygame-lags-after-drawing-full-window-grid/61650969#61650969)

[Python pygame converting drawing to an image](https://stackoverflow.com/questions/61678353/python-pygame-converting-drawing-to-an-image/61678449#61678449)

[how can I edit a sudoku grid in pygame using mouse and keyboard detection?](https://stackoverflow.com/questions/62345206/how-can-i-edit-a-sudoku-grid-in-pygame-using-mouse-and-keyboard-detection/62345586#62345586)

[Colour chainging problem and non dupicates](https://stackoverflow.com/questions/63538350/colour-chainging-problem-and-non-dupicates/63538548#63538548)  
![scene](https://stackoverflow.com/questions/63538350/colour-chainging-problem-and-non-dupicates/63538548#63538548)

[Get a sprites position so that the next sprite can be placed near it](https://stackoverflow.com/questions/63871620/get-a-sprites-position-so-that-the-next-sprite-can-be-placed-near-it/63873027#63873027)

[Python: How to make drawn elements snap to grid in pygame](https://stackoverflow.com/questions/63926261/python-how-to-make-drawn-elements-snap-to-grid-in-pygame/63926759#63926759)  
![scene](https://i.stack.imgur.com/VCmuV.gif)

## Maze

[Hide and Seek/Maze game in pygame not working](https://stackoverflow.com/questions/63853997/hide-and-seek-maze-game-in-pygame-not-working/63854295#63854295)
![scene](https://i.stack.imgur.com/2QYir.gif)

[How can I make this demo drawing game update drawing the circles faster with Pygame?](https://stackoverflow.com/questions/60284620/how-can-i-make-this-demo-drawing-game-update-drawing-the-circles-faster-with-pyg/60285364#60285364)  
![scene](https://i.stack.imgur.com/mojlK.gif)

## Collection

[Pygame Basic calculator](https://stackoverflow.com/questions/63200489/pygame-basic-calculator)  
![scene](https://i.stack.imgur.com/tbIt8.gif)

[How to make a “while mouse down” loop in pygame](https://stackoverflow.com/questions/54666587/how-to-make-a-while-mouse-down-loop-in-pygame/54667247#54667247)  
![scene](https://i.stack.imgur.com/G4RML.gif)

[How to Get the X and Y Positions of All Curves in a Lissajous Curve Table?](https://stackoverflow.com/questions/55076531/how-to-get-the-x-and-y-positions-of-all-curves-in-a-lissajous-curve-table/55076619#55076619)  
![scene](https://i.stack.imgur.com/CoB4G.png)

[How would I make a heatmap in pygame on a grid](https://stackoverflow.com/questions/55617119/how-would-i-make-a-heatmap-in-pygame-on-a-grid/55618024#55618024)  
![scene](https://i.stack.imgur.com/4c4gB.gif)

[A Bowyer-Watson Delaunay Triangulation I implemented doesn't remove the triangles that contain points of the super-triangle](https://stackoverflow.com/questions/58116412/a-bowyer-watson-delaunay-triangulation-i-implemented-doesnt-remove-the-triangle/58122991#58122991)  
![scene](https://i.stack.imgur.com/Cogod.png)

[Bowyer-Watson triangulates incorrectly when trying to implement circumcircle calculation for vertices at infinity](https://stackoverflow.com/questions/58203812/bowyer-watson-triangulates-incorrectly-when-trying-to-implement-circumcircle-cal/58205019#58205019)  
![scene](https://i.stack.imgur.com/4NMrx.png) 

[How to draw with mouse and save as 1s and 0s](https://stackoverflow.com/questions/58847079/how-to-draw-with-mouse-and-save-as-1s-and-0s/58850614#58850614)  
![scene](https://i.stack.imgur.com/hMHD8.gif)

[Calculate angles that are in degrees (clockwise) to radians (counter clockwise)](https://stackoverflow.com/questions/58845411/calculate-angles-that-are-in-degrees-clockwise-to-radians-counter-clockwise/58845851#58845851)  
![scene](https://i.stack.imgur.com/JtzD1.jpg)

[Creating an arc between two points pygame](https://stackoverflow.com/questions/58954526/creating-an-arc-between-two-points-pygame/58959662#58959662)  
![scene](https://i.stack.imgur.com/494KZ.png)

[Is there anyway to do this recursively in pygame?](https://stackoverflow.com/questions/59455641/is-there-anyway-to-do-this-recursively-in-pygame/59456232#59456232)  
![scene](https://i.stack.imgur.com/fyYSY.png)

[Trying to code the Recaman Sequence, but issue with the parameters I pass for drawing an arc](https://stackoverflow.com/questions/54384422/trying-to-code-the-recaman-sequence-but-issue-with-the-parameters-i-pass-for-dr/54386695#54386695)  

[Pygame low frame rate on simple game](https://stackoverflow.com/questions/55073598/pygame-low-frame-rate-on-simple-game/55076222#55076222)  
![scene](https://i.stack.imgur.com/hseTx.gif)

[Trying to delete two objects when placed next to eachother in pygame](https://stackoverflow.com/questions/56101697/trying-to-delete-two-objects-when-placed-next-to-eachother-in-pygame/56102178#56102178)

[Gaps in a line while trying to draw them with a mouse problem](https://stackoverflow.com/questions/56379888/gaps-in-a-line-while-trying-to-draw-them-with-a-mouse-problem/56380523#56380523)
![scene](https://i.stack.imgur.com/sCdN0.gif)

[Need help creating buttons in pygame](https://stackoverflow.com/questions/57672389/need-help-creating-buttons-in-pygame/57678017#57678017)  
![scene](https://i.stack.imgur.com/BfXkE.gif)

[Python : What is the better way to make multiple loops in pygame?](https://stackoverflow.com/questions/57908287/python-what-is-the-better-way-to-make-multiple-loops-in-pygame)  

[I want to make a visualized bubble sort in pygame, the sort works but the visualization doesn't](https://stackoverflow.com/questions/58039583/i-want-to-make-a-visualized-bubble-sort-in-pygame-the-sort-works-but-the-visual/58039872#58039872)  
![scene](https://i.stack.imgur.com/h48Os.gif)

[How can I create a window where my program draws a dot ( which is point.png here ) wherever I click on the screen?](https://stackoverflow.com/questions/59002061/how-can-i-create-a-window-where-my-program-draws-a-dot-which-is-point-png-here/59002137#59002137)
![scene](https://i.stack.imgur.com/XthPF.gif)

[Python3: Count images number and compared the similarity](https://stackoverflow.com/questions/59183941/python3-count-images-number-and-compared-the-similarity/59184495#59184495)  
![scene](https://i.stack.imgur.com/WEdJR.gif)

[How to code a rectangles that start from right in circular motion in pygame](https://stackoverflow.com/questions/59180556/how-to-code-a-rectangles-that-start-from-right-in-circular-motion-in-pygame/59217711#59217711)  
![scene](https://i.stack.imgur.com/Jskrw.png)

[How do I make my monster move randomly in my game](https://stackoverflow.com/questions/59327552/how-do-i-make-my-monster-move-randomly-in-my-game/59329312#59329312)  
![scene](https://i.stack.imgur.com/J7bIM.gif)

[Pygame problem: how to execute conditional on collision?](https://stackoverflow.com/questions/59522285/pygame-problem-how-to-execute-conditional-on-collision/59522405#59522405)  
![scene](https://i.stack.imgur.com/iTIE0.gif)

[python pygame mask collision](https://stackoverflow.com/questions/59595874/python-pygame-mask-collision/59598297#59598297)  
![scene](https://i.stack.imgur.com/vSuGD.gif)

[How do i correctly update the position and velocity of 100 class objects individually drawing with pygame?](https://stackoverflow.com/questions/59868994/how-do-i-correctly-update-the-position-and-velocity-of-100-class-objects-individ/59869091#59869091)  
![scene](https://i.stack.imgur.com/dgCq1.gif)

[Colour Changing Bouncing Ball](https://stackoverflow.com/questions/60312365/colour-changing-bouncing-ball/60315375#60315375)
![scene](https://i.stack.imgur.com/Bz0cu.gif)

[Water ripple effect Python and Pygame, from coding train video](https://stackoverflow.com/questions/60336688/water-ripple-effect-python-and-pygame-from-coding-train-video/60337269#60337269)
![scene](https://i.stack.imgur.com/L0Ct5.gif)

[Is it possible to implement gradual movement of an object to given coordinates in Pygame?](https://stackoverflow.com/questions/60356812/is-it-possible-to-implement-gradual-movement-of-an-object-to-given-coordinates-i/60356995#60356995)  
![scne](https://i.stack.imgur.com/rScfu.gif)

[Using a matrix as a sprite and testing if two sprites overlap](https://stackoverflow.com/questions/60387917/using-a-matrix-as-a-sprite-and-testing-if-two-sprites-overlap/60391694#60391694)  
![scene](https://i.stack.imgur.com/brlQk.gif)

[Pygame swap text with another text](https://stackoverflow.com/questions/60944070/pygame-swap-text-with-another-text/60953697#60953697)  
![scene](https://i.stack.imgur.com/DcHQy.gif)

[Saving history of drawing in Pygame in order to implement Ctrl Z](https://stackoverflow.com/questions/61295811/saving-history-of-drawing-in-pygame-in-order-to-implement-ctrl-z/61296440#61296440)  
![scene](https://i.stack.imgur.com/snmsK.gif)

[Removing drawings without overriding previous ones on pygame -Python](https://stackoverflow.com/questions/61309564/removing-drawings-without-overriding-previous-ones-on-pygame-python/61310016#61310016)  
![scene](https://i.stack.imgur.com/xChjD.gif)

[Is it possible to update a pygame drawing attribute when a event occurs?](https://stackoverflow.com/questions/61551790/is-it-possible-to-update-a-pygame-drawing-attribute-when-a-event-occurs/61555479#61555479)
![scene](https://stackoverflow.com/questions/61551790/is-it-possible-to-update-a-pygame-drawing-attribute-when-a-event-occurs/61555479#61555479)

[How can I blit an image on the screen where i click after pressing a button](https://stackoverflow.com/questions/61556099/how-can-i-blit-an-image-on-the-screen-where-i-click-after-pressing-a-button/61556461#61556461)

[How to find the button on the entered position by user and change it's color in pygame?](https://stackoverflow.com/questions/61767256/how-to-find-the-button-on-the-entered-position-by-user-and-change-its-color-in/61767309#61767309)  
![scene](https://i.stack.imgur.com/sqIcy.gif)
![scene](https://i.stack.imgur.com/KMpLP.gif)

[Pong game in python. Score and out-of-screen check](https://stackoverflow.com/questions/62221432/pong-game-in-python-score-and-out-of-screen-check/62221774#62221774)  
![scene](https://i.stack.imgur.com/AdKUV.gif)

[I want to make insertig sorting visualizer,the sorting works but not the visualizer](https://stackoverflow.com/questions/62327655/i-want-to-make-insertig-sorting-visualizer-the-sorting-works-but-not-the-visuali/62328400#62328400)  
![scene](https://i.stack.imgur.com/DFAkW.gif)

[Why it doesn't spin in a circle? And how to fix it?](https://stackoverflow.com/questions/62883103/why-it-doesnt-spin-in-a-circle-and-how-to-fix-it/62883770#62883770)  
![scene](https://i.stack.imgur.com/UD6Wt.gif)

[pygame.mouse.get_pressed() not responding](https://stackoverflow.com/questions/63197182/pygame-mouse-get-pressed-not-responding/63197269#63197269)  
![scene](https://stackoverflow.com/questions/63197182/pygame-mouse-get-pressed-not-responding/63197269#63197269)

[Pygame Enemys Wont Move Down - Tower Defense Game](https://stackoverflow.com/questions/63734280/pygame-enemys-wont-move-down-tower-defense-game)
