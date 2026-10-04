from tools.tavily_tool import tavily_search
# res = tavily_search("What are the best tourist attractions in Paris?")
# print(res)

from backend import run_travel_agent
 
from tools.flight_tool import search_flights

res = search_flights("plan a 7 days japan trip from bangladesh")
print(res)

user_input = input("enter: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)
print(response["answer"])
