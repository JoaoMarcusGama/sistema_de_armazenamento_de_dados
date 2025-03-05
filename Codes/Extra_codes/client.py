from pyModbusTCP.client import ModbusClient

host='127.0.0.1'
port = 502
unit_id=1

class Modbus:

    def __init__(self, host, port, unit_id):
        self.host = host
        self.port = port
        self.unit = unit_id
        self.auto_open = False
        self.auto_close = False
        self.modbus_client = None
        self.response = None

    def modbus_connect(self):

        if not self.modbus_client:
            print("Criando a instância do cliente modbus")
            self.modbus_client = ModbusClient(host=self.host, port=self.port,
                                              unit_id=self.unit,
                                              auto_open=self.auto_open,
                                              auto_close=self.auto_close)
            
            print("Criando conexão")

            if self.modbus_client.open():
                print("Conectado ao servidor Modbus em: ",self.host)
            
            else:
                print("Conectado ao servidor Modbus em: ",self.host, " FALHA!")
                self.modbus_client = None












modbus_client=ModbusClient(host=host, port=port, unit_id=unit_id, auto_open=True)

if __name__=='__main__':
    while True:
        regs = modbus_client.read_holding_registers(0,2)
        print(regs)