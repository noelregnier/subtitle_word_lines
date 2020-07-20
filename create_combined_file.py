import argparse
import glob

#take the folder path
parser = argparse.ArgumentParser()
parser.add_argument("--path", help="Enter a path to the folder with .str files", required=True)
args = parser.parse_args()

path = args.path + "/*.srt"

#put all .str files names in the list
seasons = glob.glob(path)

#path to the combined file in the same folder
combined_file_path = "combined_file.txt"

#write all .srt files to the combined file
file_output = open(combined_file_path, "w")
for i in seasons:
    with open(i, 'r') as file:
        file_content = file.read()
        file_output.write(file_content)

file_output.close()
print("combined_file.txt is created in the current directory")





