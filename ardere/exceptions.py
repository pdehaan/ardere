class ServicesStartingException(Exception):
    """Exception to indicate Services are still Starting"""


class ShutdownPlanException(Exception):
    """Exception to indicate the Plan should be Shutdown"""