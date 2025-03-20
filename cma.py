#!/usr/bin/python3
import click
from cont_mem_algos import first_fit, best_fit, worst_fit

def print_memory_map(memory_map):
    for memory in memory_map:
        print(f"({memory[0]:#0{8}x}, {memory[1]:#0{8}x})")

def read_reqs_file(reqs_filename):
    result = []
    try:
        with open(reqs_filename, 'r') as reqsfile:
            for line in reqsfile:
                req = int(line.strip(),16)
                result.append(req)
    except FileNotFoundError:
        print(f'File not found {reqs_filename}', file=sys.stderr)
        return None
    else:
        return result

def read_memmap_file(memmap_filename):
    result = []
    try:
        with open(memmap_filename, 'r') as mmfile:
            for line in mmfile:
                elems = line.strip().split()
                result.append((int(elems[0],16), int(elems[1],16)))
    except FileNotFoundError:
        print(f'File not found {memmap_filename}', file=sys.stderr)
        return None
    else:
        return result

def cmas(algo_str):
    if algo_str == 'all':
        return [
            {"name" : "First fit",
             "function" : first_fit },
            {"name" : "Best fit",
             "function" : best_fit },
            {"name" : "Worst fit",
             "function" : worst_fit},
        ]
    elif algo_str == 'first':
        return [
            {"name" : "First fit",
             "function" : first_fit },
        ]
    elif algo_str == 'best':
        return [
            {"name" : "Best fit",
             "function" : best_fit },
        ]
    elif algo_str == 'worst':
        return [
            {"name" : "First fit",
             "function" : first_fit },
            {"name" : "Best fit",
             "function" : best_fit },
            {"name" : "Worst fit",
             "function" : worst_fit},
        ]
    else:
        return None

@click.command()
@click.option('--memmap', help='file with the memory description')
@click.option('--reqs', help='requirement file')
@click.option('--function', default='all', help='Algorithm to Execute: first, best, worst, all')
@click.option('--pos', default=0, help='initial position')
def process(memmap, reqs, function, pos):
    memory = read_memmap_file(memmap)
    requirements = read_reqs_file(reqs)
    cont_mem_algo = cmas(function)
    if memory == None or requirements == None or cont_mem_algo == None:
        return

    first_pos = pos
    
    work_memory = memory[:]

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
