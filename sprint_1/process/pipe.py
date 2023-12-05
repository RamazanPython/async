from multiprocessing import Process, Pipe

def processor(conn):
    conn.send(['Привет', None, 256])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=processor, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # распечатает "['Привет', None, 256]"
    p.join()
