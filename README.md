# CloneTime

CloneTime is a Python script that allows you to clone the timestamp from one file to another. It's a handy tool when you need to match the timestamps of two files for any reason, such as synchronization, backup verification, etc.

## Features

- Display the timestamp (creation, modification, and access time) of a file.
- Clone the timestamp from one file (source) to another file (destination).

## Usage

CloneTime can be used with one or two arguments:

1. **One argument (file):** If you provide one file as an argument, CloneTime will display the timestamp of that file.

    ```
    python clonetime.py <file>
    ```

2. **Two arguments (files):** If you provide two files as arguments, CloneTime will clone the timestamp from the first file (source) to the second file (destination).

    ```
    python clonetime.py <source_file> <destination_file>
    ```

## Examples

1. To display the timestamp of a file:

    ```
    python clonetime.py example.txt
    ```

2. To clone the timestamp from one file to another:

    ```
    python clonetime.py source.txt destination.txt
    ```

## Requirements

- Python 3.x
- OS module
- Sys module
- Datetime module

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/username/clonetime.git
    ```

2. Navigate to the cloned directory:

    ```
    cd clonetime
    ```

3. Run the script with the desired arguments:

    ```
    python clonetime.py <source_file> <destination_file>
    ```
