import sys

TV_SHOWS = {
  "The Big Bang Theory": [17, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24],
  "Sex and The City": [12, 18, 18, 18, 8, 20],
}

NUM_OF_TV_SHOWS = len(TV_SHOWS)

tv_show_name = ""
tv_show_data = {}
season_number = 1
episode_number = 1

def print_final_result():
  print tv_show_name, 'season', season_number, 'episode', episode_number

def tv_show_retry():
  #TODO: remove this message?
  print "Pick a number between 1 and", NUM_OF_TV_SHOWS, '!'
  pick_tv_show()

def pick_tv_show():
  print "Pick a TV show:"
  #print '0 - random'
  for index, item in enumerate(TV_SHOWS):
    print index + 1, '-', item

  input = raw_input()
  try:
    tv_show_id = int(input)
    if tv_show_id < 1 or tv_show_id > NUM_OF_TV_SHOWS:
      tv_show_retry()
    else:
      global tv_show_data, tv_show_name
      tv_show_data = TV_SHOWS.values()[tv_show_id - 1]
      tv_show_name = TV_SHOWS.keys()[tv_show_id - 1]

  except ValueError:
    tv_show_retry()

def pick_season():
  print "Pick a season 1 -", len(tv_show_data)
  input = raw_input()
  try:
    global season_number
    season_number = int(input) - 1
    if season_number < 0 or season_number > len(tv_show_data) - 1:
      pick_season()
  except ValueError:
    pick_season()

def pick_episode():
  number_of_episodes = tv_show_data[season_number]
  print "Pick an episode number 1 -", tv_show_data[season_number]
  input = raw_input()
  try:
    global episode_number
    episode_number = int(input)
    if episode_number < 1 or episode_number > number_of_episodes:
      pick_episode()
  except ValueError:
    pick_episode()

pick_tv_show()
pick_season()
pick_episode()
print_final_result()

#TODO: random every step - TV show, season, episode, all of it