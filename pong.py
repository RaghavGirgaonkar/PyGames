# from game import BLACK
import pygame 
import sys
import random


pygame.font.init()
FPS = 60

WIDTH, HEIGHT = 900, 500
BG_COLOR = pygame.Color('grey12')
# BLACK = pygame.Color('black')
LIGHT_GREY = (200,200,200)
SCORE_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

#Ball Characteristics

ball = pygame.Rect(WIDTH//2 -4, HEIGHT//2 - 4, 8,8)
BALL_XVEL = 6
BALL_YVEL = 6

#Define Players
player1 = pygame.Rect(WIDTH - 10, HEIGHT/2 - 40, 10,80)
player2 = pygame.Rect(0, HEIGHT/2 - 40, 10,80)

player2_speed = 5
#Paddle speed
PADDLE_VEL = 6

PLAYER1_SCORE = pygame.USEREVENT + 1
PLAYER2_SCORE = pygame.USEREVENT + 2

def ball_reset():
    global BALL_XVEL, BALL_YVEL
    ball.center = (WIDTH//2, HEIGHT//2)
    BALL_YVEL *= random.choice((-1,1))
    BALL_XVEL *= random.choice((-1,1))

def paddle_movement(keys_pressed, player):
    if keys_pressed[pygame.K_UP] and player.y  >= 0: #Left
        player.y -= PADDLE_VEL
    if keys_pressed[pygame.K_DOWN] and player.y + player.height <= HEIGHT: #Left
        player.y += PADDLE_VEL

def opponent_movement():
    if player2.top < ball.y:
        player2.top += player2_speed
    if player2.top > ball.y:
        player2.top -= player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= HEIGHT:
        player2.bottom = HEIGHT

def ball_movement():
    global BALL_XVEL, BALL_YVEL
    ball.x += BALL_XVEL
    ball.y += BALL_YVEL
    if ball.left <= 0:
        pygame.event.post(pygame.event.Event(PLAYER1_SCORE))
        ball_reset()
    if ball.right >= WIDTH:
        pygame.event.post(pygame.event.Event(PLAYER2_SCORE))
        ball_reset()
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_YVEL *= -1
    if ball.colliderect(player1) or ball.colliderect(player2):
        BALL_XVEL *= -1
    

def draw_window(player1_score, player2_score):
    WIN.fill(BG_COLOR)
    player1_score_text = SCORE_FONT.render("Score: "+ str(player1_score),1 , LIGHT_GREY)
    player2_score_text = SCORE_FONT.render("Score: "+ str(player2_score),1 , LIGHT_GREY)
    WIN.blit(player1_score_text, (WIDTH - player1_score_text.get_width() - 10, 10))
    WIN.blit(player2_score_text, (10, 10))
    pygame.draw.rect(WIN, LIGHT_GREY, player1)
    pygame.draw.rect(WIN, LIGHT_GREY, player2)
    pygame.draw.ellipse(WIN, LIGHT_GREY, ball)
    pygame.draw.aaline(WIN, LIGHT_GREY, (WIDTH/2, 0),(WIDTH/2, HEIGHT))
    pygame.display.update()

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, LIGHT_GREY)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def draw_new_game():
    WIN.fill(BG_COLOR)
    pygame.display.update()
    text = "New Game: First to 10 wins"
    newgame_text = WINNER_FONT.render(text, 1, LIGHT_GREY)
    WIN.blit(newgame_text, (WIDTH//2 - newgame_text.get_width()/2, HEIGHT/2 - newgame_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)
    WIN.fill(BG_COLOR)
    pygame.display.update()
    draw_text = "Ready?"
    newgame_text = WINNER_FONT.render(draw_text, 1, LIGHT_GREY)
    WIN.blit(newgame_text, (WIDTH//2 - newgame_text.get_width()/2, HEIGHT/2 - newgame_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)
    WIN.fill(BG_COLOR)
    pygame.display.update()
    draw_text = "3"
    newgame_text = WINNER_FONT.render(draw_text, 1, LIGHT_GREY)
    WIN.blit(newgame_text, (WIDTH//2 - newgame_text.get_width()/2, HEIGHT/2 - newgame_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)
    WIN.fill(BG_COLOR)
    pygame.display.update()
    draw_text = "2"
    newgame_text = WINNER_FONT.render(draw_text, 1, LIGHT_GREY)
    WIN.blit(newgame_text, (WIDTH//2 - newgame_text.get_width()/2, HEIGHT/2 - newgame_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)
    WIN.fill(BG_COLOR)
    pygame.display.update()
    draw_text = "1"
    newgame_text = WINNER_FONT.render(draw_text, 1, LIGHT_GREY)
    WIN.blit(newgame_text, (WIDTH//2 - newgame_text.get_width()/2, HEIGHT/2 - newgame_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)
    WIN.fill(BG_COLOR)
    pygame.display.update()
    draw_text = "Begin!"
    newgame_text = WINNER_FONT.render(draw_text, 1, LIGHT_GREY)
    WIN.blit(newgame_text, (WIDTH//2 - newgame_text.get_width()/2, HEIGHT/2 - newgame_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)


def main():
    draw_new_game()
    player1_score = 0
    player2_score = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                # sys.quit()
            if event.type == PLAYER2_SCORE:
                player2_score += 1
                if player2_score == 10:
                    winner_text = "Opponent Wins!"
                    draw_winner(winner_text)
                    run = False
                    break
            if event.type == PLAYER1_SCORE:
                player1_score += 1
                if player1_score == 10:
                    winner_text = "You Win!"
                    draw_winner(winner_text)
                    run = False
                    break
        
        keys_pressed = pygame.key.get_pressed()

        ball_movement()        
        paddle_movement(keys_pressed, player1)
        opponent_movement()
        draw_window(player1_score, player2_score)
    
    main()

if __name__ == "__main__":
    main()