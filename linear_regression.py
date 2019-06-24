import math


class Regression:

    theta_0 = 0
    theta_1 = 0

    def __init__(self, learning_rate=0.001):
        self.learning_rate = learning_rate

    def train(self, x, y):
        epochs = 10000
        epoch = 1

        while epoch <= epochs:
            gradient_theta_0 = 0
            gradient_theta_1 = 0
            for i, value in enumerate(x):
                gradient_theta_0 += self.__calculate_cost(value, y[i])
                gradient_theta_1 += gradient_theta_0 * value
            epoch += 1

            print(gradient_theta_0 + gradient_theta_1)
            self.theta_0 -= self.learning_rate * (1/len(x)) * gradient_theta_0
            self.theta_1 -= self.learning_rate * (1/len(x)) * gradient_theta_1

    def __calculate_cost(self, x, y):
        return self.__hypothesis(x) - y

    def __hypothesis(self, x):
        return self.theta_0 + self.theta_1 * x

    def predict(self, x):
        return self.__hypothesis(x)


reg = Regression()
first_year = [3, 2, 4, 0, 3, 2, 0, 0, 3, 3, 1, 3, 3, 2, 4, 0, 3, 2, 0, 0, 3, 3, 1, 3]
second_year = [4, 1, 3, 1, 4, 1, 0, 1, 5, 2, 3, 3, 4, 2, 3, 1, 4, 4, 0, 1, 4, 2, 2, 4]
reg.train(first_year, second_year)

print(math.ceil(reg.predict(3)))
