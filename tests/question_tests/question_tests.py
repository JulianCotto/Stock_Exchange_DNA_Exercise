#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_d.question_d import get_profiles, get_consensus
from src.question_c.question_c import get_most_likey_ancenstor_consensus

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())


    def test_get_most_likey_ancestor_consensus(self):
        expected_variable_output0 = 2
        expected_variable_output1 = 4
        expected_variable_output2 = 10
        input1 = "GATATATGCATATACTT"
        input2 = "ATAT"
        output = get_most_likey_ancenstor_consensus(input1, input2)
        output_variable0 = int(output[0])
        output_variable1 = int(output[1])
        output_variable2 = int(output[2])
        
        self.assertEqual(expected_variable_output0, output_variable0)
        self.assertEqual(expected_variable_output1, output_variable1)
        self.assertEqual(expected_variable_output2, output_variable2)

    def test_get_profiles(self):
        dna0 = 'AGAATAA'
        dna1 = 'TGTATTT'
        dna2 = 'CGGGGGG'
        dna3 = 'CCGCGCG'
        dna4 = 'AAAAACC'
        dna5 = 'GATAAAA'
        dna6 = 'CCCCCTC'
        dna7 = 'TTTCTTT'
        expected_list = [[5, 1, 0, 0, 5, 5, 0, 0], 
                        [0, 0, 1, 4, 2, 0, 6, 1], 
                        [1, 1, 6, 3, 0, 1, 0, 0], 
                        [1, 5, 0, 0, 0, 1, 1, 6]]
        self.assertEquals(expected_list, 
                        get_profiles(dna0, dna1, 
                                    dna2, dna3, 
                                    dna4, dna5, 
                                    dna6, dna7))
                        
    def test_get_consensus(self):
        expected_list = ['A', 'T', 'G', 'C', 'A', 'A', 'C', 'T']
        profile_list = [[5, 1, 0, 0, 5, 5, 0, 0], 
                        [0, 0, 1, 4, 2, 0, 6, 1], 
                        [1, 1, 6, 3, 0, 1, 0, 0], 
                        [1, 5, 0, 0, 0, 1, 1, 6]]
        self.assertEqual(expected_list, get_consensus(profile_list))
