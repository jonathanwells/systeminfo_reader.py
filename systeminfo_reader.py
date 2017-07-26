
# Open a file
f1 = open("F:/list3.txt", "r+")

while True:

    line = f1.readline()
    line = line.rstrip('\n')
    if not line:
        break

    fo = open("F:/test/"+line, "r+")
    outfile = open("F:/test/"+line+"_summary.txt","w")
    print ("Name of the file: ", fo.name)



    while True:
        line = fo.readline()

        channel = line[0:7]
        if channel == "channel":
            print(line)
            outfile.write(line)

        hdd = line[0:5]
        if hdd == "###SD":
            print(line)
            outfile.write(line)

        rst = line[0:8]
        if rst == "  5 Real":
            print(line)
            outfile.write(line)

        smt = line[0:5]
        if smt == "SMART":
            print(line)
            outfile.write(line)

        mem = line[0:4]
        if mem == "Mem:":
            print(line)
            outfile.write(line)

        gpu = line[0:4]
        if gpu == "Mode":
            print(line)
            outfile.write(line)

        ttext = line[0:15]
        if ttext == "{subtitle-ttext":
            print(line)
            outfile.write(line)

        teletext = line[0:9]
        if teletext == "{teletext":
            print(line)
            outfile.write(line)

        gpio = line[0:5]
        if gpio == "{gpio":
            print(line)
            outfile.write(line)

        if not line:
            break


# Close opened file
    fo.close()
    outfile.close()

