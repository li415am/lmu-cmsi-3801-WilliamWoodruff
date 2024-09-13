import { open } from "node:fs/promises"

export function change(amount) {
  if (!Number.isInteger(amount)) {
    throw new TypeError("Amount must be an integer")
  }
  if (amount < 0) {
    throw new RangeError("Amount cannot be negative")
  }
  let [counts, remaining] = [{}, amount]
  for (const denomination of [25, 10, 5, 1]) {
    counts[denomination] = Math.floor(remaining / denomination)
    remaining %= denomination
  }
  return counts
}

// Write your first then lower case function here
export function firstThenLowerCase(sequence, predicate) {
  for (let i = 0; i < sequence.length; i++) {
    if (predicate(sequence[i])) {   // does a satisfy p?
      return sequence[i]?.toLowerCase(); // if it does, make it lowercase and return a[i]. ?. returns undefined for unexpected cases
    }
  }
}

// Write your powers generator here
export function* powersGenerator({ofBase: base, upTo: limit}) { // define function as generator function w/ *
  const maxIterations = Math.floor(Math.log(limit) / Math.log(base)); // lil algebra to determine our limit
  let n = 0;

  while (n <= maxIterations) { // recursion to get our powahs
    const value = Math.pow(base, n);
    yield value; // use yield rather than return
    n += 1;
  }
}

// Write your say function here
export function say(word) {
  const message = []; // initialize output array

  function joiner(input) { // chain function 
    if (input === undefined) {
      return message.join(' '); // for no words/final case
    }
    message.push(input);
    return joiner;
  }
  
  if (word === undefined) {
    return message.join(' ');
  }

  message.push(word);
  return joiner;
}


// Write your line count function here

// const fs = require('fs');
// const readline = require('readline');

// export function meaningfulLineCount(file) {
//   new Promise((resolve, reject) => {

    
//   }

// }

// Write your Quaternion class here

class Quaternion {
  constructor (i, k, j) {
    this.i = i;
    this.j = j;
    this.k = k;
    this.x = x;
  }
  toString() {
    return '<$this.i'

}

}


