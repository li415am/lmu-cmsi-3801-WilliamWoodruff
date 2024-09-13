from dataclasses import dataclass
from collections.abc import Callable
import math
import sys


def change(amount: int) -> dict[int, int]:
    if not isinstance(amount, int):
        raise TypeError('Amount must be an integer')
    if amount < 0:
        raise ValueError('Amount cannot be negative')
    counts, remaining = {}, amount
    for denomination in (25, 10, 5, 1):
        counts[denomination], remaining = divmod(remaining, denomination)
    return counts


# Write your first then lower case function here
def first_then_lower_case(sequence, predicate):
    for i in range(len(sequence)):
        if predicate(sequence[i]):
            return sequence[i].lower()
    return None

# Write your powers generator here
def powers_generator(base, limit):
    max_iterations = math.floor(math.log(limit) / math.log(base))
    n = 0

    while n <= max_iterations:
        yield pow(base, n)
        n += 1


# Write your say function here
def say(word = None):
   message = []

   def joiner(input = None):
       if input is None:
           return ''.join(message)
       message.append(input)
       return joiner
   
   if word is None:
       return ''.join(message)
   message.append(word)
   return joiner

# Write your line count function here
# def meaningful_line_count(file):

#     if len(sys.argv) != 2:
#         print(f'Usage: {sys.argv[0]} <filename>')
#         sys.exit(1)

#     line_number = 0
#     with open(sys.argv[1], 'r', encoding='utf-8') as file:
#         for line in file:
#             line_number += 1
#             print(f'{line_number:08}: {line.rstrip()}')


# Write your Quaternion class here
@dataclass(frozen=True)
class Quaternion:
    a: float
    b: float
    c: float
    d: float

    # def __str__(self):
    #     output = []
    #     first = False
        
    #     if self.a != 0:
    #             output.append(f"{self.a}")
    #     else: 
    #         first = True
                
    #     if self.b != 0:
    #         if self.b < 0:
    #             if abs(self.b) == 1:
    #                 output.append(f"-i")
    #             else:
    #                 output.append(f"{self.b}i")
    #         elif self.b > 0:
    #             if abs(self.b) == 1:
    #                 if first:
    #                     output.append(f"i")
    #                 else:
    #                     output.append(f"+i")
    #             else:
    #                 output.append(f"+{self.b}i")
    #     else:
    #         first = True
            
    #     if self.c != 0:
    #         if self.c < 0:
    #             if abs(self.c) == 1:
    #                 output.append(f"-j")
    #             else:
    #                 output.append(f"{self.c}j")
    #         elif self.c > 0:
    #             if abs(self.c) == 1:
    #                 if first:
    #                     output.append(f"j")
    #                 else:
    #                     output.append(f"+j")
    #             else:
    #                 output.append(f"+{self.c}j")
    #     else: 
    #         first = True
            
    #     if self.d != 0:
    #         if self.d < 0:
    #             if abs(self.d) == 1:
    #                 output.append(f"-k")
    #             else:
    #                 output.append(f"{self.d}k")
    #         elif self.d > 0:
    #             if abs(self.d) == 1:
    #                 if first:
    #                     output.append(f"k")
    #                 else:
    #                     output.append(f"+k")
    #             else:
    #                 output.append(f"+{self.d}k")
                    
    #     if (self.a == 0 and self.b == 0 and self.c == 0 and self.d == 0): # special case for <0, 0, 0, 0>
    #         output.append("0")
            
    #     return ''.join(output)

    def __str__(self):
        output = []
        first = True  # Start with first set to True
    
        if self.a != 0:
            output.append(f"{self.a}")
            first = False  # The first component has been added
    
        if self.b != 0:
            if self.b < 0:
                if abs(self.b) == 1:
                    output.append(f"-i")
                else:
                    output.append(f"{self.b}i")
            elif self.b > 0:
                if abs(self.b) == 1:
                    output.append(f"{'i' if first else '+i'}")  # Check if it's the first
                else:
                    output.append(f"{'' if first else '+'}{self.b}i")
            first = False  # Set first to False after adding the component

        if self.c != 0:
            if self.c < 0:
                if abs(self.c) == 1:
                    output.append(f"-j")
                else:
                    output.append(f"{self.c}j")
            elif self.c > 0:
                if abs(self.c) == 1:
                    output.append(f"{'j' if first else '+j'}")  # Check if it's the first
                else:
                    output.append(f"{'' if first else '+'}{self.c}j")
            first = False  # Set first to False after adding the component
    
        if self.d != 0:
            if self.d < 0:
                if abs(self.d) == 1:
                    output.append(f"-k")
                else:
                    output.append(f"{self.d}k")
            elif self.d > 0:
                if abs(self.d) == 1:
                    output.append(f"{'k' if first else '+k'}")  # Check if it's the first
                else:
                    output.append(f"{'' if first else '+'}{self.d}k")
            first = False  # Set first to False after adding the component
    
        if not output:
            output.append("0")
    
        return ''.join(output)
    
    def __add__(self, q):
        return Quaternion(self.a + q.a, self.b + q.b, self.c + q.c, self.d + q.d)
    
    def __mul__(self, q):
        a1, b1, c1, d1 = self.a, self.b, self.c, self.d
        a2, b2, c2, d2 = q.a, q.b, q.c, q.d

        a = a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2
        b = a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2
        c = a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2
        d = a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2

        return Quaternion(a, b, c, d)
    
    @property
    def coefficients(self):
        return (self.a, self.b, self.c, self.d)
    
    @property
    def conjugate(self):
        return Quaternion(self.a, -self.b, -self.c, -self.d)
    