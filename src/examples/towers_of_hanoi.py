def towers_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        print("No disk to move")
        return

    towers_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from {from_rod} to {to_rod}")
    towers_of_hanoi(n - 1, aux_rod, to_rod, from_rod)

n = 3
towers_of_hanoi(n, 'A', 'C', 'B')
