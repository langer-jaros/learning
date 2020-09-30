# Internetové publikování
### Javascript 
+ Od začátku unicode

? Firefox je mrtvej paralelni
WebWorkers

>- 1 Napsat přednášky
>- 2 Vybrat si zajímavou knihovnu

## Historie
- první komerční browser prodával Netscape spolu s databázema
- Sun & Netscape dohoda, přejmenováno na Java script
- na 8bitech šlo napsat všechno
- Explorer 4 -> w3c -> Explorer 5
   - in explorer 5 was too much business 
   - W couldnt brake it
- Netscape gave it opensource

# 2. přednáška
## XML a SGML 
kusu textu dáme další význam
> xml je soustava krabic se štítky

vnější krabice je jen jedna
+ html5 nedělala w3c, ale výrobci prohlížečů

vzniklo  XHTML
+ xml je case sensitive

XML nebylo nikdy pořádně nikým podporované
Kolem tisíciletí podpora XML znamenalo:
+ kořen, binární blob, uzávěr kořene

validní XML - wellformed, musí mít schéma a odpovídat mu
Bývá zvykem atributy psát se zavináčem, přišlo z xpath

### Obsah elementů a prázdné elementy
\<element />
\<element>\</element>
+ v XML se bílé znaky neignorujou!
aneb všechny bílé znaky jsou významné

+ Konec komentáře je -- nikoli -->

Předpokládá se, že základní kódování pokud není specifikované 
> \<?xml version="1.0" encoding="iso...">

+ XML není jazyk, je to meta jazyk -> pouze rada, jak psát jazyk, aby šel dobře parsovat

### Příklady použitelných jazyků postavených na XML
- SVG (program ESCAPE doporučen)
   - dom 
- XHTML striktní varianta
- MathML
   - zobrazení rovnic z textu

Python knihovna etree

### Namespaces v XML
pokud je zkombinováno více XML jazyků
> xmlns:"moje pracovní XML"
xmlns:xhtml="www.fdoajsf.xhtml"

### Schémové jazyky
+ DTD
+ XMLSchema
+ RelaxNG
+ Schematron - popisuje jak spolu jednotlive elementy souvisí
   - popisuje pomocí xpath
   - hlavní uplatnění Schematronu XSLT

### Navigace po dokumetu
+ XPath
+ DOM
+ CSS-selektory
+ SAX

na aplikace XPath musíte vytvořit DOM, což je dost velký, 
proto se může hodit SAX
SAX prochází dokument po elementech a je na nás co s tím chceme dělat.

### Vzhled a transformace dokumentu
CSS
XSL - xtensible stylesheet language

### způsob validace xml
xmlint

Clarkova notace????,

### Identifikátory
+ URI
+ URL
+ URN

RNC

# DU 1-3

### XPath
Vraci mnozinu ktera splnuje podminku

[] filtruji mnozinu, kterou vratil predchozi dotaz
> //hlavicka[2]/text()

// absolutne od pocatku

tridy:
+ text()
+ node()

musi obsahovat element - [*]

### relativni cesty
/ancestor::*

# 2. přednáška
## CSS

