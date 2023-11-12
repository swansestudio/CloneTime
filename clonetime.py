from datetime import datetime
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')


def get_timestamp(path):
    return [
    os.path.getctime(path),
    os.path.getmtime(path),
    os.path.getatime(path),
]


def datetime_print(timestamps):
    printable = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d  %H:%M:%S') for ts in timestamps]

    print("{:<12} -> \x1b[33m{:<10}\x1b[0m".format('CREATED', printable[0]))
    print("{:<12} -> \x1b[33m{:<10}\x1b[0m".format('MODIFIED', printable[1]))
    print("{:<12} -> \x1b[33m{:<10}\x1b[0m".format('ACCESSED', printable[2]))
    print()



# If no arguments in commandline
if len(sys.argv) < 2:
    print("No files have been provided.")
    print("Please provide at least one file as an argument to display it\'s timestamp.")
    print("If you want to clone the timestamp from one file to another, please provide two files as arguments.")
    print("\x1b[32mUsage: clonetime.py <source_file> <destination_file>\x1b[0m")
    print("...Exiting !")
    sys.exit(1)


# Only show file name and creation date 
if len(sys.argv) == 2:
    source_path = sys.argv[1]
    source_timestamp = get_timestamp(source_path)
    print("\nFILE: \x1b[34m'{}'\x1b[0m\n".format(source_path))
    datetime_print(source_timestamp)
    print("You have provided one file.")
    print("If you want to clone the timestamp from one file to another, you need to provide two files as arguments.")
    print("\x1b[32mUsage: clonetime.py <source_file> <destination_file>\x1b[0m")
    print()
    

# Set file creation data
if len(sys.argv) == 3:

    source_path = sys.argv[1]
    destination_path = sys.argv[2]
    source_timestamp = get_timestamp(source_path)


    print("\nSOURCE FILE: \x1b[34m'{}'\x1b[0m\n".format(source_path))
    datetime_print(source_timestamp)

    print("DESTINATION FILE: \x1b[34m'{}'\x1b[0m\n".format(destination_path))

    proceed = input("Do you want to proceed with \x1b[31mclone date/time\x1b[0m from source to destination ? (y/n): ")
    if proceed.lower() == 'y':
       
        os.utime(destination_path, (source_timestamp[2], source_timestamp[1]))

        
        print("File date/time cloned.")

        destination_timestamp = get_timestamp(destination_path)


        print("\nDESTINATION FILE: \x1b[34m'{}'\x1b[0m\n".format(destination_path))
        datetime_print(destination_timestamp)

    else:
        print("Cancelled by user. Exiting.")
        sys.exit(0)



if len(sys.argv) > 3:
    print("Too many arguments provided. Only handling up to two arguments. Exiting.")
    sys.exit(1)
