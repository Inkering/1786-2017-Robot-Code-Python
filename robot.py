import magicbot
import wpilib

import pytest

from robotpy_ext.control.button_debouncer import ButtonDebouncer
from robotpy_ext.common_drivers import navx, distance_sensors

from networktables.networktable import NetworkTable

class myRobot(magicbot.MagicRobot):
    def createObjects(self):
        #Sticks
        self.driverStick = wpilib.Joystick(1)
        self.operatorStick = wpilib.Joystick(0)

        #CAN Talons
        self.lf = wpilib.CANTalon(2)
        self.lr = wpilib.CANTalon(3)
        self.rf = wpilib.CANTalon(4)
        self.rb = wpilib.CANTalon(5)

        #robot drive to eventually control our mecanum drive train
        self.robotDrive = wpilib.RobotDrive(self.lf, self.lr, self.rf, self.rb)

        #Intake motor
        self.intakeController = wpilib.CANTalon(6)

        #Shooter motor
        self.intakeController = wpilib.CANTalon(7)

        #Climber motor
        self.climbController = wpilib.CANTalon(8)

        #agitator
        # Maybe be deprecated because of a simpler solution
        self.aggitController = wpilib.CANTalon(9)

        # IMU Gyroscope
        self.navX = navx.AHRS.create_spi()

        #network tables
        self.sd = NetworkTable.getTable('smartdashboard')
        self.viz = NetworkTable.getTable('visiondashboard')