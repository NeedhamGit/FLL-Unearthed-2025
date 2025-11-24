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

async def runMission12b():
    await moveForInches(303)
    await moveForInches (-5)
    await turnForDegrees (-35)

async def moveToPosition1():    # has to be async to use await which is neeeded for running motors cuz those are a kind of Class type called "awaitables"
    while(color_sensor.color(port.E) is not color.BLACK):
         motor_pair.move(motor_pair.PAIR_1, 0, velocity= 300)
    await moveForInches(7);
    await turnForDegrees(125)

    #await moveForInches(-1) --- LEAVE THIS CODE COMMENTED (it is NOT needed)
    #await turnForDegrees(25) --- LEAVE THIS CODE COMMENTED (it is NOT needed)
    
async def runMission11():
    await motor.run_to_absolute_position(port.F, 243, 1000)
    await moveForInches(3.5)
    for i in range(5):
        await turnForDegrees(42)
        await turnForDegrees(-42)
    await turnForDegrees(21)
    await moveForInches(-4)
    #await turnForDegrees(-90)
    #await moveForInches(8)
    #await turnForDegrees(-135)
    #await motor.run_to_absolute_position(port.F, 270, 1000)
    #await turnForDegrees(-35)
    #await moveForInches(0.5)
    #await motor.run_to_absolute_position(port.F, 240, 1000)
    #await moveForInches(-3)
    #await turnForDegrees(-150)
    #await moveForInches(-40)

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    motor.run_to_absolute_position(port.F, 0, 1000)
    #await runMission12b()
    await moveToPosition1()
    await runMission11()

runloop.run(main())