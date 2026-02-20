from Assembler import Pass1Assembler, Pass2Assembler, AssemblerError
from Assembler import Assembler
import sys
import os

SAMPLES_DIR = "samples/"
TESTS = [f"{SAMPLES_DIR}{i}.asm" for i in range(1, 10)]
ASSEMBLER_ERRORS = [f"{SAMPLES_DIR}AssemblerError{i}.asm" for i in range(1, 5)]

def compare_files(file1_path: str, file2_path: str) -> bool:
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        content1 = f1.read().strip()
        content2 = f2.read().strip()
        return content1 == content2

def _make_gold_standard():
    # Generate gold standard files for test cases
    for asm_path in TESTS:
        gold_path = asm_path + ".obj.gold"
        A = Assembler(asm_path, gold_path)
        A.assemble()
    for asm_path in ASSEMBLER_ERRORS:
        try:
            gold_path = asm_path + ".obj.gold"
            A = Assembler(asm_path, gold_path)
            A.assemble()
        except AssemblerError:
            pass  # Expected exception
        except Exception as e:
            print(f"Unexpected error while generating gold standard for {asm_path}: {e}", file=sys.stderr)

def main():
    # Temporary function to run a single test case
    for asm_path in TESTS:
        print(f"Testing Assembler on {asm_path}...")
        obj_path = asm_path + ".obj"
        gold_path = asm_path + ".obj.gold"
        A = Assembler(asm_path, obj_path)
        A.assemble()
        assert compare_files(obj_path, gold_path), f"Test failed for {asm_path}"
    for asm_path in ASSEMBLER_ERRORS:
        print(f"Testing Assembler Error handling on {asm_path}...")
        obj_path = asm_path + ".obj"
        A = Assembler(asm_path, obj_path)
        try:
            A.assemble()
            raise AssertionError(f"Expected AssemblerError for {asm_path}, but none was raised.")
        except AssemblerError as e:
            print(f"Caught expected AssemblerError: {e}")
            A.cleanup()  # Clean up any generated files even in error cases

if __name__ == "__main__":
    # _make_gold_standard()
    main()