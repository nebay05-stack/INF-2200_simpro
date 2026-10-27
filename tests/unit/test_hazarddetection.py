import unittest
from elements.hazard_detection_unit import Hazard_detection
from common import Value

class TestHazardDetection(unittest.TestCase):
    def setUp(self):
        self.hazard_detection = Hazard_detection()
        self.id_ex_RegWrite = Value(0)
        self.muxregdist_result = Value(0)
        self.ex_mem_RegWrite = Value(0)
        self.ex_mem_reg_dst = Value(0)
        self.if_id_rs = Value(8)
        self.if_id_rt = Value(9)
        self.branch_taken = Value(0)
      

        
    def test_connectInputs(self):
        self.hazard_detection.connectInputs([self.id_ex_RegWrite, self.muxregdist_result, self.ex_mem_RegWrite, self.ex_mem_reg_dst, self.if_id_rs, self.if_id_rt, self.branch_taken])
        self.assertEqual(self.hazard_detection.if_id_rs.value, 8)
        self.assertEqual(self.hazard_detection.if_id_rt.value, 9)

    def test_writeOutput_no_hazard(self):
        self.hazard_detection.connectInputs([self.id_ex_RegWrite, self.muxregdist_result, self.ex_mem_RegWrite, self.ex_mem_reg_dst, self.if_id_rs, self.if_id_rt, self.branch_taken])
        self.hazard_detection.writeOutput()
        self.assertEqual(self.hazard_detection.pc_write.value, 1)
        self.assertEqual(self.hazard_detection.if_id_write.value, 1)
        self.assertEqual(self.hazard_detection.id_ex_flush.value, 0)
        self.assertEqual(self.hazard_detection.if_id_flush.value, 0)

        
    def test_writeOutput_data_hazard_stall(self):
        self.id_ex_RegWrite.value = 1
        self.muxregdist_result.value = 8
        self.hazard_detection.connectInputs([self.id_ex_RegWrite, self.muxregdist_result, self.ex_mem_RegWrite, self.ex_mem_reg_dst, self.if_id_rs, self.if_id_rt, self.branch_taken])
        self.hazard_detection.writeOutput()
        self.assertEqual(self.hazard_detection.pc_write.value, 0)
        self.assertEqual(self.hazard_detection.if_id_write.value, 0)
        self.assertEqual(self.hazard_detection.id_ex_flush.value, 1)
        self.assertEqual(self.hazard_detection.if_id_flush.value, 0)

    def test_writeOutput_branch_taken_flsuh(self):
        self.id_ex_RegWrite.value = 0
        self.muxregdist_result.value = 0
        self.branch_taken.value = 1
        self.hazard_detection.connectInputs([self.id_ex_RegWrite, self.muxregdist_result, self.ex_mem_RegWrite, self.ex_mem_reg_dst, self.if_id_rs, self.if_id_rt, self.branch_taken])
        self.hazard_detection.writeOutput()
        self.assertEqual(self.hazard_detection.pc_write.value, 1)
        self.assertEqual(self.hazard_detection.if_id_write.value, 1)
        self.assertEqual(self.hazard_detection.id_ex_flush.value, 0)
        self.assertEqual(self.hazard_detection.if_id_flush.value, 1)

        



    


    
