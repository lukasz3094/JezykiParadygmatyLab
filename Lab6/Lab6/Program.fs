//[<AbstractClass>]
//type Pojazd(typPojazdu: string) =
//    member val TypPojazdu = typPojazdu with get, set    
//    abstract member Info: unit -> string

//type Samochod(typPojazdu: string, marka: string, model: string, rok: int) =
//    inherit Pojazd(typPojazdu)

//    member val Marka = marka with get, set
//    member val Model = model with get, set
//    member val Rok = rok with get, set

//    override this.Info() = $"{this.TypPojazdu}: {this.Marka} {this.Model} {this.Rok}"

//    member this.Opis() = $"{this.TypPojazdu}: {this.Marka} {this.Model} {this.Rok}"

//let samochod1 = Samochod("Samochód","Audi", "A4", 2010)

//printfn "%s" (samochod1.Opis())

//type IWydruk =
//    abstract member Drukuj: unit -> unit


//type Dokument(tresc: string) =
//    interface IWydruk with
//        member this.Drukuj() = printfn "Drukowany jest tekst z klasy Dokument %s" tresc

Zad1.main()