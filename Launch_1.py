import motor_pair
import motor
from hub import port
import runloop

async def moveForInches(inches, speed= 500):
    degrees = inches * 360 // 11.5
    degrees = round(degrees)
    # motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, speed, speed)
    motor_pair.stop(motor_pair.PAIR_1)
    # motor_pair.unpair(motor_pair.PAIR_1)

async def turnForDegrees(degrees, speed= 500):
    # motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    speedLeft = -1 * speed
    speedRight = speed
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, speedRight, speedLeft)
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(250)
    # motor_pair.unpair(motor_pair.PAIR_1)

async def moveToPosition1():    # has to be async to use await which is neeeded for running motors cuz those are a kind of Class type called "awaitables"
    await motor.run_to_absolute_position(port.F, 234, 500)
    await moveForInches(30)
    await turnForDegrees(-50)
    await moveForInches(4)
    await moveForInches(-7)
    await turnForDegrees(-30)
    await motor.run_for_degrees(port.F, 50, 1000)
    await moveForInches(1)
    await turnForDegrees(-70)
    await turnForDegrees(80)
    await moveForInches(-3)
    await turnForDegrees(45)
    await motor.run_for_degrees(port.F, -10, 1000)
    await moveForInches(7)
    await motor.run_for_degrees(port.F, 60, 1100)
    await moveForInches(-10)
    await turnForDegrees(70)
    await moveForInches(-35)

async def runMission1():
    motor.run_for_degrees(port.C, 90, 1000)


async def main():
    motor.run_to_absolute_position(port.F, 0, 500)
    motor.run_to_absolute_position(port.B, 30, 500)
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    await moveToPosition1()
    #await runMission1()

runloop.run(main())

