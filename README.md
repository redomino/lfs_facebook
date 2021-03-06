What is it?
====================
It is a package for lfs e-commerce.....

Features
=============
* Protegge alcune viste con un decoratore "permissions_required" (definito in decorators.py) che si basa sul "login_required". 
Nel dettaglio "permissions_required" cicla su un dizionario di variabili booleane, che rappresentano una vista, 
e se la variabile relativa alla vista protetta da decoratore è settata a True, chiama login_required.
Le variabili rappresentanti le viste devono essere raggrupate in un dizionario chiamato VIEW_WITH_LOGIN_REQUIRED 
dichiarato nel file di settings. 
Example:
```
VIEW_WITH_LOGIN_REQUIRED = {
    #'view name': boolean value
    'add-to-cart': True,#
    'shop': False,
    'category': False,
    'product': True,
    'checkout': False,
}
```

* introduce un nuovo modello per lo user, in modo che per personalizzare le info per lo user  basterà modificare 
i campi in "LfsFbUser" del models.py di questo pacchetto e aggiungere ai settings `AUTH_PROFILE_MODULE = 'lfs_facebook.LfsFbUser'`

* fornisce una pagina di login (lfs_facebook/login.html) in modo da usare come backend quello di facebook 

* è disabilitato il pulsante di login(lfs/user_actions.html), in quanto l'utente sarà rediretto alla pagina di login solo quando necessario, cioè se la vista ha "permission_required"

* fornisce la possibilità di riservare un prodotto solo agli utenti a cui piace la propria facebook page.
Per far questo deve essere aggiunta una proprietà lfs al prodotto che si vuole riservare. Va bene qualsiasi proprietà basta
che abbia come titolo "Facebook Fan Reserved". Attraverso la patch della vista "product_inline" si controlla se il 
prodotto è riservato e poi in lfs/catalog/product_base.html si decide o meno se permettere l'acquisto

With lfs_facebook you can make a product available for facebook fans only.

   To set this feature to a product you add a lfs property(of whatever type you want) 
   with title: "Facebook Fan Reserved". So if a user doesn't like your Facebook page, he can't
   add to cart the specific product. 

* modificata la pagina di login-checkout in modo da permettere autenticazione con facebook o procedere
  con l'aquisto da anonimo

* traduzione di alcune parti di testo in italiano attraverso il sistema di internazionalizzazione di django
