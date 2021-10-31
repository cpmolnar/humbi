file1 = open("datasets\\Training_set\\train_pair.txt", "r")
file2 = open("datasets\\Training_set\\training_set.txt", "w")
for line in file1.read().split("\n"):
    line_split = line.split(" ")
    line_split[0] = 'image/' + line_split[0]
    line_split[1] = ('keypoints/' + line_split[1]).split(".")[0] + '.txt'
    write_line = ' '.join(line_split)
    file2.write(write_line + '\n')
print()