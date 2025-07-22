
import random
import webbrowser

difficulties = ['easy', 'medium']


url_file = 'setup/interview_problem_urls.txt'

def get_urls(url_file = url_file):
    with open(url_file, 'r') as file:
        urls = file.readlines()

    return [elem[:-1] for elem in urls if elem != '\n']

def get_problem(urls, difficulties):
    assert len(difficulties) > 0

    easy_start = urls.index('easy') + 1
    easy_end = urls.index('medium')
    medium_start = easy_end + 1
    medium_end = urls.index('hard')
    hard_start = medium_end + 1
    hard_end = len(urls)

    problem_candidates = []
    if 'easy' in difficulties:
        problem_candidates += urls[easy_start:easy_end]
    if 'medium' in difficulties:
        problem_candidates += urls[medium_start:medium_end]
    if 'hard' in difficulties:
        problem_candidates += urls[hard_start:hard_end]
    
    if len(problem_candidates) == 0:
        print(f"no more problems in: {difficulties}")
        return
    return random.choice(problem_candidates)

def add_to_attempted_file(chosen, file = 'setup/attempted_problems.txt'):
    with open(file, 'a') as save_file:
        save_file.write(chosen + '\n')

def remove_attempted_and_save_urls(urls, chosen, urls_file=url_file):
    saved_urls = [elem if elem != chosen else '' for elem in urls]
    saved_urls.insert(saved_urls.index('medium'), '')
    saved_urls.insert(saved_urls.index('hard'), '')
    with open(urls_file, 'w') as save_file:
        [save_file.write(elem + '\n') for elem in saved_urls]

urls = get_urls()
chosen_url = get_problem(urls, difficulties)
add_to_attempted_file(chosen_url)
remove_attempted_and_save_urls(urls, chosen_url)

webbrowser.open(chosen_url)