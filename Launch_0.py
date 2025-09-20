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
    await runloop.sleep_ms(250)
    
async def moveToPosition0():    # has to be async to use await which is neeeded for running motors cuz those are a kind of Class type called "awaitables"
    await moveForInches(2)
    await turnForDegrees(63)
    await moveForInches(37.5)
    await turnForDegrees(-60)        # moves straight
    await moveForInches(8.5)         # turns left
    await turnForDegrees(-147)       # moves backwards
    await moveForInches(1.15)         # turns left
    await motor.run_for_degrees(port.F, -147, 1000)
    #await moveForInches(465)


async def runMission13():
    motor.run_for_degrees(port.F, -147, 1000)


async def main():
    motor.run_to_absolute_position(port.F, 4, 500)
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    # await turnForDegrees(90)
    # await moveForInches(6)
    # motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1000, 500, 500)
    await moveToPosition0()

runloop.run(main())
