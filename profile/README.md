# TrafficFlowOptimizer
## Praca inżynierska

### Title:
Application for optimizing traffic flow at crossroads by controlling traffic lights

### Tytuł:
Aplikacja do optymalizacji przepływu pojazdów na skrzyżowaniu poprzez zmiany cykli świateł ulicznych

### Opis:
Celem pracy jest stworzenie aplikacji webowej w architekturze klient-serwer, która będzie usprawniała przepływ pojazdów na skrzyżowaniu wskazanym przez użytkownika, za pomocą optymalizacji zmian cykli sygnalizacji świetlnej. Jako dane wejściowe do aplikacji zostaną użyte nagrania pobrane z kamer monitoringu, które zostaną przetworzone modelem uczenia maszynowego w celu wyekstrahowania informacji o pojazdach. Otrzymane dane przekazane zostaną do optymalizatora wykorzystującego programowaniu z ograniczeniami. Wyniki optymalizacji zostaną zaprezentowane w formie wizualizacji graficznej oraz w postaci danych liczbowych, które posłużą do walidacji i weryfikacji narzędzia.
Produktem będzie aplikacja webowa typu klient-serwer. Frontend zaimplementowany zostanie z użyciem frameworku React a backend wykorzystując framework Spring. Optymalizator będzie zaimplementowany w języku modelowania Minizinc.

### Autorzy:
- Nikodem Korohoda
- Mateusz Więcek
- Jędrzej Ziebura
- Szymon Żychowicz

## Porty:
- 8080:  Spring
- 27017: Mongo
- 9091:  Minizinc Server
- 8081:  OpenCV Server
