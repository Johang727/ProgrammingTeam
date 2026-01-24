import sys

def solve():
    # Read N, the number of participants 
    try:
        n_line = sys.stdin.readline()
        if not n_line:
            return  # Handle empty input
        N = int(n_line.strip())
    except EOFError:
        return
    except ValueError:
        return

    times = []
    # Read the N participant times 
    for _ in range(N):
        try:
            line = sys.stdin.readline()
            if not line:
                break
            times.append(int(line.strip()))
        except (EOFError, ValueError):
            break
            
    if len(times) != N:
        return # Input mismatch

    # 1. Sort the times
    times.sort()

    # 2. Calculate the total sum
    total_sum = sum(times)

    # 3. Get the latest time (t_N)
    # (using 0-based indexing, t_N is at index N-1)
    t_N = times[N - 1]

    # 4. Initialize min_total_wait to a large value
    # We can use the wait time if everyone goes on one bus
    # (equivalent to k=N, which isn't in our loop but is a valid scenario)
    # W(N) = (N * t_N) - total_sum
    min_total_wait = (N * t_N) - total_sum 

    # 5. Loop k from 1 to N-1
    # k represents the number of people on the first bus
    for k in range(1, N):
        # Get the k-th time (t_k)
        # (using 0-based indexing, t_k is at index k-1)
        t_k = times[k - 1]

        # Calculate wait time for this split using the simplified formula
        # W(k) = (k * t_k) + ((N - k) * t_N) - total_sum
        current_wait = (k * t_k) + ((N - k) * t_N) - total_sum

        # 6. Update the minimum
        if current_wait < min_total_wait:
            min_total_wait = current_wait

    # 7. Print the smallest possible total waiting time 
    print(min_total_wait)

if __name__ == "__main__":
    solve()