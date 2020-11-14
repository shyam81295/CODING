import requests
import json


def leetcode_file_creator(leetcode_problem_no):
    # Leetcode difficulty mapping to string
    difficulty_map = {1: "easy", 2: "medium", 3: "hard"}

    # Leetcode API URL to get json of problems on algorithms categories
    ALGORITHMS_ENDPOINT_URL = "https://leetcode.com/api/problems/algorithms/"

    # Load JSON from API
    algorithms_problems_json = requests.get(ALGORITHMS_ENDPOINT_URL).content
    algorithms_problems_json = json.loads(algorithms_problems_json)

    # List to store question_title_slug
    links = []
    for child in algorithms_problems_json["stat_status_pairs"]:
        # Only process free problems
        if not child["paid_only"]:
            question__title_slug = child["stat"]["question__title_slug"]
            question__article__slug = child["stat"]["question__article__slug"]
            question__title = child["stat"]["question__title"]
            frontend_question_id = child["stat"]["frontend_question_id"]
            difficulty = child["difficulty"]["level"]
            links.append((question__title_slug, difficulty,
                          frontend_question_id, question__title,
                          question__article__slug))

    # Sort by difficulty follwed by problem id in ascending order
    links = sorted(links, key=lambda x: (x[2]))

    _, diff, ques_id, _, ques__title = links[leetcode_problem_no-1]
    fname = f"{difficulty_map[diff]}_{ques_id}_{ques__title}"
    print(fname)


leetcode_problem_no = int(input())

leetcode_file_creator(leetcode_problem_no)
