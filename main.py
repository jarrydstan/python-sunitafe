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
            msg = conn.recv
            print(msg)
            if (msg != None):
                self.readfile(conn)
                if (msg == "Good"):
                    conn.send("Credit check approved")
                    return True
                else:
                    conn.send("Credit Check denied")
                    return False
            else:
                conn.send("[ERROR] Unable to process credit check")
                
                return False
            
            
        except socket.error as e_msg:
            print(e_msg)


    def readFile(self, conn):
        print(self.filename)
        f = open(self.filename, 'rb')
        line = f.read(1024)
        if line:
            print("File reading done...")
        f.close()

        print("File transfer starting...")

        while line:
            conn.send(line)
            print("File Transfer Complete!")


if __name__ == "__main__":
    mpy = PythonServer("myfile.txt", "127.0.0.1", 3030)
    mpy.setupServer()