module Zad2

type Tree<'a> = 
    | Empty
    | Node of 'a * Tree<'a> * Tree<'a>

let rec findRec x = function
    | Empty -> false
    | Node (y, left, right) -> 
        if x = y then true
        else findRec x left || findRec x right

let findIter x tree =
    let rec findIterHelper stack =
        match stack with
        | [] -> false
        | (Node (y, left, right))::tail -> 
            if x = y then true
            else findIterHelper (left::right::tail)
        | Empty::tail -> findIterHelper tail
    findIterHelper [tree]
