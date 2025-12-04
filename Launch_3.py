import motor_pair
import color_sensor
import color
import motor
from hub import port
import runloop


async def moveForInches(inches, speed= 500):
    degrees = inches * 360 // 11.5
    degrees = round(degrees)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, speed, speed)
    motor_pair.stop(motor_pair.PAIR_1)

async def turnForDegrees(degrees, speed= 500):
    speedLeft = -1 * speed
    speedRight = speed
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, speedRight, speedLeft)
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(500)

async def moveToPosition0():
    await motor.run_to_absolute_position(port.F,0,2000)
    await moveForInches (14)
    for x in range(4):
        await motor.run_to_absolute_position(port.F,260,2000)
        await runloop.sleep_ms(200)    
        await motor.run_to_absolute_position(port.F,0,2000)
        await runloop.sleep_ms(200)
    await moveForInches (-14)

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    motor.run_to_absolute_position(port.F, 0, 1000)
    await moveToPosition0()
