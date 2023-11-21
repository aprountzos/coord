import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        in_file = open(sys.argv[1], "r")
        out_file = open("out_" + sys.argv[1],"a")
        line_count = 1
        for line in in_file.readlines():
            out_line = "point " + line.strip() + "\n-text " + line.strip() + " 1 " + str(line_count) + "\n"
            line_count += 1
            out_file.write(out_line)
        in_file.close()
        out_file.close()
	 