import numpy.random as nr


class UniformGenerator:
    def __init__(self, m, d):
        self._a = m - d
        self._b = m + d

        if self._a < 0:
            self._a = 0
        
        if self._b < 0:
            self._b = 0


    def next(self):
        return nr.uniform(self._a, self._b)


class ConstGenerator:
    def __init__(self, m):
        if m <= 0:
            raise ValueError('Параметр должен быть больше 0')
        self._m = m

    def next(self):
        return self._m




class Operator():
    def __init__(self, m, d):
        self.generator = UniformGenerator(m, d)
        self.time_to_start = float('Inf')
        self.queue = 0
        self.maxQueue = 0
        self.countOfPeople = 0
        
    def gen_new_time(self, current_time):
        g_next = self.generator.next()
        self.time_to_start = current_time +  g_next

    def add_to_queue(self, current_time):
        if self.queue == 0:
            self.gen_new_time(current_time)
        self.queue += 1
        if self.queue > self.maxQueue:
            self.maxQueue = self.queue
        return self.queue

    def get_from_queue(self):
        if self.queue:
            self.queue -= 1
            self.countOfPeople += 1
            if self.queue > 0:
                self.gen_new_time(self.time_to_start)
            else:
                self.time_to_start = float('Inf')
            return 1
        else:
            return 0


    def gen_prob(self):
        return nr.uniform()


class Generator():
    def __init__(self, m, d, mx = 500):
        self.generator = UniformGenerator(m, d)
        self.time_to_start = 0
        self.max_req = mx
        self.gen_new_time()
    def gen_new_time(self):
        self.time_to_start += self.generator.next()

    def get_from_queue(self):
        if self.max_req > 0:
            self.max_req -= 1
            return 1
        else:
            return None 



def event_based_modelling(client_m = 1, client_d = 0,
                          ter0_m = 50, ter0_d = 0, ter1_m = 30, ter1_d = 0, ter2_m = 60, ter2_d = 0, car0_m = 400, car0_d = 0,
                           ekg_m = 40, ekg_d = 0, ter0_prob = 0.5, ter1_prob=0.3, ter2_prob=0.7, ekg_prob=0.6, all = 100 ):
    client_gen = Generator(client_m, client_d, all)

    ter0 = Operator(ter0_m, ter0_d)
    ter1 = Operator(ter1_m, ter1_d)
    ter2 = Operator(ter2_m, ter2_d)

    car0 = Operator(car0_m, car0_d)

    ekg = Operator(ekg_m, ekg_d)


    stuff = [client_gen, ter0, ter1, ter2, car0, ekg]
    current_time = 0

    while True:
        allCur = 0
        for i in range(1, 4):
            allCur += stuff[i].countOfPeople
        if allCur == all:
            break
        if client_gen.max_req > 0:
            current_time, index = client_gen.time_to_start, 0
        else:
            current_time, index = ter0.time_to_start, 1
            client_gen.time_to_start = float('Inf')

        for i, device in enumerate(stuff):
            if 0 < device.time_to_start < current_time:
                current_time = device.time_to_start
                index = i
        print(current_time, index, "|", client_gen.time_to_start, ter0.time_to_start, ter1.time_to_start, ter2.time_to_start, car0.time_to_start, ekg.time_to_start)
        print('begin ', ter0.queue, ter1.queue, ter2.queue, car0.queue, ekg.queue)
        if index == 0:
            if client_gen.max_req <= 0:
                continue
            req = client_gen.get_from_queue()
            if req is None:
                client_gen.time_to_start = float('Inf')
                continue 

            client_gen.gen_new_time()
            minQueue = float("Inf")
            minQueueIndex = -1
            for i in range(1, 4):
                if stuff[i].queue < minQueue:
                    minQueue = stuff[i].queue
                    minQueueIndex = i
                
            stuff[minQueueIndex].add_to_queue(current_time)
            
        elif index == 1:
            res = ter0.get_from_queue()
            if res == 0:
                continue
            p = ter0.gen_prob()
            if p <= ter0_prob:
                car0.add_to_queue(current_time)

        elif index == 2:
            res = ter1.get_from_queue()
            if res == 0:
                continue
            p = ter1.gen_prob()
            if p <= ter1_prob:
                car0.add_to_queue(current_time)

        elif index == 3:
            res = ter2.get_from_queue()
            if res == 0:
                continue
            p = ter2.gen_prob()
            if p <= ter2_prob:
                car0.add_to_queue(current_time)

        elif index == 4:
            res = car0.get_from_queue()
            if res == 0:
                continue
            
            p = car0.gen_prob()
            if p <= ekg_prob:
                ekg.add_to_queue(current_time)
            
        elif index == 5:
            ekg.get_from_queue()   
        print('end ', ter0.queue, ter1.queue, ter2.queue, car0.queue, ekg.queue)   
    maxQueue = ter0.maxQueue, ter1.maxQueue, ter2.maxQueue, car0.maxQueue, ekg.maxQueue
    AllCount = ter0.countOfPeople, ter1.countOfPeople, ter2.countOfPeople, car0.countOfPeople, ekg.countOfPeople               
    print(maxQueue, AllCount)
    return maxQueue, AllCount
    

event_based_modelling()

if __name__ == "__main__":
    pass
    #event_based_modelling(10,8,20,5,40,10,40,20,15,30)