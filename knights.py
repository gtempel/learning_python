# < 3 knights, retreat
# > 10 knights, trojan rabbit
# otherwise, try to sign truce

import unittest

def take_action(number_of_knights):
  if number_of_knights < 3:
    return "retreat!"
  elif number_of_knights >= 10:
    return 'trojan rabbit!'
  else:
    return 'attempt truce'

num_knights = int(input('Enter the number of knights: '))
print('You entered:', num_knights)
print(take_action(num_knights))


class Tests(unittest.TestCase):
  def test_retreat_for_less_than(self):
    self.assertEqual(take_action(2), 'retreat!')
  
  def test_truce_for_retreat_threshold(self):
    self.assertEqual(take_action(3), 'attempt truce')
  
  def test_truce_for_trojan_rabbit_threshold(self):
    self.assertEqual(take_action(10), 'trojan rabbit!')
  
  def test_truce(self):
    self.assertEqual(take_action(5), 'attempt truce')

  def test_trojan_rabbit(self):
    self.assertEqual(take_action(11), 'trojan rabbit!')


if __name__ == '__main__':
    unittest.main()
