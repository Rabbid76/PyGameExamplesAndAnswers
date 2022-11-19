[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Joystick

Related Stack Overflow questions:

- [How do I get xbox controls outside event loop in pygame?](https://stackoverflow.com/questions/73502525/how-do-i-get-xbox-controls-outside-event-loop-in-pygame/73502685#73502685)  
  ![How do I get xbox controls outside event loop in pygame?](https://i.stack.imgur.com/xXIOv.gif)

  :scroll: **[move with joystick](../../examples/minimal_examples/pygame_minimal_joystick_1.py)**

- [how to make sprite move upwards and downwards with joystick in PyGame](https://stackoverflow.com/questions/54677539/how-to-make-sprite-move-upwards-and-downwards-with-joystick-in-pygame/54679667#54679667)  
  ![how to make sprite move upwards and downwards with joystick in PyGame](https://i.stack.imgur.com/VXFfF.gif)

- [problems with pygame controller support](https://stackoverflow.com/questions/68218005/problems-with-pygame-controller-support/68219654#68219654)  
  ![problems with pygame controller support](https://i.stack.imgur.com/eZlPa.gif)
  
```py
joystick = None
run  = True
while run:

    move = [0, 0]
    if joystick:
        axis_x, axis_y = (joystick.get_axis(0), joystick.get_axis(1))
        if abs(axis_x) > 0.1:
            move[0] = speed * axis_x
        if abs(axis_y) > 0.1:
            move[1] = speed * axis_y
    else:
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            print("joystick initialized")
```

## USB joystick

Related Stack Overflow questions:

- [How to get USB controller/gamepad to work with python](https://stackoverflow.com/questions/60309652/how-to-get-usb-controller-gamepad-to-work-with-python/60323121#60323121)


## Gamepad issues

Related Stack Overflow questions:

- [Getting the number of axes for Logitech G920](https://stackoverflow.com/questions/56569442/getting-the-number-of-axes-for-logitech-g920)

## Xbox issues

Related Stack Overflow questions:

- [Pygame Xbox One Controller](https://stackoverflow.com/questions/49887874/pygame-xbox-one-controller)  
- [Controller Support in PyGame](https://stackoverflow.com/questions/49987072/controller-support-in-pygame)  
- [Pygame: Analog trigger initial value is not the neutral trigger position](https://stackoverflow.com/questions/53267296/pygame-analog-trigger-initial-value-is-not-the-neutral-trigger-position)  
- [How to know if a joystick is XInput in pygame?](https://stackoverflow.com/questions/54494141/how-to-know-if-a-joystick-is-xinput-in-pygame)  
- [Is there a way to receive inputs from xbox controller triggers, in pygame?](https://stackoverflow.com/questions/59604049/is-there-a-way-to-receive-inputs-from-xbox-controller-triggers-in-pygame)  

:scroll: **[Joystick test tool`](../../tools/pygame/pygame_joystick_test.py)**
