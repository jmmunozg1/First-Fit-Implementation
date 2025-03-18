#!/usr/bin/python3
import click
from cont_mem_algos import first_fit, best_fit, worst_fit

@click.command()
@click.option('--memmap', help='file with the memory description')
@click.option('--req', help='requirement file')
@click.option('--pos', help='initial position')

def print_memory_map(memory_map):
    for memory in memory_map:
        print(f"({memory[0]:#0{8}x}, {memory[1]:#0{8}x})")

def process():
    memory = [(0x06D01000, 0x00500000),
              (0x06100C00, 0x00C00000),
              (0x05200400, 0x00F00000),
              (0x04800000, 0x00A00000),
              (0x01E00000, 0x00400000),
              (0x02500000, 0x01400000),
              (0x07201800, 0x01200000),
              (0x08402C00, 0x00700000)]
    first_pos = 0

    requirements = [0x00C00000, 0x00A00000, 0x00B00000]
    work_memory = memory[:]
    cont_mem_algo = [
        {"name" : "First fit",
         "function" : first_fit },
        {"name" : "Best fit",
         "function" : best_fit },
        {"name" : "Worst fit",
         "function" : worst_fit},
    ]

    for cmae in cont_mem_algo:

        work_memory = memory[:]
        index = first_pos
        print(cmae["name"])
        print_memory_map(work_memory)
        
        for req in requirements:
            search = cmae["function"](work_memory, req, index)
            
            if search == None:
                print(f"Not found: {req:#0{8}x}")
            else:
                print(f"Assigned to the process base: {search[1]:#0{8}x} limit: {search[2]:#{8}x}")
                print(f"Index: {search[3]}")
                print_memory_map(search[0])
                index = search[3]

if __name__ == '__main__':
    process()
