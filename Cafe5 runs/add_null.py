def main():
	with open("new_ortho.tsv","rt") as old_file:
		old_file_lines = old_file.readlines()

	for i in old_file_lines:
		print("(null)","\t",i)

main()
