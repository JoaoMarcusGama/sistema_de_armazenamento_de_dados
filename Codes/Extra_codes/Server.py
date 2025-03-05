from pyModbusTCP.server import ModbusServer, DataBank
import random
import time
import logging

logging.basicConfig()
logging.getLogger('pyModbusTCP.server').setLevel(logging.DEBUG)

host='0.0.0.0'
port = 502
unit_id=1

class piDataBank(DataBank):
    def  __init__(self):
        super().__init__()

    def get_holding_registers(self, address, number=1, srv_info=None):

        self._h_regs {0:5544, }



if __name__== '__main__':
    Server = ModbusServer(host=host, port=port)

    Server.start()