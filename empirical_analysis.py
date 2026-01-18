import time
import csv
import random
import string
from lcs import lcs

def generate_random_sequence(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def run_empirical_analysis(max_time_seconds=300, initial_size=10):
    csv_filename = 'lcs_analysis.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Input_Size', 'Execution_Time_s', 'LCS_Result'])
    
    current_size = initial_size
    iteration = 0
    
    print("=" * 60)
    print("EMPIRICAL ANALYSIS - LONGEST COMMON SUBSEQUENCE")
    print("=" * 60)
    print(f"Maximum time: {max_time_seconds} seconds ({max_time_seconds/60:.1f} minutes)")
    print(f"Initial size: {initial_size}")
    print(f"Strategy: Doubling size each iteration")
    print("=" * 60)
    print()
    
    try:
        while True:
            iteration += 1
            
            X = generate_random_sequence(current_size)
            Y = generate_random_sequence(current_size)
            
            print(f"Iteration {iteration}: Testing with size {current_size}...", end=" ")
            
            start_time = time.time()
            result = lcs(X, Y)
            execution_time = time.time() - start_time
            
            print(f"Time: {execution_time:.4f}s | LCS: {result}")
            
            with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([current_size, f'{execution_time:.6f}', result])
            
            if execution_time >= max_time_seconds:
                print()
                print("=" * 60)
                print("TIME LIMIT REACHED!")
                print(f"Input size: {current_size}")
                print(f"Execution time: {execution_time:.2f}s ({execution_time/60:.2f} minutes)")
                print(f"Total iterations: {iteration}")
                print("=" * 60)
                break
            
            current_size *= 2
            
    except KeyboardInterrupt:
        print("\n\nAnalysis interrupted by user.")
        print(f"Last input tested: {current_size // 2}")
        print(f"Total iterations: {iteration - 1}")
    
    print(f"\nResults saved in: {csv_filename}")
    print()

if __name__ == "__main__":
    run_empirical_analysis(max_time_seconds=300, initial_size=10)
    
