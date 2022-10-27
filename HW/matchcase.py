if __name__ == "__main__": 
    n = "short"
    match n:
        case "long":
            print(f'its long') 
        case "short":
            print(f'short')
        case _:
            print(f'questionable length')