# Create a class kata with fields number and text
# Create two instances
# Print the instance
# Print the fields of each instance (tip: do so by creating a print function in the class and by using __str__)
from kata import Kata

kata1 = Kata(1, 'This is kata number 1')
kata2 = Kata(2, 'This is kata number 2')

print(kata1)
kata1.print()
print(kata2)
kata2.print()
