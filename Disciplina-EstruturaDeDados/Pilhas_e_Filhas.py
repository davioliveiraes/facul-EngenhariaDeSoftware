# Pilha
pilha = []
pilha.append('A') # Adiciona 'A' ao topo da pilha
pilha.append('B') # Adiciona 'B' ao topo da pilha
pilha.append('C') # Adciona 'C' ao topo da pilha
print(f"Pilha: {pilha}")

elemento_pilha = pilha.pop() # Remove o último elemento (topo) da pilha
print(f"Elemento removido da pilha: {elemento_pilha}")
print(f"Pilha após remoção: {pilha}")

# Fila
from collections import deque
fila = deque()
fila.append("X") # Enfileira 'X'
fila.append("Y") # Enfileira 'Y'
fila.append("Z") # Enfileira 'Z'
print(f"\nFila: {list(fila)}")

elemento_fila = fila.popleft() # Remove o primeiro elemento da fila
print(f"Elemento removido da fila: {elemento_fila}")
print(f"Fila após remoção: {list(fila)}")