import copy


class Router:
    def __init__(self, buffer: list = None, linkedServers: list = None):
        if not buffer: self.buffer = []
        if not linkedServers: self.linkedServers = []

    def link(self, server):
        self.linkedServers.append(server)
        server.router = self

    def unlink(self, server):
        self.linkedServers.remove(server)
        server.router = None

    def send_data(self):
        for data in self.buffer:
            for server in self.linkedServers:
                if data.ip == server.ip: server.buffer.append(data)
        self.buffer.clear()

    def __str__(self):
        return "I'm your router"


class Server:
    _IP = 0

    def __new__(cls, *args, **kwargs):
        cls._IP += 1
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, buffer: list = None, ip=None):
        if not buffer: self.buffer = []
        self.ip = self.get_ip()
        self.router = None

    def send_data(self, data):
        self.router.buffer.append(data)

    def get_data(self):
        get_buffer_list = copy.copy(self.buffer)
        self.buffer.clear()
        return get_buffer_list

    @classmethod
    def get_ip(cls):
        return cls._IP

    def __repr__(self):
        return f"server ip {self.ip}"


class Data:
    def __init__(self, text: str, ip: int):
        self.text = text
        self.ip = ip

    def __repr__(self):
        return f"data: {self.text}\tto server ip {self.ip}"


# serverList = []
# for i in range(4):
#     serverList.append(Server())
#     print(serverList[i].ip)
# router = Router()
# server_1 = Server()
# data = Data("hello", 2)
# server_1.send_data(data)
# server_2 = Server()
# router.link(server_1)
# router.link(server_2)
# router.send_data()
# print(router)
# print(server_1)
# print(server_2)
# print(f"{data.ip}, {data.text}")
# print(router.linkedServers)
# print(server_2.buffer)
# print(server_2.get_data())
# print(server_2.buffer)

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
