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

async def runMission5():
    await moveForInches(-28)
    for i in range(3):
        await motor.run_to_absolute_position(port.B, 0, 1500)
        await motor.run_for_degrees(port.B, 200, 1750)
        await motor.run_for_degrees(port.B, -50, 1750)
        await motor.run_for_degrees(port.B, 50, 1750)
    await motor.run_to_absolute_position(port.B, 0, 10000)
    await moveForInches(28)

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    await runMission5()


runloop.run(main())
