class Kata:
    def __init__(self, number, text):
        self.number = number
        self.text = text

    def __str__(self):
        return '\nFrom __str__\n' + 'number: ' + str(self.number) + ', text: ' + self.text

    def print(self):
        print('\nFrom print')
        print('number: ' + str(self.number) + ', text: ' + self.text)
