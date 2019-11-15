class calculations:
    def __init__(self,name,ticket_type="",counter_type="",before_queuein={}):
        self.ticket_type = ticket_type
        self.counter_type = counter_type 
        self.before_queue = before_queuein
        self.name = name

    def on_update(self,input = ""):
        buffer = 0
        if(input in self.before_queue):
            del self.before_queue[input]
            for i in self.before_queue:
                buffer += self.before_queue[i]
            return buffer,self.before_queue
        return -1,-1


if __name__ == '__main__':
    static_data = {"a":100,"b":100,"c":100,"d":100,"e":100,"f":100}
    tt = calculations(name = "A000",ticket_type="ticket_a",counter_type="counter_a",before_queuein = static_data)
    a,b = tt.on_update("a") 
    print(static_data)
    k = calculations(name = "A001",ticket_type="ticket_a",counter_type="counter_a",before_queuein = static_data)
    print(k.before_queue)
    a,b = tt.on_update("b")
    print(k.before_queue)
    a,b = k.on_update("b")
    print(tt.before_queue)
    print(k.before_queue)