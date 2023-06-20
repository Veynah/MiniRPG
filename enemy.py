import pygame
from pygame.math import Vector2 as vec
import random
from monster_animations import (
    skeleton1_walking_L,
    skeleton1_walking_R,
    skeleton1_attacking_L,
    skeleton1_attacking_R,
)

# Le même principe que pour player
ACC = 0.06
FRIC = -0.1


# Classe enemy dont vont hériter les différents monstres
class Enemy(pygame.sprite.Sprite):
    ATTACK_COOLDOWN = 3000

    def __init__(self, x, y, walls, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # Physique et collision et mouvement
        self.vx = 0
        self.walls = walls
        self.position = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "LEFT"
        self.running = False
        self.attacking = False
        self.enemy_take_damage = False

        # Stats
        self.health = 5

        # Animation
        self.attack_frame = 0
        self.frame_index = 0
        self.time_since_last_frame = 0
        self.frame_duration = 40
        self.player_in_attack_range = False

        # Cooldown pour les attaques sur le joueur
        self.last_attack_time = 0
        
        # Cooldown pour recevoir des dégâts
        self.last_attack_counter = -1
        self.last_damage_time = 0
        self.damage_cooldown = 100

        self.patrol_direction = random.choice([-1, 1])
        self.patrol_time = pygame.time.get_ticks()
        self.patrol_duration = random.randint(2000, 5000)

    # Update l'enemie, sa position et son comportement
    def update_enemy(self, player):
        self.acc = vec(0, 0.5)

        # Running = faux si on est trop slow
        if abs(self.vel.x) > 0.01:
            self.running = True
        else:
            self.running = False

        # Comportement du monstre
        if self.see_player(player):
            self.chase_player(player)
            # print(self.running) debug
            # print(self.direction)
            if self.close_to_player(player):
                self.attack_player(player)
        else:
            self.patrol()

        # Donne sa position
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc

        self.position.x += self.vel.x
        self.position.y += self.vel.y
        self.rect.y = self.position.y
        self.rect.x = self.position.x

        # Vérifie s'il entre en collision avec walls
        self.collision_check()

        self.rect.topleft = self.position

    # Donne la distance à laquelle le monstre voit le joueur
    def see_player(self, player):
        sight_range = 300

        dx = self.position.x - player.position.x
        dy = self.position.y - player.position.y
        distance = (dx**2 + dy**2) ** 0.5
        return distance <= sight_range

    # Le monstre bouge vers le joueur
    def chase_player(self, player):
        if self.position.x < player.position.x:
            self.acc.x = ACC
            self.direction = "RIGHT"
        else:
            self.acc.x = -ACC
            self.direction = "LEFT"
        self.running = True

    # Donne la distance à laquelle le monstre peut attaquer le joueur
    def close_to_player(self, player):
        distance_x = abs(self.rect.x - player.rect.x)
        attack_range = 70
        if distance_x <= attack_range:
            self.player_in_attack_range = True
        return self.player_in_attack_range

    # Attaque le joueur avec un cooldown pour ne pas spamme
    def attack_player(self, player):
        current_time = pygame.time.get_ticks()
        if (
            self.close_to_player(player)
            and current_time - self.last_attack_time > self.ATTACK_COOLDOWN
        ):
            self.attacking = True
            print("Im attacking you")
            self.last_attack_time = current_time
        else:
            self.attacking = False
            self.player_in_attack_range = False

    # Donne le comportement du monstre si le joueur n'est pas dans le coin
    def patrol(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.patrol_time > self.patrol_duration:
            self.patrol_direction *= -1
            self.patrol_time = current_time
            self.patrol_duration = random.randint(2000, 5000)

        self.acc.x = ACC * self.patrol_direction
        self.running = True

        if self.patrol_direction > 0:
            self.direction = "RIGHT"
        else:
            self.direction = "LEFT"

    # La meme (presque) fonction que player, on enlève juste le jump
    def collision_check(self):
        move_by = int(self.vel.x)
        for _ in range(abs(move_by)):
            # Increment or decrement x position by 1 pixel
            if move_by > 0:
                self.position.x += 1
            else:
                self.position.x -= 1
            # Update le rectangle
            self.rect.x = self.position.x
            # Check pour les collisions
            collisions = pygame.sprite.spritecollide(self, self.walls, False)
            if collisions:
                # Si je bouge vers la droite ajuste ma position à 1 pixel à gauche du mur
                if move_by > 0:
                    self.position.x = collisions[0].rect.left - self.rect.width - 3
                # Si je bouge vers la gauche ajuste ma position à 1 pixel à droite du mur
                elif move_by < 0:
                    self.position.x = collisions[0].rect.right + 3
                # Stop any horizontal movement
                self.vel.x = 0
                break

        collisions = pygame.sprite.spritecollide(self, self.walls, False)
        if collisions:
            # Détecet si le joueur bouge vers le bas
            if self.vel.y > 0:
                # Personnage bouge vers le bas
                for wall in collisions:
                    # Place le joueur sur le mur
                    self.position.y = wall.rect.top - self.rect.height
                    # Stoppe la chute verticale
                    self.vel.y = 0
            # Détecte si le personnage saute
            elif self.vel.y < 0:
                # Saut
                for wall in collisions:
                    # Place le joueur sous le mur
                    self.position.y = wall.rect.bottom
                    # Stop mouvement vers le haut
                    self.vel.y = 0

    def take_damage(self, damage_amount, attack_counter):
        if attack_counter != self.last_attack_counter:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_damage_time > self.damage_cooldown:
                self.health -= damage_amount
                self.last_damage_time = current_time
                print("HP: " + str(self.health))
                self.last_attack_counter = attack_counter
                if self.health <= 0:
                    self.die()

    def die(self):
        self.kill()


class Skeleton1(Enemy):
    def __init__(self, x, y, walls):
        super().__init__(
            x, y, walls, "img/enemies/skeleton1/Skeleton1_Walk_L/Skeleton1_Walk_L0.png"
        )
        self.running_animation_L = skeleton1_walking_L
        self.running_animation_R = skeleton1_walking_R
        self.attacking_animation_L = skeleton1_attacking_L
        self.attacking_animation_R = skeleton1_attacking_R
        self.frame_index = 0
        self.attack_frame = 0
        self.time_since_last_frame = 0
        self.frame_duration = 100

    def attack_player(self, player):
        current_time = pygame.time.get_ticks()
        if (
            self.close_to_player(player)
            and current_time - self.last_attack_time > self.ATTACK_COOLDOWN
            and not self.attacking
        ):
            self.attacking = True
            self.attack_frame = 0
            print("Im attacking you")
            self.last_attack_time = current_time

    def update_enemy(self, player):
        super().update_enemy(player)
        self.update_animation()

    def update_animation(self):
        time_passed = (
            pygame.time.get_ticks() - self.time_since_last_frame
        )  # Pour que les animations soient plus smooth, elles vont charger moins vite
        if time_passed > self.frame_duration:
            self.time_since_last_frame = pygame.time.get_ticks()

            if (
                self.frame_index > 5
            ):  # Comme nous avons 8 images pour les animations, ceci nous permet de revenir à l'image 0
                self.frame_index = 0
                return

            if self.attacking:
                if self.direction == "LEFT":
                    self.image = self.attacking_animation_L[self.attack_frame]
                elif self.direction == "RIGHT":
                    self.image = pygame.transform.flip(
                        self.attacking_animation_L[self.attack_frame], True, False
                    )
                self.attack_frame += 1
                if self.attack_frame > 18:
                    self.attack_frame = 0
                    self.attacking = False
            else:
                if self.running and self.direction == "LEFT":
                    self.image = self.running_animation_L[self.frame_index]
                elif self.running and self.direction == "RIGHT":
                    self.image = pygame.transform.flip(
                        self.running_animation_L[self.frame_index], True, False
                    )
                self.frame_index += 1
            self.mask = pygame.mask.from_surface(self.image)
