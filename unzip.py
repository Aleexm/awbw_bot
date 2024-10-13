import os
import gzip

def decompress_gzip(input_file, output_file):
    """
    Decompresses a gzip file and saves the decompressed content to another file.
    
    :param input_file: Path to the compressed gzip file.
    :param output_file: Path where the decompressed file will be saved.
    """
    with gzip.open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            f_out.write(f_in.read())
    print(f"File decompressed and saved to {output_file}")

def read_file(file_path):
    """
    Reads and returns the content of a file.
    
    :param file_path: Path to the file to be read.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

if __name__ == "__main__":
    # Directory containing the GZIP files
    input_directory = "C:\\Users\\alexm\\.aaprojects\\awbw\\replays"
    
    # Iterate over all files in the directory
    for filename in os.listdir(input_directory):
        input_gzip_file = os.path.join(input_directory, filename)
        
        # Construct the output filename for the decompressed content
        output_decompressed_file = os.path.join(input_directory, "unzipped", f"decoded_{os.path.splitext(filename)[0]}")

        # Step 1: Decompress the GZIP file
        decompress_gzip(input_gzip_file, output_decompressed_file)

        # Step 2: Read and print the decompressed content (optional)
        try:
            decompressed_content = read_file(output_decompressed_file)
            print(f"First 500 characters of {output_decompressed_file}:\n{decompressed_content[:500]}\n")
        except Exception as e:
            print(f"Error reading file {output_decompressed_file}: {e}")
