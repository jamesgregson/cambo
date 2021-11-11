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