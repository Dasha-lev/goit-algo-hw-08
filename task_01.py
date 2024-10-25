import heapq

def min_cost_to_connect_cables(cables):
    #Створюємо купу з довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        #Вартість з'єднання
        cost = first + second
        
        total_cost += cost
        
        heapq.heappush(cables, cost)
    
    return total_cost

cable_lengths = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cable_lengths)
print(f"Мінімальні витрати на з'єднання кабелів: {result}")
