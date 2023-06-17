# """
# Script python utiliser pour mettre à jour toutes les tables à chaque push
# """


# import os 
# from test_build_table import process_files
# import shutil
# from grewpy import Request, Corpus, set_config



# def get_files_in_directory(directory):
#     files = []
#     for file_name in os.listdir(directory):
#         file_path = os.path.join(directory, file_name)
#         if os.path.isfile(file_path):
#             files.append(file_name)
#     return files


# def get_subdirectories_paths_with_name(directory):
#     subdirectories_paths = []
#     for entry in os.scandir(directory):
#         if entry.is_dir():
#             subdirectories_paths.append((entry.name,entry.path))
#     return subdirectories_paths

# def get_subdirectories_paths(directory):
#     subdirectories_paths = []
#     for entry in os.scandir(directory):
#         if entry.is_dir():
#             subdirectories_paths.append((entry.path))
#     return subdirectories_paths

# def find_file_by_name(directory, filename):
#     for root, dirs, files in os.walk(directory):
#         if filename in files:
#             return os.path.join(root, filename)
#     return None


# def replace_file(directory,filename,actual_table_path):
#     file_path = find_file_by_name(directory, filename)
#     file_path_r = str(file_path).split("/")
#     new_file_path = f"{'/'.join(file_path_r[:-1])}"
#     print(new_file_path)
#     os.rename(actual_table_path,file_path)

# if __name__ == "__main__":
#     directory_path = "."
#     subdirectories_list = get_subdirectories_paths_with_name(directory_path)

#     get_files_per_language = {}

#     for language,folder in subdirectories_list:
#         if language != "__pycache__":
#             subfolder = get_subdirectories_paths_with_name(folder)
#             get_files_per_language[language]=subfolder


#     #print(get_files_per_language)

#     get_tuple_request_table = {}
#     liste_files = []
#     for key,value in get_files_per_language.items():
#         for name,path in value:
#             if name.endswith("table_json"):
#                 corpora_information = name
#             if name.endswith("request_json"):
#                 liste_files = get_files_in_directory(path)
#         get_tuple_request_table[key]=(corpora_information,liste_files)

#     get_all_table=[]

#     for key,value in get_tuple_request_table.items():
#         corpora_inf = value[0]
#         for element in value[1]:
#             result = process_files(f"{key}/{key}_request_json/{element}",f"{key}/{corpora_inf}/sud_{key}.json")
#             real_name = element.split("_")
#             new = "_".join(real_name[1:])
#             new_name = f"table_{new}"
#             get_all_table.append(new_name)
#             with open(f"{key}/{key}_table_json/{new_name}",'w') as output:
#                 output.write(str(result))

#         for element in get_all_table:
#             directory = "../static/docs/"
#             filename = element
#             actual_table_path = f"{key}/{key}_table_json/{element}"
#             print(f"directory = {directory}\n filename = {filename}\n actual_table_path = {actual_table_path}")
#             replace_file("../static/docs/","table_output_french_subj.json","french/french_table_json/table_output_french_subj.json")

print("hello")