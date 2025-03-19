import openai
from llmastar.pather import AStar, LLMAStar
openai.api_key = "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"

# # -----------------------------------------------
# # Example 1: Small Grid with No Obstacles
# # -----------------------------------------------
# query1 = {
#     "start": [0, 0],
#     "goal": [5, 5],
#     "size": [6, 6],
#     "horizontal_barriers": [],
#     "vertical_barriers": [],
#     "range_x": [0, 6],
#     "range_y": [0, 6]
# }
# astar1 = AStar().searching(query=query1, filepath='astar1.png')
# llm1 = LLMAStar(llm='gpt', prompt='standard').searching(query=query1, filepath='llm1.png')
# print("Example 1 completed: 'astar1.png' and 'llm1.png' have been saved.")

# # -----------------------------------------------
# # Example 2: Medium Grid with Single Barriers
# # -----------------------------------------------
# query2 = {
#     "start": [2, 2],
#     "goal": [8, 8],
#     "size": [10, 10],
#     "horizontal_barriers": [[4, 1, 7]],  # Barrier on row 4 from column 1 to 7.
#     "vertical_barriers": [[6, 3, 5]],      # Barrier on column 6 from row 3 to 5.
#     "range_x": [0, 10],
#     "range_y": [0, 10]
# }
# astar2 = AStar().searching(query=query2, filepath='astar2.png')
# llm2 = LLMAStar(llm='gpt', prompt='standard').searching(query=query2, filepath='llm2.png')
# print("Example 2 completed: 'astar2.png' and 'llm2.png' have been saved.")

# -----------------------------------------------
# Example 3: Large Grid with Multiple Obstacles
# -----------------------------------------------
query3 = {
    "start": [3, 3],
    "goal": [45, 25],
    "size": [50, 30],
    "horizontal_barriers": [
        [10, 5, 40],  # Barrier on row 10 from column 5 to 40.
        [20, 10, 30]  # Barrier on row 20 from column 10 to 30.
    ],
    "vertical_barriers": [
        [25, 5, 15],  # Barrier on column 25 from row 5 to 15.
        [35, 20, 28]  # Barrier on column 35 from row 20 to 28.
    ],
    "range_x": [0, 50],
    "range_y": [0, 30]
}
astar3 = AStar().searching(query=query3, filepath='astar3.png')
llm3 = LLMAStar(llm='gpt', prompt='standard').searching(query=query3, filepath='llm3.png')
print("Example 3 completed: 'astar3.png' and 'llm3.png' have been saved.")