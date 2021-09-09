#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_dir = dir(hidden_4)
    not_this = "__"
    for i in range(0, len(all_dir)):
        if not_this not in all_dir[i]:
            print(all_dir[i])
