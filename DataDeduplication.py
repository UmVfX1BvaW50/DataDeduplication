import sys

def DataDeduplication(inputdir, outputdir):
    with open(inputdir,'r+', encoding='utf-8') as Ifile:
        lines = Ifile.readlines()

    deduplicated_lines = []
    count = 1
    for i in range(len(lines) - 1):
        if lines[i] == lines[i + 1]:
            count += 1
        else:
            if count > 1:
                deduplicated_lines.append(f'{lines[i].strip()} ({count})')
            else:
                deduplicated_lines.append(lines[i].strip())
            count = 1

    if count > 1:
        deduplicated_lines.append(f'{lines[-1].strip()} ({count})')
    else:
        deduplicated_lines.append(lines[-1].strip())

    with open(outputdir, 'w') as f:
        f.write('\n'.join(deduplicated_lines))

    print(f'Deduplicated lines written to {outputdir}.')
    print('Deduplicated lines:')
    print('\n'.join(deduplicated_lines))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python DataDeduplication.py input_file output_file')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        DataDeduplication(input_file, output_file)