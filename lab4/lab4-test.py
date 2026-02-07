from Assembler import Pass1Assembler, AssemblerError
import sys
import os

SAMPLES_DIR = "samples/"
TESTS = [f"{SAMPLES_DIR}{i}.asm" for i in range(1, 5)]
ASSEMBLER_ERRORS = [f"{SAMPLES_DIR}AssemblerError{i}.asm" for i in range(1, 5)]

def compare_files(file1_path: str, file2_path: str) -> bool:
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        content1 = f1.read().strip()
        content2 = f2.read().strip()
        return content1 == content2

def run_pass1(asm_path: str, target_path: str):
    with open(asm_path, 'r') as source_file, open(target_path, 'w') as target_file:
        assembler = Pass1Assembler(source_file, target_file)
        assembler.run()

def _make_gold_standard():
    # Generate gold standard files for test cases
    for asm_path in TESTS:
        gold_path = asm_path + ".pass1.gold"
        run_pass1(asm_path, gold_path)
    for asm_path in ASSEMBLER_ERRORS:
        try:
            gold_path = asm_path + ".pass1.gold"
            run_pass1(asm_path, gold_path)
        except AssemblerError:
            pass  # Expected exception
            os.remove(gold_path)  # Remove any partial output
        except Exception as e:
            print(f"Unexpected error while generating gold standard for {asm_path}: {e}", file=sys.stderr)

def main():
    for asm_path in TESTS:
        print(f"Testing Pass 1 on {asm_path}...")
        target_path = asm_path + ".pass1"
        gold_path = asm_path + ".pass1.gold"
        run_pass1(asm_path, target_path)
        assert compare_files(target_path, gold_path), f"Test failed for {asm_path}"
    
    for asm_path in ASSEMBLER_ERRORS:
        print(f"Testing Assembler Error handling on {asm_path}...")
        try:
            run_pass1(asm_path, target_path=asm_path + ".pass1")
            raise AssertionError(f"Expected AssemblerError for {asm_path}, but none was raised.")
        except AssemblerError as e:
            print(f"Caught expected AssemblerError: {e}")
            pass  # Expected exception

if __name__ == "__main__":
    # _make_gold_standard()
    main()