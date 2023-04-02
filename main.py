def main_run():

    files = ['1.txt', '2.txt', '3.txt']
    file_content = []

    for file in files:
        with open(file, 'rt', encoding='utf-8') as f:
            content = f.readlines()
            file_content.append((file, len(content), content))

    file_content.sort(key=lambda x: x[1])

    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in file_content:
            f.write(file[0] + '\n')
            f.write(str(file[1]) + '\n')
            for line in file[2]:
                f.write(line)
            f.write('\n')


if __name__ == '__main__':
    main_run()
