# NS Consumentenzuil
HU_miniproject

Dit is onze eerste miniproject van de opleiding HBO-ICT in Utrecht. We  hebben een samen een programma geschreven waarmee we tweets kunnen uitzenden naar twitter, en deze tweets weer kunnen weergeven via de GUI. 

Het programma bestaat uit 3 hoofdonderdelen:

    •	de backend: Backend_Consuemntenzuil;
    •	de front-end: GUI_consumentenzuil;
    •	De twitter Api: Twitter_API.
    
Om tweets te versturen moet de eerst in Backend_Consuemntenzuil: input_van_consument.py uitvoeren en een tweet als input schrijven in de terminal. Maar de tweet wordt niet direct verzonden. Deze moet eerst worden goedgekeurd in Backend_Consuemntenzuil: accept_reject.py.
Deze moet je dan eerst uitvoeren, accepteren of afwijzen. Als je de tweet accepteert, wordt deze vervolgens naar twitter verzonden, en vertoond.
In de front-end kunnen de tweets worden weergegeven door in GUI_consumentenzuil:  uit te voeren. Deze geeft met Tkinter een vormgeving aan de data die vanuit de twitter_APi: Request_Response_Tweets.py
 via fetch_tweets() wordt gehaald.a



Voordat het programma werkt moet eerst de TwitterAPI en Onauth2 geinstalleerd worden.
Hiervoor ga je naar je Command Prompt en typ je in: pip install TwitterAPI, pip install Onauth2.
Als hij zegt dat "pip" niet werkt, moet eerst pip worden geinstalleerd. 
Dit doe je door dit bestand te downloaden: https://bootstrap.pypa.io/get-pip.py
Als dit bestand is gedownload in je downloads map ga je naar Commands Prompt
Hier typ je in: CD Downloads
Nu zit je in je downloads map.
Dan typ je in: python get-pip.py
Nu wordt er iets uitgevoerd in je Commands Prompt en wordt pip geinstalleerd.
Als pip is geinstalleerd typ je: pip install TwitterAPI.
Nu is de TwitterAPI geinstalleerd en kan het programma gerund worden.
