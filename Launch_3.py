import motor_pair
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


async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    # await moveForInches(18, 100)
    await motor.run_to_absolute_position(port.B, 0, 1110)
    for i in range(5):
        await motor.run_to_absolute_position(port.B, 180, 1110)
        await motor.run_to_absolute_position(port.B, 160, 1110)
        await motor.run_to_absolute_position(port.B, 180, 1110)
        await motor.run_to_absolute_position(port.B, 84, 1110)

   # await motor.run_for_degrees(port.B, -35, 750)
    #await moveForInches(-20)



runloop.run(main())
