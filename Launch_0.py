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

async def RunMission2():   
    await motor.run_to_absolute_position(port.F,235,1000)
    await moveForInches(29, 500)            
    await turnForDegrees(-50, 400)
    await moveForInches(6, 500)
    await moveForInches(-9, 500)
    await motor.run_to_absolute_position(port.F,278,1000)

async def RunMission1():
    await moveForInches(2)
    await turnForDegrees(-120, 150)   
    await turnForDegrees(125, 150)    
    await moveForInches(-4, 400)
    await motor.run_to_absolute_position(port.F,0,1000)

async def RamBackWall():
    await turnForDegrees(52, 300)
    await moveForInches(15,200)
    await moveForInches(-4, 250)
    await turnForDegrees(72, 100)

async def RunMission3():
    await moveForInches(-1,100)
    await turnForDegrees(37, 100)
    await motor.run_to_absolute_position(port.F,240,1000)
    await moveForInches(7.5)
    await motor.run_to_absolute_position(port.F, 330, 100)
    await runloop.sleep_ms(2000)

async def BackToPos0():
    await moveForInches (-8)
    await turnForDegrees (115)
    await moveForInches (40)


async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    motor.run_to_absolute_position(port.F, 0, 1000)
    await RunMission2()
    await RunMission1()
    await RamBackWall()
    await RunMission3()
    await BackToPos0()

runloop.run(main())
