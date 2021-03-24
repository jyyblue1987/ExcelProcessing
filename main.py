import os

print("Start Program")

if not os.path.exists('files'):
    os.makedirs('files')

file = open("watersheds_supergrid_rc.csv", "r")

i = 0
while True:
    line = file.readline()
    if not line:
        break;

    if i == 0:
        i = i + 1
        continue

    array = line.split(",")

    id = array[0]
    
    wf = open('files/' + str(id) + ".txt", "a+")
    wf.write(array[1] + "," + array[2])
    wf.close()

    i = i + 1

    # print(line)

file.close()

# please release current payemnt

print("End Program")
