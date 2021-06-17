import pickle

def main():
	with open('species_dict.pkl','rb') as handle:
		b = pickle.load(handle)

	print(b)

main()