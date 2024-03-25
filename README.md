# Splendor

Gra cyfrowa stworzona w oparciu o grę planszową Splendor pod tym samym tytułem.

## General information

Gra umożliwia rozgrywkę taką samą jak ma to miejsce w oryginalnej grze planszowej.
Wybieramy liczbe graczy, podajemy imiona i możemy przystąpić do rywalizacji.
Aktualnie gra pozwala na lokalną rywalizację, ale jest plan, aby rozbudować ją o możliwość grania w sieci.
W grze mamy mozliwośc prowadzenia statystyk graczy. Po każdej rozegranej grze aktualizowane są
statystyki dla każdego gracza. Gra będzie poprawiana i rozbudowywana o nowe funkcjonalności.

## Installation and running
Po sklonowaniu repozytorium należy zainstalować zależności:

    pip install -r requirements.txt 

, które pozwola na poprawne uruchomienie skryptu.
W celu uruchomienia gry należy uruchomieć plik main.py

Do prowadzenia statystyk wymagane jest zainstalowanie bazy danych Postgresql.

## Technologies
Główne technologie wykorzystane do opracowania gry:
* Python
* Postgresql
* Pygame

## Game description with examples
### Main view
Po uruchomieniu pliku main.py pojawi się okienko z widokiem głównym (pic.1), w którym można wybrać jedną z trzech opcji:
* Game - przejście do widoku z dodawaniem graczy
* Statistics - widok statystyk graczy
* Quit - wyjście z gry


![](github_img/1_main_view.png )
<p align="left">
    pic.1 Main view
</p>

### Add players
W widoku dodawania graczy należy wybrać liczbę graczy od 2 do 4 i podać ich imiona zatwierdzając je przyciskiem "ENTER".
Po podaniu wszystkich imion zostanie wykonane przejście do kolejnego widoku.
![](github_img/2_add_players.png )
<p align="left">
    pic.2 Add players
</p>

### Added players
Przed rozpoczęciem gry zostaje wyświetlona lista graczy biorących udział w grze, aby rozpocząć grę należy przycisnąć "START GAME"
![](github_img/3_added_players.png )
<p align="left">
    pic.3 Added players
</p>

### Game table
Po przyciśniuęciu przycisku "Start Game" w poprzednim widoku następuje przygotowanie gry, tzn. karty zostają przetasowane i wyłożone na stół oraz 
ilość kart arystokratów i znaczników jest wyłożona w zależności od ilości graczy.
Stół zawiera:
* obszar graczy (imię, punkty, znaczniki, karty rozwoju, zarezerwowane karty rozwoju, ilość kart arystokratów)
* obszar kart rozwoju
* obszar znaczników
* obszar kart arystokratów
* obszar przycisków akcji (weź 3 znaczniki różnego kolory, weź 2 znaczniki tego samego koloru, kup kartę, zarezerwuj kartę)
* przycisk wyjścia z gry

W celu wykonania akcji należy wybrać i przycisnąc przycisk tak by zmienił kolor na żółty a nastepnie wykonać akcje.

### Prepared game table
![](github_img/4_clean_table.png )
<p align="left">
    pic.4 Prepared game table
</p>

### Finishing round and game

![](github_img/7_finishing_round_and_game.png )
<p align="left">
    pic.7 Finishing round and game
</p>


### Results
Po zakończeniu rozgrywki pojawia się ekran z tabela wyników, w który możeby wrócić do ekranu startowego lub rozpocząć kolejną grę z podanymi wcześniej graczami
![](github_img/8_results.png )
<p align="left">
    pic.8 Results view
</p>


### Statistics
W statystykach mamy możliwość sprawdzenia najlepszej 10tki graczy. Można tutaj sprawdzić podstawowe dane takie jak:
*  ilość zdobytych punktów
*  ilośc rozegranych gier
*  ilość zakupionych kart
*  ilość przyjętychy arystokratów
*  czas ostatniej rozegranej gry przez gracza

Mamy do dyspozycji przycisk reset w celu zresetowania statystyk.
![](github_img/9_statistics.png )
<p align="left">
    pic.9 Statistics view
</p>

## What's next?
W przyszłości chciałbym rozbudować grę o możliwość gry on-line.
Kod wymaga refaktoryzacji oraz pokrycia większa ilością testów.

