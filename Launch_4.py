import motor_pair
import motor
from hub import port
import runloop

async def moveForInches(inches, speed= 500):
    degrees = inches * 360 // 11.5
    degrees = round(degrees)
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

async def moveToPosition0():    # has to be async for awaitables
    return

async def runMission9():
    await moveForInches (28.75)
    await turnForDegrees (50)
    await moveForInches(-0.5)
    await motor.run_to_absolute_position(port.F, 265, 1000)
    await turnForDegrees (-49, 100)
    await moveForInches (2)
    await turnForDegrees (-50,300)
    await moveForInches (-3)
    await turnForDegrees (-67)
    await moveForInches(19)
    await turnForDegrees(30)
    await moveForInches(-7)
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, -500, -1200, 2000)
    #await moveForInches(3)
    #await turnForDegrees(-70)
    #await moveForInches(-10)
    
async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    motor.run_to_absolute_position(port.F, 0, 1000)
    await moveToPosition0()
    await runMission9()
runloop.run(main())
