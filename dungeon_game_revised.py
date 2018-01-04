import random



def create_matrix(column, row):

	room = []
	idx =0
	inner_matrix = []

	while idx < column:
		for r in range(row):
			inner_matrix.append('__')
		room.append(inner_matrix)
		inner_matrix = []
		idx += 1

	return room


def set_initial_location(room):

	player_init_col = random.randint(0,len(room) -1)
	player_init_row = random.randint(0,len(room) -1)
	player_col_row = [player_init_col, player_init_row]

	return player_col_row


def get_monster(room):

	monster_row = random.randint(0,len(room)-1)
	monster_col = random.randint(0,len(room)-1)
	
	return monster_col, monster_row


def get_door(room):
	
	door_row = random.randint(0,len(room)-1)
	door_col = random.randint(0,len(room)-1)
	
	return door_col, door_row


def start_game():

	dungeon_room = create_matrix(6, 6)
	player_col_row = set_initial_location(dungeon_room)
	monster_col_row = get_monster(dungeon_room)
	door_col_row = get_door(dungeon_room)

	return player_col_row, monster_col_row, door_col_row, dungeon_room


def resume_game(room):

	print('\n \n')
	print(room)
	print( '\n \n')
	user_input = input("""What do you want to do?: \n [1] Move Up \n [2] Move Down
 [3] Move Right \n [4] Move Left \n """)

	return user_input


def update_board(room, num1, num2):

	room[num1][num2] = 'p'
	new_player_pos = [num1, num2]

	return room, new_player_pos


def delete_p(room, num1):

	idx = room[num1].index('p')
	room[num1].remove('p')
	room[num1].insert(idx, '__')

	return room

def player_moves(player_col_row, monster_col_row, door_col_row, dungeon_room, user_input):
	if user_input == '1':
		if player_col_row[0] == 0:
			print("\n You're about to fall! Try another move.\n")
			user_input = resume_game(dungeon_room)
		else:
			delete_p_board = delete_p(dungeon_room, player_col_row[0])
			player_col_row[0] -= 1
			revised_board_info = update_board(delete_p_board, player_col_row[0], player_col_row[1])
			dungeon_room = revised_board_info[0]
			player_col_row[0] = revised_board_info[1][0]
			player_col_row[1] = revised_board_info[1][1]
	elif user_input == '2':
		if player_col_row[0] == len(dungeon_room) - 1:
			print("\n You're about to fall! Try another move. \n")
			user_input = resume_game(dungeon_room)
		else:
			delete_p_board = delete_p(dungeon_room, player_col_row[0])
			player_col_row[0] += 1
			revised_board_info = update_board(delete_p_board, player_col_row[0], player_col_row[1])
			dungeon_room = revised_board_info[0]
			player_col_row[0] = revised_board_info[1][0]
			player_col_row[1] = revised_board_info[1][1]
	elif user_input == '3':
		if player_col_row[1] == len(dungeon_room[0]) - 1:
			print("\n You're about to fall! Try another move. \n")
			user_input = resume_game(dungeon_room)
		else:
			delete_p_board = delete_p(dungeon_room, player_col_row[0])
			player_col_row[1] += 1
			revised_board_info= update_board(delete_p_board, player_col_row[0], player_col_row[1])
			dungeon_room1 = revised_board_info[0]
			player_col_row[0] = revised_board_info[1][0]
			player_col_row[1] = revised_board_info[1][1]
	elif user_input == '4':
		if player_col_row[1] == 0:
			print("\nYou're about to fall! Try another move. \n")
			user_input = resume_game(dungeon_room)
		else:
			delete_p_board = delete_p(dungeon_room, player_col_row[0])
			player_col_row[1] -= 1
			revised_board_info = update_board(delete_p_board, player_col_row[0], player_col_row[1])
			dungeon_room = revised_board_info[0]
			player_col_row[0] = revised_board_info[1][0]
			player_col_row[1] = revised_board_info[1][1]

	return player_col_row, monster_col_row, door_col_row, dungeon_room


play_again = True

while play_again:
	starter_kit = start_game()
	player_col_row = starter_kit[0]
	monster_col_row = starter_kit[1]
	door_col_row = starter_kit[2]
	dungeon_room_s = starter_kit[3]
	dungeon_room_s[door_col_row[0]][door_col_row[1]] = 'd'
	dungeon_room_s[monster_col_row[0]][monster_col_row[1]] = 'm'
	dungeon_room_s[player_col_row[0]][player_col_row[1]] = 'p'

	user_input= resume_game(dungeon_room_s)

	game_over = False

	while not game_over:
		play_kit = player_moves(player_col_row, monster_col_row, door_col_row, dungeon_room_s, user_input) 
		player_col_row = play_kit[0]
		monster_col_row = play_kit[1]
		door_col_row = play_kit[2]
		dungeon_room = play_kit[3]
		if player_col_row[0] == monster_col_row[0] and player_col_row[1] == monster_col_row[1]:
			user_input = input("\n You touched the monster! Game over. Play again? Y/N \n ")
			if user_input.lower() != 'n':
				game_over = True
				play_again = True
			else:
				game_over = True
				play_again = False

		elif player_col_row[0] == door_col_row[0] and player_col_row[1]== door_col_row[1]:
			user_input = input("You won! You avoided the monster. Play again? Y/N")
			if user_input.lower() != 'n':
				game_over = True
				play_again = True
			else:
				game_over = True
				play_again = False
		else:
			user_input = resume_game(dungeon_room)














