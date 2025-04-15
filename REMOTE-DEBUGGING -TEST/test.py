import time
import random

def process_numbers(n):

    total = 0
    for i in range(n):
        total += i

        print(f"Processing {i}: Total = {total}")
        time.sleep(0.1)  
    return total

def simulate_workload(iterations):

    results = []
    for j in range(iterations):
        num = random.randint(5, 15)
        print(f"\nIteration {j+1}: Processing number {num}")
        result = process_numbers(num)
        print(f"Iteration {j+1}: Result = {result}")
        results.append(result)
    return results

def main():
    print("Program başladı.")
    

    iterations = 3
    print("Workload simülasyonuna başlıyoruz...")
    all_results = simulate_workload(iterations)
    
    print("\nTüm işlemler tamamlandı!")
    print("Sonuçlar:", all_results)

    print("\nEkstra döngü başlıyor:")
    for k in range(5):
        print(f"Ekstra döngü adımı: {k}")
        time.sleep(0.2)
    
    print("Program sonlandı.")

if __name__ == '__main__':
    main()
