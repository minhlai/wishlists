"""
Wishlist Service Runner
Start the Wishlist Service and initializes logging
"""

import os
from app import app, service

# Pull options from environment
HOST = os.getenv('HOST', '0.0.0.0')
DEBUG = (os.getenv('DEBUG', 'False') == 'True')
PORT = os.getenv('PORT', '5000')

######################################################################
#   M A I N
######################################################################
if __name__ == "__main__":
    print "****************************************"
    print " W I S H L I S T   S E R V I C E   R U N N I N G"
    print "****************************************"
    service.initialize_logging()
    app.run(host=HOST, port=int(PORT), debug=DEBUG)
