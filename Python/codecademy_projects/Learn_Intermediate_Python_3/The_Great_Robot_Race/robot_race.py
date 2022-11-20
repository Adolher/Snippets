import robot_race_functions as rr
from collections import deque, Counter, namedtuple
from time import time, sleep

maze_file_name = "maze_data_2.csv"
seconds_between_turns = 0.3
max_turns = 35

maze_data = rr.read_maze(maze_file_name)
rr.print_maze(maze_data)
walls, goal, bots = rr.process_maze_init(maze_data)

robot_moves = deque()
num_of_turns = 0
while not rr.is_race_over(bots) and num_of_turns < max_turns:
    for bot in bots:
        if not bot.has_finished:
            robot_moves.append(rr.compute_robot_logic(walls, goal, bot))
    num_of_turns += 1

count_moves = Counter(move[0] for move in robot_moves)
print(count_moves)

count_collisions = Counter(move[0] for move in robot_moves if move[2])
print(count_collisions)

BotScoreData = namedtuple("BotScoreData", "name num_moves num_collisions score")

bot_scores = []
for bot in bots:
    score = count_moves[bot.name] + count_collisions[bot.name]
    bot_scores.append(BotScoreData(bot.name, count_moves[bot.name], count_collisions[bot.name], score))


bot_data = {}
for bot in bots:
    bot_data[bot.name] = bot

while len(robot_moves) > 0:
    move = robot_moves.popleft()
    bot_data[move[0]].process_move(move[1])

    rr.update_maze_characters(maze_data, bots)
    rr.print_maze(maze_data)
    sleep(seconds_between_turns - time() % seconds_between_turns)

rr.print_results(bot_scores)