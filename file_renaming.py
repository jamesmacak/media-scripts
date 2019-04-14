import os, re

def get_file_information():
	title = input("Show title: ")
	season = input("Season (##): ")
	other_details = input("Other details: ")
	file_extension = input("File extension: ")
	separator = input("Separator: ")
	content_path = input("Content path: ")
	return title, season, other_details, file_extension, content_path, separator

def get_episode_names():
	with open("episode_names.txt") as f:
		episode_names = f.readlines()
		episode_names = [i.strip() for i in episode_names]
	return episode_names

def construct_new_filename(title, season, episode, other_details, file_extension, separator, episode_number):
	if int(episode_number) < 10:
		constructed_filename = (title + separator + "S" + season + "E0" + episode_number + separator + episode + separator + other_details + file_extension)
	else:
		constructed_filename = (title + separator + "S" + season + "E" + episode_number + separator + episode + separator + other_details + file_extension)
	return constructed_filename

def rename_files(new_filenames, content_path):
	new_filenames = new_filenames
	i = 0
	for old_filename in os.listdir(content_path):
		#print(old_filename + " | " + new_filenames[i])
		old_filename = content_path + old_filename
		new_filename = content_path + new_filenames[i]
		os.rename(old_filename, new_filename)
		print(new_filename)
		i += 1

def main():
	episodes = get_episode_names()
	
	title, season, other_details, file_extension, content_path, separator = get_file_information()
	
	new_filenames = []
	episode_number = 1
	for episode in episodes:
		str_episode_number = str(episode_number)
		new_filenames.append(construct_new_filename(title, season, episode, other_details, file_extension, separator, str_episode_number))
		episode_number += 1

	rename_files(new_filenames, content_path)

main()