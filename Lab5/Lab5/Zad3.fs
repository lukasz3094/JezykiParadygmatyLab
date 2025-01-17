module Zad3

let rec permutations list =
    match list with
    | [] -> [[]]
    | _ -> 
        list |> List.collect (fun x -> 
            permutations (List.filter (fun y -> y <> x) list) |> List.map (fun y -> x::y)
        )
