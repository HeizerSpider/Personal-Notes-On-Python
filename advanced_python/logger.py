import logging

extData = {
    'user' : 'imanheizer@gmail.com'
    }

def main():
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    datestr = "%d/%m/%Y %I:%M:%S %p"
    
    logging.basicConfig(level=logging.DEBUG, 
                        filename = 'output.log', 
                        filemode = 'w',
                        format = fmtstr,
                        datefmt = datestr)

    logging.debug("This is a debug message", extra = extData)
    logging.info("This is an info message", extra = extData)
    logging.warning("This is a warning message", extra = extData)
    logging.error("This is an error message", extra = extData)
    logging.critical("This is a critical message", extra = extData)

    logging.info("This is a string {0} and this is an int {1}".format("hello", 4), extra = extData)

main()