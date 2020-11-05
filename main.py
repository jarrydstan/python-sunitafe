import socket

class PythonServer:



    def __init__(self, filename, addr, port):
        self.filename = filename
        self.addr = (addr, port)


    def setupServer(self):

        ps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Python Socket is ready!" + "\n")

        try:
            ps.bind(self.addr)
            ps.listen(5)
            print("Python Socket is Listening!" + "\n")
            conn, addr = ps.accept()
            return conn
        except socket.error as e_msg:
            print(e_msg)


    def readFile(filename):
        f = open(filename, 'rb')
        line = f.read(1024)
        if line:
            print("File reading done...")
        f.close()

        print("File transfer starting...")

        while line:
            conn.send(line)
            print("File Transfer Complete!")


if __name__ == "__main__":
    mpy = PythonServer("myfile.txt", "127.0.0.1", 9999)
    mpy.setupServer()
    mpy.readFile()