from collections import deque

def check_pali(word):
    d = deque(word)
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True

def main():
    #add code here
    word = 'tacocat'
    print(check_pali(word))
    return

if __name__ == "__main__":
    main()