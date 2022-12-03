import unittest
import calorie_counting as cc

class TestCalorieCounter(unittest.TestCase):
    def test_elf_separation(self):
        '''
        Ensure elf sums are calculated separately
        '''
        calorie_list = cc.get_processed_input("day_01/testinput_1.txt")
        
        self.assertEqual(len(cc.get_calories_per_elf(calorie_list)), 5)

    def test_calorie_sums(self):
        '''
        Test each elf's calories are summed correctly
        '''
        elf1 = [1000, 2000, 3000, cc.ELF_DELIMITER]
        elf2 = [4000, cc.ELF_DELIMITER]
        elf3 = [5000, 6000, cc.ELF_DELIMITER]
        elf4 = [7000, 8000, 9000, cc.ELF_DELIMITER]
        elf5 = [10000, cc.ELF_DELIMITER]

        self.assertEqual(cc.get_calories_per_elf(elf1), [6000])
        self.assertEqual(cc.get_calories_per_elf(elf2), [4000])
        self.assertEqual(cc.get_calories_per_elf(elf3), [11000])
        self.assertEqual(cc.get_calories_per_elf(elf4), [24000])
        self.assertEqual(cc.get_calories_per_elf(elf5), [10000])

    
    def test_elf_without_food(self):
        '''
        Test that any elf without food is counted correctly
        '''
        elf = [cc.ELF_DELIMITER]
        self.assertEqual(cc.get_calories_per_elf(elf), [0])

    def test_calperelf_is_descending(self):

        test_input = [5, 8, cc.ELF_DELIMITER, 
                      1, 3, 2, cc.ELF_DELIMITER, 
                      cc.ELF_DELIMITER,
                      10, 5, 3, cc.ELF_DELIMITER]
        
        self.assertEqual(cc.get_calories_per_elf(test_input), [18, 13, 6, 0])

    def test_get_most_calories(self):
        calorie_list = cc.get_processed_input("day_01/testinput_1.txt")

        cal_per_elf = cc.get_calories_per_elf(calorie_list)

        self.assertEqual(cc.get_most_calories(cal_per_elf), [24000])
        self.assertEqual(cc.get_most_calories(cal_per_elf, num_elves=3), [24000,11000,10000])
        self.assertEqual(cc.get_most_calories(cal_per_elf, num_elves=100), [24000,11000,10000,6000,4000])

    


if __name__ == '__main__':
    unittest.main()