from djitellopy import Tello

tello = Tello()

tello.connect()
tello.streamon()
tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)




#tello.flip_forward()
#tello.flip_back()
#tello.land()
#tello.takeoff()
#tello.move_left(100)
#tello.flip_forward()
#tello.flip_back()
#tello.rotate_counter_clockwise(90)
#tello.flip_forward()
#tello.flip_back()
