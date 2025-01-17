import sys
import os
# import time

def extract_logs_by_date(input_file, date, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            batch_size = 10000  #batch of 10000 lines
            lines_buffer = []  # temporary buffer
            
            for line in infile:
                lines_buffer.append(line)
                
                if len(lines_buffer) >= batch_size:
                    for log_line in lines_buffer:
                        if log_line.startswith(date):
                            outfile.write(log_line)

                    lines_buffer = [] #buffer emptied
            

            if lines_buffer: #to process last batch which have less than 10000 lines
                for log_line in lines_buffer:
                    if log_line.startswith(date):
                        outfile.write(log_line)


            print(f"Logs for {date} have been successfully written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <YYYY-MM-DD>")
        sys.exit(1)


    date = sys.argv[1]

    # start_time = time.time()

    # input_file = 'test_logs.log'
    input_file = 'logs_2024.log'
    output_file = os.path.join('output', f"output_{date}.txt")
    
    # Extract logs for the given date
    extract_logs_by_date(input_file, date, output_file)

    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(f"Time taken to process the logs: {elapsed_time:.2f} seconds")
