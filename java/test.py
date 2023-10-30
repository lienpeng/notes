def split_ip():
    with open("name.txt", 'r') as f:
        for lines in f:
            line = lines.strip()
            print(line)
            

if __name__ == '__main__':
    # get_pod_len()
    split_ip()
    # get_ip_pod()
    # result = get_map()
    # # bads = get_bad_ip()
    # balance(result,"")