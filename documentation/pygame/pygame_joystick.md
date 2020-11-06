[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Joystick

Related Stack Overflow questions:

- [how to make sprite move upwards and downwards with joystick in PyGame](https://stackoverflow.com/questions/54677539/how-to-make-sprite-move-upwards-and-downwards-with-joystick-in-pygame/54679667#54679667)
- [How to get USB controller/gamepad to work with python](https://stackoverflow.com/questions/60309652/how-to-get-usb-controller-gamepad-to-work-with-python/60323121#60323121)

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
