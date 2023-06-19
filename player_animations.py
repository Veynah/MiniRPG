import pygame

# Dictionnaire avec les animations
player_run_anim_R = [
    pygame.image.load("img/player/Player_Run_R/Player_Run_R0.png"),
    pygame.image.load("img/player/Player_Run_R/Player_Run_R1.png"),
    pygame.image.load("img/player/Player_Run_R/Player_Run_R2.png"),
    pygame.image.load("img/player/Player_Run_R/Player_Run_R3.png"),
    pygame.image.load("img/player/Player_Run_R/Player_Run_R4.png"),
    pygame.image.load("img/player/Player_Run_R/Player_Run_R5.png"),
    pygame.image.load("img/player/Player_Run_R/Player_Run_R6.png"),
    pygame.image.load("img/player/Player_Run_R/Player_Run_R7.png"),
]

player_run_anim_L = [
    pygame.image.load("img/player/Player_Run_L/Player_Run_L0.png"),
    pygame.image.load("img/player/Player_Run_L/Player_Run_L1.png"),
    pygame.image.load("img/player/Player_Run_L/Player_Run_L2.png"),
    pygame.image.load("img/player/Player_Run_L/Player_Run_L3.png"),
    pygame.image.load("img/player/Player_Run_L/Player_Run_L4.png"),
    pygame.image.load("img/player/Player_Run_L/Player_Run_L5.png"),
    pygame.image.load("img/player/Player_Run_L/Player_Run_L6.png"),
    pygame.image.load("img/player/Player_Run_L/Player_Run_L7.png"),
]

player_idle_anim_R = [
    pygame.image.load("img/player/Player_Idle_R/Player_Idle_R0.png"),
    pygame.image.load("img/player/Player_Idle_R/Player_Idle_R1.png"),
    pygame.image.load("img/player/Player_Idle_R/Player_Idle_R2.png"),
    pygame.image.load("img/player/Player_Idle_R/Player_Idle_R3.png"),
    pygame.image.load("img/player/Player_Idle_R/Player_Idle_R4.png"),
    pygame.image.load("img/player/Player_Idle_R/Player_Idle_R5.png"),
    pygame.image.load("img/player/Player_Idle_R/Player_Idle_R6.png"),
    pygame.image.load("img/player/Player_Idle_R/Player_Idle_R7.png"),
]

player_idle_anim_L = [
    pygame.image.load("img/player/Player_Idle_L/Player_Idle_L0.png"),
    pygame.image.load("img/player/Player_Idle_L/Player_Idle_L1.png"),
    pygame.image.load("img/player/Player_Idle_L/Player_Idle_L2.png"),
    pygame.image.load("img/player/Player_Idle_L/Player_Idle_L3.png"),
    pygame.image.load("img/player/Player_Idle_L/Player_Idle_L4.png"),
    pygame.image.load("img/player/Player_Idle_L/Player_Idle_L5.png"),
    pygame.image.load("img/player/Player_Idle_L/Player_Idle_L6.png"),
    pygame.image.load("img/player/Player_Idle_L/Player_Idle_L7.png"),
]

player_jump_anim_R = [
    pygame.image.load("img/player/Player_Jump_R/Player_Jump_R0.png"),
    pygame.image.load("img/player/Player_Jump_R/Player_Jump_R1.png"),
    pygame.image.load("img/player/Player_Jump_R/Player_Jump_R2.png"),
    pygame.image.load("img/player/Player_Jump_R/Player_Jump_R3.png"),
    pygame.image.load("img/player/Player_Jump_R/Player_Jump_R4.png"),
    pygame.image.load("img/player/Player_Jump_R/Player_Jump_R5.png"),
    pygame.image.load("img/player/Player_Jump_R/Player_Jump_R6.png"),
    pygame.image.load("img/player/Player_Jump_R/Player_Jump_R7.png"),
]

player_jump_anim_L = [
    pygame.image.load("img/player/Player_Jump_L/Player_Jump_L0.png"),
    pygame.image.load("img/player/Player_Jump_L/Player_Jump_L1.png"),
    pygame.image.load("img/player/Player_Jump_L/Player_Jump_L2.png"),
    pygame.image.load("img/player/Player_Jump_L/Player_Jump_L3.png"),
    pygame.image.load("img/player/Player_Jump_L/Player_Jump_L4.png"),
    pygame.image.load("img/player/Player_Jump_L/Player_Jump_L5.png"),
    pygame.image.load("img/player/Player_Jump_L/Player_Jump_L6.png"),
    pygame.image.load("img/player/Player_Jump_L/Player_Jump_L7.png"),
]

player_attack_anim_R = [
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R0.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R1.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R2.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R3.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R4.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R5.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R6.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R7.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R8.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R9.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R10.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R11.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R12.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R13.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R14.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R15.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R16.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R17.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R18.png"),
    pygame.image.load("img/player/Player_Attack_R/Player_Attack_R19.png"),
]

player_attack_anim_L = [
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L0.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L1.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L2.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L3.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L4.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L5.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L6.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L7.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L8.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L9.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L10.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L11.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L12.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L13.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L14.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L15.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L16.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L17.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L18.png"),
    pygame.image.load("img/player/Player_Attack_L/Player_Attack_L19.png"),
]
