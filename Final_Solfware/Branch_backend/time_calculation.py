class calculations:
    Avg_data = {}
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
    
    def add_data(self,inputs = ""):
        calculations.Avg_data[inputs]= 1000


if __name__ == '__main__':
    calculations.add_data("A000")
    calculations.add_data("A001")
    calculations.add_data("A002")
    print(calculations.Avg_data)