import requests
import json

# class GetPrograms:
#     def __init__(self):
#         pass

#     def get_programs(self):
#         URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

#         response = requests.get(URL)
#         return response.content

#     def program_school(self):
#     # we use the JSON library to parse the API response into nicely formatted JSON
#         programs_list = []
#         programs = json.loads(self.get_programs())
#         for program in programs:
#             programs_list.append(program["agency"])

#         return programs_list

# programs = GetPrograms()
# programs_schools = programs.program_school()

# for school in set(programs_schools):
#     print(school)

class GetPrograms:
    def __init__(self):
        pass

    #  get json data from api
    def get_programs(self):
        # API endpoint URL
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.content

    # convert json into python, select item with key 'agency'
    def program_school(self):
        programs_list = []
        # programs = json.loads(self.get_programs())
        programs = self.load_json(self.get_programs())
        for program in programs:
            programs_list.append(program['agency'])

        return programs_list

    def load_json(self, py_obj):
        return json.loads(py_obj)

# programs = GetPrograms().get_programs()
# print(programs)
program_schools = GetPrograms().program_school()
print(program_schools[:4])