import pygame
from pygame.locals import *
from rt import Raytracer
from figuras import *
from materiales import *
from luces import *


width = 500
height = 500

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)
raytracer = Raytracer(screen)
raytracer.rtClearColor(0.0, 0.0, 1.0) 
nieve = Material(diffuse=(1, 1, 1), spec=16)
carbon = Material(diffuse=(0, 0, 0), spec=4)
zanahoria = Material(diffuse=(1, 0.65, 0), spec=64)

raytracer.scene.append(Sphere(position=(0,-1.5,-5), radius = 1, material=nieve))
raytracer.scene.append(Sphere(position=(0,0,-5), radius = 0.9, material=nieve))
raytracer.scene.append(Sphere(position=(0,1.5,-5), radius = 0.8, material=nieve))
button_radius = 0.15  # Tamaño de los botones
torso_y_start = 0.5  # Posición inicial para los botones del torso
torso_button_spacing = 0.4  # Espacio entre los botones del torso
button_radius = 0.15  # Tamaño de los botones
# Primer botón del torso
raytracer.scene.append(Sphere(position=(0, 0.3, -5), radius=button_radius, material=carbon))
# Segundo botón del torso
raytracer.scene.append(Sphere(position=(0, -0.5, -5), radius=button_radius, material=carbon))
# Botón para la base
raytracer.scene.append(Sphere(position=(0, -1.5, -5), radius=button_radius, material=carbon))
eye_radius = 0.25  # Dimensión para la parte blanca de los ojos.
pupil_radius = 0.1  # Dimensión para las pupilas.
eye_y_position = 1.7
eye_x_offset = 0.3
raytracer.scene.append(Sphere(position=(-eye_x_offset, eye_y_position, -5.2), radius=eye_radius, material=nieve))
raytracer.scene.append(Sphere(position=(-eye_x_offset, eye_y_position, -5.1), radius=pupil_radius, material=carbon))
raytracer.scene.append(Sphere(position=(eye_x_offset, eye_y_position, -5.2), radius=eye_radius, material=nieve))
raytracer.scene.append(Sphere(position=(eye_x_offset, eye_y_position, -5.1), radius=pupil_radius, material=carbon))

raytracer.scene.append(Sphere(position=(-0.25, 1.05, -5.2), radius=0.05, material=carbon))
raytracer.scene.append(Sphere(position=(-0.1, 1.0, -5.15), radius=0.05, material=carbon))
raytracer.scene.append(Sphere(position=(0.1, 1.0, -5.15), radius=0.05, material=carbon))
raytracer.scene.append(Sphere(position=(0.25, 1.05, -5.2), radius=0.05, material=carbon))
raytracer.scene.append(Sphere(position=(0,1.3,-5), radius = 0.2, material=zanahoria))
raytracer.lights.append(AmbientLight(intensity = 0.1))
raytracer.lights.append(DirectionalLight(direction=(-0.8, 0, -0.6), intensity = 0.6))




isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.KEY == pygame.K_ESCAPE:
                isRunning == False  
    raytracer.rtClear()
    raytracer.rtRender()    
    pygame.display.flip()
pygame.quit()