# GauchoDefense

![Captura de juego](assets/screenshots/gameplay.png) <!-- Agrega una captura real después -->

Juego de acción 2D ambientado en la Argentina del siglo XIX, despues de la Guerra Gaucha, donde defendés tu hogar contra soldados realistas.

## Características principales

- Combate con desplazamiento lateral
- Ambientación histórico y de ciencia-ficcion
- Enemigos realistas zombificados
- Sistema de puntuación y ranking
- Sprites y efectos animados
- Musica y efectos de sonido


## Requisitos

- Python 3.8+
- Pygame 2.0+
- gif_pygame (para animaciones)


## Instalación

1. Clonar el repositorio:
    git clone https://github.com/Amparo221/GauchoDefense.git
   cd gaucho-defense

2. Ejecutar el juego:
    python main.py


## Controles

- W	     Moverse arriba
- S	     Moverse abajo
- ESPACIO	 Disparar
- ESC	     Saltar introducción/Pausa


## Estructura del proyecto

/gaucho-defense
├── assets/               
│   ├── fonts/
│   │   └── Jersey10-Regular.ttf            
│   ├── images/ 
│   │   ├── caminar.gif          
│   │   ├── disparo.gif 
│   │   ├── fondo_juego_2.png
│   │   ├── render.py     
│   │   ├── fondo_juego.png
│   │   ├── gaucho.png  
│   │   ├── sprite_zombie.gif
│   │   ├── vidas.png       
│   │   └── zombie_muerto.png          
│   ├── music/
│   │   ├── gameplay_music.wav  
│   │   ├── musica_juego_PorMilonga.mp3
│   │   ├── musica_menu_milonga.mp3       
│   │   └── musica_western_1.wav           
│   ├── sounds/
│   │   ├── disparo_western_1.wav     
│   │   ├── disparo_western_2.wav
│   │   ├── game_over_1.wav  
│   │   ├── game_over_2.wav
│   │   ├── hurt_gaucho.ogg       
│   │   └── zombie_hit.wav           
│   └── assets.py         
├── data/                 
│   └── ranking.json
├── entities/             
│   ├── enemigos.py
│   └── jugador.py
├── game/                 
│   ├── audio.py          
│   ├── ejecutar_juego.py 
│   ├── input_handler.py
│   ├── render.py     
│   ├── state.py
│   ├── update.py          
│   └── utils.py               
├── ui/                   
│   ├── intro.py       
│   ├── ranking.py          
│   └── renderer.py               
├── config.py             
├── main.py
├── menu.py               
└── README.md             

## Creditos
- Desarrollo de anemigos y fondos dinamicos: Paula Ortega
- Implementacion de personaje jugable e introduccion: Amparo Moreno
- Creacion del menu, organizacion y optimizacion de modulos: Leon Puddini
