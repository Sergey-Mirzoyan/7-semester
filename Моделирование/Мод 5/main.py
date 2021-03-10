import sys
from PyQt5 import QtWidgets, uic
import numpy as np

ui_file = 'ui_maindialog.ui'
form, base = uic.loadUiType(ui_file)


class Randomizer:
    def __init__(self, a, diff=0):
        self.a = a
        self.d = diff

    def new_random(self):
        result = 0
        if self.d == 0:
            return self.a
        while result <= 0:
            result = np.random.uniform(self.a - self.d, self.a + self.d)
        return result

    def uniform_random(self):
        return self.new_random()

    def exponential_random(self):
        return self.new_random()


class Generator:
    def __init__(self, randomizer, requests):
        self.randomizer = randomizer
        self.num_requests = requests
        self.receivers = []
        self.next = 0

    def generate_request(self):
        self.num_requests -= 1
        for receiver in self.receivers:
            if receiver.receive_request():
                return receiver
        return None

    def get_new_delay(self):
        result = -1
        while result < 0:
            result = self.randomizer.uniform_random()
        return result


class Processor:
    def __init__(self, randomizer, probability=0, max_queue_size=-1):
        self.randomizer = randomizer
        self.queue_size, self.received, \
        self.max_queue_size, self.reenters, self.processed = 0, 0, max_queue_size, 0, 0
        self.probability = probability
        self.next = 0

    def receive_request(self):
        if self.max_queue_size == -1 or self.max_queue_size > self.queue_size:
            self.queue_size += 1
            self.received += 1
            return True
        return False

    def get_new_delay(self):
        result = -1
        while result < 0:
            result = self.randomizer.exponential_random()
        return result

    def process(self):
        if self.queue_size > 0:
            self.queue_size -= 1
            self.processed += 1
        if np.random.random_sample() < self.probability:
            self.reenters += 1
            self.receive_request()


class Model:
    def __init__(self, generator, computers, processors):
        self.generator = generator
        self.computers = computers
        self.processors = processors

    def event_mode(self):
        dropped = 0
        generated_estimate = self.generator.num_requests
        generator = self.generator

        first_computer = self.computers[0]
        second_computer = self.computers[1]
        third_computer = self.computers[2]

        first_processors = self.processors[0]
        second_processors = self.processors[1]

        generator.receivers = [first_computer, second_computer, third_computer]
        first_computer.receivers = [first_processors]
        second_computer.receivers = [first_processors]
        third_computer.receivers = [second_processors]

        blocks = [generator,
                  first_computer,
                  second_computer,
                  third_computer,
                  first_processors,
                  second_processors]

        for block in blocks:
            block.next = 0

        generator.next = generator.get_new_delay()
        first_computer.next = first_computer.get_new_delay()

        while generator.num_requests >= 0:
            current_time = generator.next
            for block in blocks:
                if 0 < block.next < current_time:
                    current_time = block.next

            for block in blocks:
                if current_time == block.next:
                    if not isinstance(block, Processor):
                        assigned_processor = generator.generate_request()
                        if assigned_processor is not None:
                            assigned_processor.next = (current_time +
                                                       assigned_processor.get_new_delay())
                        else:
                            dropped += 1
                        generator.next = current_time + generator.get_new_delay()
                    else:
                        block.process()
                        if block.queue_size == 0:
                            block.next = 0
                        else:
                            block.next = current_time + block.get_new_delay()

        return {"denial_percentage": dropped / generated_estimate * 100,
                "denials": dropped}


class MainWindow(base, form):
    def __init__(self):
        super(base, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        time_clients = int(self.lineEdit_C.text())
        potential_time_clients = int(self.lineEdit_Cpm.text())

        first_operator = int(self.lineEdit_C0.text())
        second_operator = int(self.lineEdit_C1.text())
        third_operator = int(self.lineEdit_C2.text())

        first_processor = int(self.lineEdit_P0.text())
        second_processor = int(self.lineEdit_P1.text())

        potential_first_operators = int(self.lineEdit_C0pm.text())
        potential_second_operators = int(self.lineEdit_C1pm.text())
        potential_third_operators = int(self.lineEdit_C2pm.text())

        clients_number = int(self.lineEdit_n.text())

        generator = Generator(Randomizer(time_clients, potential_time_clients), clients_number)
        computers = [Processor(Randomizer(first_operator, potential_first_operators), max_queue_size=1),
                     Processor(Randomizer(second_operator, potential_second_operators), max_queue_size=1),
                     Processor(Randomizer(third_operator, potential_third_operators), max_queue_size=1)]
        processors = [Processor(Randomizer(first_processor)), Processor(Randomizer(second_processor))]

        model = Model(generator, computers, processors)

        result = model.event_mode()
        self.textBrowser.append(f"\nСобытийный подход: "
                                f"\n\tПроцент отказа в обработке: {result['denial_percentage']}"
                                f"\n\tОтказов: {result['denials']}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
    sys.exit(app.exec_())