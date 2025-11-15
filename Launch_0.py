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
    await motor.run_to_absolute_position(port.F,235,1000)
    await moveForInches(28, 500)            #mission 2
    await turnForDegrees(-50, 400)
    await moveForInches(7, 500)
    await moveForInches(-9, 500)
    await motor.run_to_absolute_position(port.F,244,1000)
    await turnForDegrees(-120, 250)    #mission 1
    await turnForDegrees(125, 250)
    await turnForDegrees(47, 250)    #Transition between mission 1 and 3
    await moveForInches(-4, 400)
    #Option 2: Stabilize First
    #await turnForDegrees(165)
    #await motor.run_to_absolute_position(port.F, 0, 1000)
    #await turnForDegrees(-80)
    #await moveForInches(20)

    #Option 1: Direct
    #await turnForDegrees(165)
    #await moveForInches(10)
    #await turnForDegrees(30)
    #await moveForInches(6)
    #await turnForDegrees(-96)


async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    motor.run_to_absolute_position(port.F, 0, 1000)
    await moveToPosition0()

runloop.run(main())
