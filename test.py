from tools.tavily_tool import tavily_search
# res = tavily_search("What are the best tourist attractions in Paris?")
# print(res)
 
from tools.flight_tool import search_flights

res = search_flights("plan a 7 days japan trip from bangladesh")
print(res)
