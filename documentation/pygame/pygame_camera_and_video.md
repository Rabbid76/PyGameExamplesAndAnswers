[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Camera and Video

## Camera

Related Stack Overflow questions:

- [python pygame.camera.init() NO vidcapture](https://stackoverflow.com/questions/16266244/python-pygame-camera-init-no-vidcapture/69053911#69053911)
- [blit opencv camera capture with pygame throws TypeError: argument 1 must be pygame.Surface, not cv2.VideoCapture](https://stackoverflow.com/questions/74077114/blit-opencv-camera-capture-with-pygame-throws-typeerror-argument-1-must-be-pyga/74077144#74077144)  
- [How to open camera with pygame in Windows?](https://stackoverflow.com/questions/29673348/how-to-open-camera-with-pygame-in-windows)  
- [hard lag when webcam is release(https://stackoverflow.com/questions/74215542/hard-lag-when-webcam-is-release/74217826#74217826)  

📁 **[Minimal example - OpenCV Camera capture](../../examples/minimal_examples/pygame_minimal_video_camera.py)**

📁 **[Minimal example - Camera capture (pygame.camera)](../../examples/minimal_examples/pygame_minimal_video_camera_2.py)**

📁 **[Minimal example - OpenCV Camera capture and release](../../examples/minimal_examples/pygame_minimal_video_camera_rlease.py)**

The [`pygame.camera`](https://www.pygame.org/docs/ref/camera.html) is only supported on linux:

> Pygame currently supports only Linux and v4l2 cameras.

An alternative solution is to use the [OpenCV `VideoCapture`](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html). Install OpenCV for Python (_cv2_) (see [opencv-python](https://pypi.org/project/opencv-python/)).

Opens a camera for video capturing:

```py
capture = cv2.VideoCapture(0)
```

Grabs a camera frame:

```py
success, camera_image = capture.read()
```

Convert the camera frame to a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object using [`pygame.image.frombuffer`](https://www.pygame.org/docs/ref/image.html#pygame.image.frombuffer):

```py
camera_surf = pygame.image.frombuffer(camera_image.tobytes(), camera_image.shape[1::-1], "BGR")
```

## Video

Related Stack Overflow questions:

- [How to load and play a video in pygame](https://stackoverflow.com/questions/21356439/how-to-load-and-play-a-video-in-pygame/69054207#69054207)  
- [How to play video in Pygame currently?](https://stackoverflow.com/questions/62870381/how-to-play-video-in-pygame-currently)

📁 **[Minimal example - Play video with MoviePy](../../examples/minimal_examples/pygame_minimal_video_play.py)**

📁 **[Minimal example - Play video](../../examples/minimal_examples/pygame_minimal_video_play.py)**

The [`pygame.movie`](http://man.hubwiz.com/docset/PyGame.docset/Contents/Resources/Documents/ref/movie.html) is deprecated and not longer supported.

If you only want to show the video you can use [MoviePy](https://zulko.github.io/moviepy/) (see also [How to be efficient with MoviePy](https://stackoverflow.com/questions/21356439/how-to-load-and-play-a-video-in-pygame/69054207#69054207)):

```py
import pygame
import moviepy.editor

pygame.init()
video = moviepy.editor.VideoFileClip("video.mp4")
video.preview()
pygame.quit()
```

An alternative solution is to use the [OpenCV `VideoCapture`](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html). Install OpenCV for Python (_cv2_) (see [opencv-python](https://pypi.org/project/opencv-python/)). However, it should be mentioned that `cv2.VideoCapture` does not provide a way to read the audio from the video file. **This is only a solution to view the video but no audio is played.**

Opens a camera for video capturing:

```py
video = cv2.VideoCapture("video.mp4")
```

Get the frames per second form the `VideoCapture` object:

```py
fps = video.get(cv2.CAP_PROP_FPS)
```

Create a [`pygame.time.Clock`](https://www.pygame.org/docs/ref/time.html):

```py
clock = pygame.time.Clock()
```

Grabs a video frame and limit the frames per second in the application loop:

```py
clock.tick(fps)
success, video_image = video.read()
```

Convert the camera frame to a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object using [`pygame.image.frombuffer`](https://www.pygame.org/docs/ref/image.html#pygame.image.frombuffer):

```py
video_surf = pygame.image.frombuffer(video_image.tobytes(), video_image.shape[1::-1], "BGR")
```
