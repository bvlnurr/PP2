import pygame
import psycopg2
import random
import sys
import time

# Connect to PostgreSQL
conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="9874563210")
cur = conn.cursor()

# Create users table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE
    )
""")

# Create user_score table with five columns
cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        pause BOOLEAN
    )
""")

conn.commit()

pygame.init()

WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
COLORS = {"WHITE": (255, 255, 255), "GREEN": (0, 255, 0), "RED": (255, 0, 0), "YELLOW":(255, 255, 0)}
MOVEMENTS = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

def get_username():
    username = input("Enter your username: ")
    return username

def create_user(username):
    try:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id
    except psycopg2.Error as e:
        print("Error while creating user:", e)
        return None

def check_user(username):
    try:
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        return cur.fetchone()
    except psycopg2.Error as e:
        print("Error while checking user:", e)
        return None

def get_current_level(user_id):
    cur.execute("SELECT level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
    level = cur.fetchone()
    return level[0] if level else 1

def save_user_state(user_id, score, level, pause):
    cur.execute("INSERT INTO user_score (user_id, score, level, pause) VALUES (%s, %s, %s, %s)", (user_id, score, level, pause))
    conn.commit()

class Snake:
    def __init__(self):
        self.size = 1
        self.body = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice(list(MOVEMENTS.values()))  # Start with a random direction
        self.color = COLORS["GREEN"]
        '''self.head_color = COLORS["GREEN"]
        self.body_color = COLORS["RED"]
        self.tail_color = COLORS["YELLOW"]'''

    def head(self):
        return self.body[0]

    def move(self):
        current = self.head()
        dx, dy = self.direction
        new_position = (((current[0] + (dx * GRID_SIZE)) % WIDTH), (current[1] + (dy * GRID_SIZE)) % HEIGHT)
        # Check for collision with itself or obstacles
        if len(self.body) > 2 and new_position in self.body[2:] or any(new_position in obstacle.body for obstacle in obstacles):
            return True  # Game over if collision occurs
        else:
            self.body.insert(0, new_position)
            if len(self.body) > self.size:
                self.body.pop()
        return False

    def reset(self):
        self.size = 1
        self.body = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice(list(MOVEMENTS.values()))  # Start with a random direction
    

    def draw(self, surface):
        for part in self.body:
            rect = pygame.Rect((part[0], part[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, COLORS["WHITE"], rect, 1)


    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Change direction according to key press, but disallow opposite direction
                if event.key == pygame.K_UP and self.direction != MOVEMENTS["DOWN"]:
                    self.direction = MOVEMENTS["UP"]
                elif event.key == pygame.K_DOWN and self.direction != MOVEMENTS["UP"]:
                    self.direction = MOVEMENTS["DOWN"]
                elif event.key == pygame.K_LEFT and self.direction != MOVEMENTS["RIGHT"]:
                    self.direction = MOVEMENTS["LEFT"]
                elif event.key == pygame.K_RIGHT and self.direction != MOVEMENTS["LEFT"]:
                    self.direction = MOVEMENTS["RIGHT"]

# Food class to represent the food in the game
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = COLORS["RED"]
        self.randomize_position()  # Generate random position for the food
        self.weight = random.randint(1, 2)  # Random weight between 1 and 2
        self.creation_time = time.time()  # Time when the food is created

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, COLORS["WHITE"], rect, 1)

    def is_expired(self, duration):
        # Check if the food is expired based on the duration
        return time.time() - self.creation_time > duration

# Obstacle class to represent obstacles in the game
class Obstacle:
    def __init__(self, blocks, vertical=False):
        self.body = [(0, 0)] * blocks
        self.color = COLORS["WHITE"]
        self.vertical = vertical
        self.randomize_position()  # Generate random position for the obstacle

    def randomize_position(self):
        start = (random.randint(0, GRID_WIDTH - 2) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 2) * GRID_SIZE)
        if self.vertical:
            self.body = [(start[0], (start[1] + i * GRID_SIZE) % HEIGHT) for i in range(len(self.body))]
        else:
            self.body = [((start[0] + i * GRID_SIZE) % WIDTH, start[1]) for i in range(len(self.body))]

    def draw(self, surface):
        for pos in self.body:
            rect = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, (0, 0, 0), rect, 1)

def display_game_over_data(score, level):
    font = pygame.font.Font(None, 36)  
    game_over_text = font.render("Game Over", True, COLORS["WHITE"])  
    score_text = font.render(f"Final Score: {score}", True, COLORS["WHITE"])  
    level_text = font.render(f"Final Level: {level}", True, COLORS["WHITE"])  

    # Располагаем текст по центру экрана
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.update()

def main():
    global obstacles
    snake = Snake()
    food = Food()
    obstacles = [Obstacle(4, vertical=i%2==0) for i in range(6)] 
    score = 0
    level = 1
    game_over = False 
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)

    # Get username from user
    username = get_username()
    user = check_user(username)

    if user:
        user_id = user[0]
        current_level = get_current_level(user_id)
        print(f"Welcome back, {username}! You are currently on level {current_level}.")
    else:
        print("New user! Let's get started.")
        user_id = create_user(username)
        if user_id:
            print(f"Welcome, {username}! Let's start from level 1.")
        else:
            print("Failed to create user. Exiting...")
            pygame.quit()
            sys.exit()

    while True:
        screen.fill((0, 0, 0))  
        snake.handle_keys()  
        game_over = snake.move()  
        if game_over:
            # Display game over data
            display_game_over_data(score, level)
            
            # Save user state
            save_user_state(user_id, score, level, False) # Set pause to False

            pygame.time.wait(3000)  
            pygame.quit()  
            sys.exit()  

        if snake.head() == food.position:
            snake.size += food.weight 
            score += food.weight  
            food = Food()  
            game_over = False 

            if score % 5 == 0:
                level += 1
                obstacles.append(Obstacle(4, vertical=level%2==0))
                clock.tick(8 + level)
                snake.color = random.choice([(0,255,255), (255,255,0)]) 

        if food.is_expired(10):
            food = Food() 

        if (snake.head()[0] < 0 or snake.head()[0] >= WIDTH or
                snake.head()[1] < 0 or snake.head()[1] >= HEIGHT):
            snake.reset()
            score = 0
            level = 1
            obstacles = [Obstacle(4, vertical=i%2==0) for i in range(7)] 
            game_over = True

        if not game_over:
            snake.draw(screen) 
            food.draw(screen)  
            for obs in obstacles:
                obs.draw(screen)  

        score_text = font.render(f"Score: {score}", True, COLORS["WHITE"])
        level_text = font.render(f"Level: {level}", True, COLORS["WHITE"])
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))

        pygame.display.update()  
        clock.tick(8 + level)  

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
