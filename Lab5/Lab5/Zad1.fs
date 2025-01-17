module Zad1

let rec fib n =
    if n = 0 then 0
    elif n = 1 then 1
    else fib (n-1) + fib (n-2)

let fibTail n =
    let rec fibTailHelper n a b =
        if n = 0 then a
        elif n = 1 then b
        else fibTailHelper (n-1) b (a+b)
    fibTailHelper n 0 1
