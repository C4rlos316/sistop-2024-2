# -*- coding: utf-8 -*-
"""FIFO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18M-ggUBpJKDGNXZa7l0kRsrk3RioFBLA
"""

class FIFOQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Añade un elemento al final de la cola."""
        self.queue.append(item)
        print(f"Elemento '{item}' añadido a la cola.")

    def dequeue(self):
        """Retira el primer elemento de la cola."""
        if len(self.queue) == 0:
            print("La cola está vacía, no se puede retirar un elemento.")
            return None
        return self.queue.pop(0)

    def peek(self):
        """Devuelve el primer elemento de la cola sin retirarlo."""
        if len(self.queue) == 0:
            print("La cola está vacía.")
            return None
        return self.queue[0]

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return len(self.queue) == 0

    def size(self):
        """Retorna el número de elementos en la cola."""
        return len(self.queue)

# Uso de la cola FIFO
fifo_queue = FIFOQueue()

# Añadiendo elementos
fifo_queue.enqueue("Primero")
fifo_queue.enqueue("Segundo")
fifo_queue.enqueue("Tercero")

# Viendo el primer elemento
print(f"Próximo elemento a retirar: {fifo_queue.peek()}")

# Tamaño de la cola
print(f"Tamaño de la cola: {fifo_queue.size()}")

# Retirando elementos
print(f"Elemento retirado: {fifo_queue.dequeue()}")
print(f"Elemento retirado: {fifo_queue.dequeue()}")

# Tamaño de la cola después de retirar elementos
print(f"Tamaño de la cola después de retirar elementos: {fifo_queue.size()}")

# Intentando retirar más elementos de los que hay
print(f"Elemento retirado: {fifo_queue.dequeue()}")
print(f"Intentando retirar un elemento cuando la cola está vacía: {fifo_queue.dequeue()}")