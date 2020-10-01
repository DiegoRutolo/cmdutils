#!/usr/bin/env python3

import argparse
from random import randint

parser = argparse.ArgumentParser(description="Genera números enteros aleatorios")
parser.add_argument('int_min', metavar='MIN', type=int, nargs='?', default=0)
parser.add_argument('int_max', metavar='MAX', type=int)
parser.add_argument('-n', type=int, help='Cuántos números produce', default=1)
args = parser.parse_args()

if args.int_min > args.int_max:
    parser.error("El primer número debe ser menor")

for i in range(args.n):
    print(randint(args.int_min, args.int_max))