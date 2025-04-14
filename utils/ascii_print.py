def get_lines(filepath: str) -> list:
    """Reads ascii art lines from a file at filepath and returns a list of lines"""
    temp = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            temp.append(line.strip("\n"))
            
    return temp
