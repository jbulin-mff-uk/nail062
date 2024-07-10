# NAIL062 Výroková a predikátová logika: První cvičení

Po absolvování cvičení student:

* rozumí pojmům sytaxe výrokové logiky (_jazyk_, _prvovýrok_, _výrok_, _strom výroku_, _podvýrok_, _teorie_), umí je formálně definovat a uvést příklady
* rozumí pojmům _model teorie_, _důsledek teorie_, umí je formálně definovat a uvést příklady
* umí formalizovat daný systém (slovní úlohu, výpočetní úlohu, apod.) ve výrokové logice
* umí najít modely dané výrokové teorie
* umí rozhodnout, zda je daný výrok důsledkem dané teorie
* má zkušenost s použitím (s pomocí instruktora) tablo metody a rezoluční metody k důkazu vlastností daného systému (např. k řešení slovní úlohy)

## Příklady na cvičení

### 1. příklad

Ztratili jsme se v labyrintu a před námi jsou troje dveře: červené, zelené a modré. Víme, že za právě jedněmi dveřmi je cesta ven, za ostatními je drak. Na dveřích jsou nápisy:
* Červené dveře: _``Cesta ven je za těmito dveřmi.''_
* Modré dveře: _``Cesta ven není za těmito dveřmi.''_
* Zelené dveře: _``Cesta ven není za modrými dveřmi.''_
Víme, že alespoň jeden z nápisů je pravdivý a alespoň jeden je lživý. Formalizujte naše znalosti. Určete, za kterými dveřmi je cesta ven.

#### Postup řešení:
1. Zvolte vhodný jazyk (množinu prvovýroků).
