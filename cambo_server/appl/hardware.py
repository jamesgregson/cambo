import os

class DummyHardware:
    def __init__( self, *args, **kwargs ):
        self._name = 'Dummy hardware'
        self._pwmL = 0
        self._pwmR = 0

    @property
    def left_pwm( self ):
        return self._pwmL

    @left_pwm.setter
    def left_pwm( self, val ):
        self._pwmL = max( 0, min( 255, val ) )

    @property
    def right_pwm( self ):
        return self._pwmL

    @right_pwm.setter
    def right_pwm( self, val ):
        self._pwmR = max( 0, min( 255, val ) )
    
    @property
    def quaternion( self ):
        return (1.0, 0.0, 0.0, 0.0)

try:
    import RPi.GPIO as GPIO

    class RasPiHardware:
        def __init__( self, *args, **kwargs ):
            self._name = 'RasPi Hardware'
            GPIO.setwarnings(False)
            GPIO.setmode( GPIO.BCM )
            GPIO.setup( 12, GPIO.OUT )
            GPIO.setup( 13, GPIO.OUT )
            self._pwmL = GPIO.PWM( 12, 1000 )
            self._pwmR = GPIO.PWM( 13, 1000 )
            self._dutyL = 0
            self._dutyR = 0
            self._pwmL.start(self._dutyL)
            self._pwmR.start(self._dutyR)

        @property
        def left_pwm( self ):
            return self._dutyL

        @left_pwm.setter
        def left_pwm( self, val ):
            self._dutyL = max( 0, min( 255, val ) )
            self._pwmL.ChangeDutyCycle(self._dutyL)

        @property
        def right_pwm( self ):
            return self._dutyR

        @right_pwm.setter
        def right_pwm( self, val ):
            self._dutyR = max( 0, min( 255, val ) )
            self._pwmR.ChangeDutyCycle(self._dutyR)

        @property
        def quaternion( self ):
            return (1.0, 0.0, 0.0, 0.0)

except:
    class RasPiHardware(DummyHardware): pass
