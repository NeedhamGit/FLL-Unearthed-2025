import motor_pair
import color_sensor
import color
import motor
from hub import port
import runloop

async def moveForInches(inches, speed= 400):
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

async def runMissionShip():
    await moveForInches(30)
    await moveForInches (-4)
    await turnForDegrees (-36)
    await moveForInches(17)
    await turnForDegrees(123)

async def runMissionCoral():
    await moveForInches(17)
    await turnForDegrees(123)
    await motor.run_to_absolute_position(port.F, 243, 1000)
    await moveForInches(3.5, 100)
    for i in range(5):
        await turnForDegrees(42)
        await turnForDegrees(-42)
    await turnForDegrees(21)
    await moveForInches(-5)
    await turnForDegrees(-60)

async def runMissionBucket():
    await moveForInches(7)
    await motor.run_to_absolute_position(port.F, 0, 1000)
    await turnForDegrees(-152)
    await moveForInches(-0.5)
    await motor.run_to_absolute_position(port.F, 243, 1000)
    await moveForInches(-3.5)
    await motor.run_to_absolute_position(port.F, 0, 1000)

async def runToBlueSide():
    await moveForInches(2)
    await turnForDegrees(-100)
    await moveForInches(-50)


async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    motor.run_to_absolute_position(port.F, 0, 1000)
    await runMissionShip()
    await runMissionCoral()
    await runMissionBucket()
    await runToBlueSide()

runloop.run(main())
