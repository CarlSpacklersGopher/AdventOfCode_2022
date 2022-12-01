import unittest
import calorie_counting

class TestCalorieCounter(unittest.TestCase):
    def test_example(self):
        '''
        Run the example provided by the prompt
        '''
        calorie_list = []
        with open("day_01/testinput_1.txt", 'r') as f:
            calorie_list = f.readlines()
        
        self.assertEqual(calorie_counting.count_calories(calorie_list), 24000)

    def test_calorie_sums(self):
        '''
        Test each elf's calories are summed correctly
        '''
        elf1 = ['1000', '2000', '3000']
        elf2 = ['4000']
        elf3 = ['5000', '6000']
        elf4 = ['7000', '8000', '9000']
        elf5 = ['10000']

        self.assertEqual(calorie_counting.count_calories(elf1), 6000)
        self.assertEqual(calorie_counting.count_calories(elf2), 4000)
        self.assertEqual(calorie_counting.count_calories(elf3), 11000)
        self.assertEqual(calorie_counting.count_calories(elf4), 24000)
        self.assertEqual(calorie_counting.count_calories(elf5), 10000)

    
    def test_elf_without_food(self):
        '''
        Test that any elf without food is counted correctly
        '''
        elf = []
        self.assertEqual(calorie_counting.count_calories(elf), 0)


if __name__ == '__main__':
    unittest.main()