
class Knapsack_Dinamic_Programming:
    def knapsack(item_value, item_weights, item_capacity):
        return Knapsack_Dinamic_Programming.knapsack_solution(item_value, item_weights, item_capacity, 0)

    def knapsack_solution(item_value, item_weights, item_capacity, currentIndex):
        if item_capacity <= 0 or currentIndex >= len(item_value):
            return 0

        value1 = 0

        if item_weights[currentIndex] <= item_capacity:
            value1 = item_value[currentIndex] + Knapsack_Dinamic_Programming.knapsack_solution(item_value, item_weights, item_capacity - item_weights[currentIndex], currentIndex+1)

        value2 = Knapsack_Dinamic_Programming.knapsack_solution(item_value, item_weights, item_capacity, currentIndex + 1)

        return max(value1, value2)

def main():
    """
        Nombre -> Precio -> Peso 
        Collar -> 10K -> 1KG
        Anillo -> 50K -> 2.5KG
        Cuadro -> 50K -> 3KG
        Copa -> 30K -> 1.5KG
        Dell -> 30K -> 5KG
        Apple -> 70K -> 6KG

        Backpack -> 9KG
    """
    item_value = [10, 50, 50, 30, 30, 70]
    item_weights= [1, 2.5, 3, 1.5, 5, 6]
    item_capacity = 9

    maxProfit = Knapsack_Dinamic_Programming.knapsack(item_value, item_weights, item_capacity)
    print(f"""
    Maximo valor para los elementos: {item_value}
    Con peso de: {item_weights}
    Para Knapsack capacity: {item_capacity}

    Es ---> {maxProfit}
    """) 

if __name__ == '__main__':
    main()