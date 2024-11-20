from queue import Queue

def FIFO(pages, n, capacity):
    s = set()
    indexes = Queue()
    page_faults = 0
    output = []

    output.append("Step | Page | Memory         | Page Fault")
    output.append("-----|------|---------------|-----------")

    for i in range(n):
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])
                page_faults += 1
                indexes.put(pages[i])
                output.append(f"{i+1:>4} | {pages[i]:>4} | {str(list(s)): <14} | Yes")
            else:
                output.append(f"{i+1:>4} | {pages[i]:>4} | {str(list(s)): <14} | No")
        else:
            if pages[i] not in s:
                val = indexes.queue[0]
                indexes.get()
                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
                page_faults += 1
                output.append(f"{i+1:>4} | {pages[i]:>4} | {str(list(s)): <14} | Yes")
            else:
                output.append(f"{i+1:>4} | {pages[i]:>4} | {str(list(s)): <14} | No")

    output.append(f"Total Page Faults: {page_faults}")
    return output
    
def LRU(pages, n, capacity):
    s = set()
    indexes = {}
    page_faults = 0
    output = []

    output.append("Step | Page | Memory         | Page Fault")
    output.append("-----|------|---------------|-----------")

    for i in range(n):
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])
                page_faults += 1
                output.append(f"{i+1:>4} | {pages[i]:>4} | {str(list(s)): <14} | Yes")
            else:
                output.append(f"{i+1:>4} | {pages[i]:>4} | {str(list(s)): <14} | No")
            indexes[pages[i]] = i
        else:
            if pages[i] not in s:
                lru = float('inf')
                for page in s:
                    if indexes[page] < lru:
                        lru = indexes[page]
                        val = page
                s.remove(val)
                s.add(pages[i])
                page_faults += 1
                output.append(f"{i+1:>4} | {pages[i]:>4} | {str(list(s)): <14} | Yes")
            else:
                output.append(f"{i+1:>4} | {pages[i]:>4} | {str(list(s)): <14} | No")
            indexes[pages[i]] = i

    output.append(f"Total Page Faults: {page_faults}")
    return output

if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n = len(pages)
    capacity = 4

    # FIFO results
    fifo_result = FIFO(pages, n, capacity)
    for line in fifo_result:
        print(line)

    print(" ")

    # LRU results
    lru_result = LRU(pages, n, capacity)
    for line in lru_result:
        print(line)
