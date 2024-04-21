# Arkkitehtuurikuvaus

## Pelilogiikka
Aluksi ohjelma luo App-luokan, joka alustaa ohjelman ja aloitta pelisilmukan.
Pelin logiikka tapahtuu Game-luokassa, jota päivitetään App-luokasta kutsumalla funktioita tick(), draw() ja handle_input().
Game-luokan tick() funktio päivittää palikoita, pitää niistä listaa ja tarkastaa täydet rivit.
Tetromino-luokka on yksittäisistä paloista (Block-luokka) koostuva palikka, ja sitä voi ohjata kutsumalla funktioita move() ja rotate().


```mermaid
classDiagram

App  "1"  --  "1"  Game
Tetromino  "*"  --  "*"  Block
Game  "1"  --  "*"  Tetromino

class  App{
start()
process_events()
tick()
draw()
}

class  Game{
tick(dt)
draw()
handle_input()
}

class  Tetromino{
move()
rotate()
}

class  Block{
update()
move()
rotate()
}
```

Pelisilmukan toiminta sekvenssikaaviona
```mermaid
sequenceDiagram
    participant main
    participant game
    participant tetromino
    participant block
    main->>game: Game()
    game->>tetromino: Tetromino()
    tetromino->>block: Block()
    main->>game: process_events()
    main->>game: tick()
    game->>tetromino: move()
    tetromino->>block: move()
    main->>game: draw()
```