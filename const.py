# create module to retrieve constants and bindings using key-value storage
class _const:

    class ConstError(TypeError): pass

    # set constant attribute using the name and value
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)"%name)
        self.__dict__[name] = value

    # delete constant attribute using the name
    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("Can't unbind const(%s)"%name)
        raise NameError(name)

# set the class as a system module
import sys
sys.modules[__name__] = _const()

# set global constants (cannot be changed after this class)
import const
# name of the current project
const.projectName = "MadMobile"

# motor GPIO pin numbers to connect via raspberry pi
const.rightMotorFrontPin = 1
const.rightMotorBackPin = 2
const.leftMotorFrontPin = 3
const.leftMotorBackPin = 4

# keys to connect to mapping api
const.mapQuestApiKey = "vtJYRcXbeLw2mQ66f6LWDRMaFn4E1D67"
const.googleMapsApiKey = "AIzaSyAuPFEQGq-5JohYzHZxJpQ6buf24tU_dmU"
const.mapboxApiKey = "sk.eyJ1IjoibWFhbml0bSIsImEiOiJjajY1YTFjdDEyMTlzMnFvM3FwcjRxZXY5In0.RF3RkIbvcfDiIK4xB2eBxQ"

# motor and cruise
const.motorZeroSpeed = 0
const.cruiseSpeedIncrement = 3
const.cruiseTopSpeed = 30 # maximum allowed
const.motorMaxSpeed = 100 # maximum capable
const.cruiseMinStopDistance = 50;
const.cruiseMaxStopDistance = 400;
