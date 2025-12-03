def parse_disk_map(disk_map):
    """Parses the dense format of the disk map into a detailed list."""
    disk = []
    current_is_file = True
    for length in map(int, disk_map):
        if current_is_file:
            disk.extend([len(disk)] * length)  # Add file blocks with file ID
        else:
            disk.extend([None] * length)  # Add free space blocks
        current_is_file = not current_is_file

    return disk

def compact_disk(disk):
    """Compacts the disk by moving file blocks to the leftmost free spaces."""
    compacted = []
    file_blocks = [block for block in disk if block is not None]
    compacted.extend(file_blocks)
    compacted.extend([None] * (len(disk) - len(file_blocks)))

    return compacted

def calculate_checksum(compacted_disk):
    """Calculates the checksum for the compacted disk layout."""
    checksum = 0
    for pos, file_id in enumerate(compacted_disk):
        if file_id is not None:
            checksum += pos * file_id
    return checksum

def process_disk_map(disk_map):
    """Processes the disk map to calculate the checksum after compaction."""
    disk = parse_disk_map(disk_map)
    compacted_disk = compact_disk(disk)
    return calculate_checksum(compacted_disk)
file = "example.txt"
print("using input:", file)

with open(file, 'r') as file:
    content = file.read()
# Input disk map (replace with your puzzle input)
disk_map = content
checksum = process_disk_map(disk_map)
print("Checksum:", checksum)
