from hub import motion_sensor
from hub import port
import time
import motor_pair
import runloop

def get_yaw():
   print(motion_sensor.tilt_angles()[0])
   return -10 * motion_sensor.tilt_angles()[0]

async def turn_for_degrees(degrees, speed=250):
    speedLeft = -1 * speed
    speedRight = speed
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, speedRight, speedLeft)
    if (get_yaw() - (-10 * degrees) < 100):
      return
    else:
      
      motor_pair.move_tank()
   
async def move_for_time(seconds, speed):
   start = time.time()
   motion_sensor.reset_yaw(0)
   while True:
    elapsed = time.time() - start
    motor_pair.move(motor_pair.PAIR_1, get_yaw(), velocity= speed)
    if elapsed > 5: # time is up
        break


async def main():
   motion_sensor.set_yaw_face(motion_sensor.FRONT)  
   motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
   await turn_for_degrees(90)

runloop.run(main())
