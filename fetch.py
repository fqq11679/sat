import argparse
import os      

def main(args):
    filenames = []
    for filename in os.listdir(args.dir_path):
        if '.wcnf' in filename:
            filenames.append(filename)
    samples = []
    for i, filename in enumerate(filenames):
        if i >= args.samples:
            break
        samples.append(filename)
    print(samples)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir_path', type=str)
    parser.add_argument('--samples', type=int)
    args = parser.parse_args()
    main(args)
