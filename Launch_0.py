import motor_pair
import motor
from hub import port
import runloop

async def moveToPosition0():    # has to be async to use await which is neeeded for running motors cuz those are a kind of Class type called "awaitables"
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, 1000, 1000)        # moves straight for 1 second
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 2000, -1000, 1000)    # does a tank turn to the right for 1 second'

async def runMission3():
    motor.run_for_degrees(port.C, 90, 1000)


async def main():
    await moveToPosition0()
    await runMission3()

runloop.run(main())
