import sys
from PyQt5 import QtWidgets, uic
import numpy as np
from copy import copy

ui_file = 'ui_maindialog.ui'
form, base = uic.loadUiType(ui_file)


class Randomizer:
    def __init__(self, a, b, input_lambda):
        self.a = a
        self.b = b
        self.input_lambda = input_lambda

    def uniform_random(self):
        return np.random.gamma(self.a, self.b)

    def exponential_random(self):
        return np.random.exponential(self.input_lambda)


class Generator:
    def __init__(self, randomizer, requests):
        self.randomizer = randomizer
        self.num_requests = requests

    def generate_request(self):
        self.num_requests -= 1

    def get_new_delay(self):
        result = -1
        while result < 0:
            result = self.randomizer.uniform_random()
        return result


class Processor:
    def __init__(self, randomizer, probability):
        self.randomizer = randomizer
        self.queue_size, self.received, \
        self.max_queue_size, self.reenters, self.processed = 0, 0, 0, 0, 0
        self.probability = probability

    def receive_request(self):
        self.queue_size += 1
        self.received += 1
        self.max_queue_size = max(self.max_queue_size, self.queue_size)

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
    def __init__(self, generator, processor):
        self.generator = generator
        self.processor = processor

    def event_mode(self):
        generated_time = 0
        processed_time = self.generator.get_new_delay()
        generated_estimate = copy(self.generator.num_requests)
        while self.processor.processed < generated_estimate + self.processor.reenters:
            if generated_time <= processed_time:
                self.generator.generate_request()
                self.processor.receive_request()
                generated_time += self.generator.get_new_delay()
            else:
                self.processor.process()
                if self.processor.queue_size > 0:
                    processed_time += self.processor.get_new_delay()
                else:
                    processed_time = generated_time + self.processor.get_new_delay()

        result = {"processed": self.processor.processed,
                  "reenters": self.processor.reenters,
                  "total_received": self.processor.received,
                  "max_queue": self.processor.max_queue_size,
                  "time": processed_time,
                  "generated_time": generated_time}

        return result

    def dt_mode(self, dt):
        generated_time = self.generator.get_new_delay()
        processed_time = generated_time + self.generator.get_new_delay()
        generated_estimate = copy(self.generator.num_requests)
        current_time = 0
        while self.processor.processed < generated_estimate + self.processor.reenters:
            if generated_time < current_time:
                self.generator.generate_request()
                self.processor.receive_request()
                generated_time += self.generator.get_new_delay()
            if current_time >= processed_time:
                self.processor.process()
                if self.processor.queue_size > 0:
                    processed_time += self.processor.get_new_delay()
                else:
                    processed_time = generated_time + self.processor.get_new_delay()
            current_time += dt

        result = {"processed": self.processor.processed,
                  "reenters": self.processor.reenters,
                  "total_received": self.processor.received,
                  "max_queue": self.processor.max_queue_size,
                  "time": current_time,
                  "gen_time": generated_time}

        return result


class MainWindow(base, form):
    def __init__(self):
        super(base, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        # Input Parameters for Exponential Distribution:
        parameter_a = float(self.lineEdit_a.text())
        parameter_b = float(self.lineEdit_b.text())

        # Input Parameter for Uniform Distribution:
        parameter_lambda = float(self.lineEdit_l.text())

        request_amount = int(self.lineEdit_n.text())
        dt = float(self.lineEdit_dt.text())

        if self.lineEdit_p.text():
            probability = float(self.lineEdit_p.text())
        else:
            probability = -1

        randomizer = Randomizer(parameter_a,
                                parameter_b,
                                parameter_lambda)

        generator = Generator(randomizer, request_amount)

        processor = Processor(randomizer, probability)

        model = Model(generator, processor)

        if self.comboBox.currentIndex() == 0:
            result = model.dt_mode(dt)
            self.textBrowser.append(f"\nДельта-т - моделирование: "
                                    f"\n\tОбработано всего: {result['processed']}"
                                    f"\n\tиз них повторов: {result['reenters']}"
                                    f"\n\tНаибольший размер очереди: {result['max_queue']}"
                                    f"\n\tВремя работы: {result['time']}")
        else:
            result = model.event_mode()
            self.textBrowser.append(f"\nСобытийный подход: "
                                    f"\n\tОбработано всего: {result['processed']}"
                                    f"\n\tиз них повторов: {result['reenters']}"
                                    f"\n\tНаибольший размер очереди: {result['max_queue']}"
                                    f"\n\tВремя работы: {result['time']}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
