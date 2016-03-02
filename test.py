from APMC.APMConnector import APMConnector


def main():
    vehicle = APMConnector('/dev/ttyUSB0',57600)
    #vehicle.connect()
    vehicle.getAttributes()
    vehicle.addListeners()
    vehicle.armed()
    #vehicle.getHomeLocation()
    vehicle.gerParams()
    vehicle.armAndTakeOff(1)
    #vehicle.sendNedVelocity(1,0,0,2)


if __name__ == '__main__':
    main()