module Zad1

type Book(tytul: string, autor: string, liczbaStron: int) =
    member val Tytul = tytul with get, set
    member val Autor = autor with get, set
    member val LiczbaStron = liczbaStron with get, set

    member this.GetInfo() = $"{this.Tytul} {this.Autor} {this.LiczbaStron}"

type User(imie: string, nazwisko: string) =
    let mutable borrowedBooks = []
    member this.BorrowedBooks = borrowedBooks

    member val Imie = imie with get, set
    member val Nazwisko = nazwisko with get, set

    member this.BorrowBook(book: Book) = 
        borrowedBooks <- book :: borrowedBooks
        printfn "Użytkownik %s %s wypożyczył książkę %s" this.Imie this.Nazwisko (book.GetInfo())

    member this.ReturnBook(book: Book) = 
        borrowedBooks <- List.filter (fun b -> b <> book) borrowedBooks
        printfn "Użytkownik %s %s zwrócił książkę %s" this.Imie this.Nazwisko (book.GetInfo())

type Library(users: List<User>) =
    let mutable books = []
    let mutable users = users

    member val Books = books with get, set
    member val Users = users with get, set

    member this.AddBook(book: Book) = this.Books <- book :: this.Books
    member this.RemoveBook(book: Book) =  this.Books <- List.filter (fun b -> b <> book)  this.Books
   
    member this.GetBorrowedBooks() = this.Users |> List.collect (fun (u: User) -> u.BorrowedBooks)
    member this.ListBooks() = this.Books |> List.iter (fun b -> printfn "%s" (b.GetInfo()))
    member this.ListBorrowedBooks() = this.GetBorrowedBooks() |> List.iter (fun b -> printfn "%s" (b.GetInfo()))
    member this.ListAvailableBooks() = this.Books |> List.filter (fun b -> 
        not (this.GetBorrowedBooks() |> List.exists (fun bb -> bb = b))) |> List.iter (fun b -> printfn "%s" (b.GetInfo()))

let main() =
    let user = User("Jan", "Kowalski")
    let library = Library([user])

    let book1 = Book("Wiedźmin", "Andrzej Sapkowski", 300)
    let book2 = Book("Harry Potter", "J.K. Rowling", 400)
    let book3 = Book("Hobbit", "J.R.R. Tolkien", 350)

    library.AddBook(book1)
    library.AddBook(book2)
    library.AddBook(book3)

    printfn "Lista książek:\n"
    library.ListBooks()

    printfn ""

    user.BorrowBook(book1)
    user.BorrowBook(book2)

    user.ReturnBook(book1)

    printfn "\n---Lista wypożyczonych książek---\n"
    library.ListBorrowedBooks()
    printfn "\n---Lista dostępnych książek---\n"
    library.ListAvailableBooks()
