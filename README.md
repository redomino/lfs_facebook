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
