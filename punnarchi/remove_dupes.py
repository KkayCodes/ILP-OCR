def remove_duplicates_from_text_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    unique_lines = []
    seen = set()

    for line in lines:
        stripped_line = line.strip()  
        if stripped_line and stripped_line not in seen:  
            unique_lines.append(line)
            seen.add(stripped_line)

    with open(output_file, 'w') as file:
        file.writelines(unique_lines)

    print(f"Duplicates removed. The output is saved in: {output_file}")

input_file = 'punnarchi/punarchi_dataset.txt'
output_file = 'punnarchi/dupes_removed_pun.txt'

remove_duplicates_from_text_file(input_file, output_file)
