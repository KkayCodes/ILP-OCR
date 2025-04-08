# Input and output file paths
input_file = "punnarchi/format_change.txt"  # Replace with your input file path
output_file = "punnarchi/format_changed.txt"  # Replace with your output file path

# Function to transform the format of the lines
def transform_format(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                # Strip any leading/trailing whitespace
                line = line.strip()
                
                # Skip empty lines
                if not line:
                    continue
                
                # Split the line by '=>'
                parts = line.split("=>")
                if len(parts) != 2:
                    print(f"Skipping invalid line: {line}")
                    continue

                compound_word = parts[0].strip()
                split_words = parts[1].strip()

                # Write the transformed line to the output file
                transformed_line = f"{split_words} => {compound_word}\n"
                outfile.write(transformed_line)

    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
transform_format(input_file, output_file)

print(f"Transformation complete. Check the output file: {output_file}")
