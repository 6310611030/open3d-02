def filter(input_file, output_file):
    with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
        # Copy the first 14 lines unchanged
        for _ in range(14):
            line = f_input.readline()
            f_output.write(line)

        # Copy lines with the condition
        for line in f_input:
            parts = line.split()  # Split the line into parts
            if len(parts) == 9:  # Check if there are 9 parts
                _, _, _, x2, y2, z2, _, _, _ = parts  # Extract values
                # Check if x2 and y2 are in -0.2 to 0.2 and z2 are greater than 0.9
                if -0.2 <= float(x2) <= 0.2 and -0.2 <= float(y2) <= 0.2 and float(z2) >= 0.9:
                    f_output.write(line)


input = 'C:\\Users\\Asus\\Desktop\\cropped_1_normal.ply' 
output = 'C:\\Users\\Asus\\Desktop\\filtered_cropped_1.ply'  

filter(input, output)