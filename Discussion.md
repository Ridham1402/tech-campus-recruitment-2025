# Discussion

## Solutions Considered

When I first approached the problem of extracting logs based on a specific date, I initially started with a **simple method**. The process involved reading each log entry, checking if the timestamp matched the given date, and then writing it to the output file. However, I soon realized that this approach was **incredibly slow**, especially when dealing with **large files**. 

The time it took to process each line individually was taking a toll on the overall performance, and it became clear that a more **efficient approach** was necessary. At this point, I thought of using a **list of lists**, where each list would act as a **buffer** to store a group of lines. While this method seemed like it could improve performance, I noticed that it didn’t significantly speed up the process. The root cause of the delay remained the same—the **constant reading and writing** of individual lines, which resulted in excessive I/O operations.

As I kept thinking through the problem, it became evident that the solution needed a way to efficiently **read large chunks** of data and **write them out in batches**, so that both operations—reading and writing—would not consume unnecessary **system resources**.

## Final Solution Summary

After experimenting with a few ideas, I decided to implement a **batch processing approach**. The key insight was to:

- **Read 10,000 lines at once** into a buffer,
- **Check each line** for the date,
- **Write all matching lines** in one go.

This allowed for much better control over **memory usage** and minimized the number of **read/write operations**. The batch size of **10,000 lines** was chosen after testing various sizes, and it seemed to strike the right balance between **memory usage** and **processing time**.

By processing in batches, the script could now:

- Read **10,000 lines at once**,
- Write them all at once,
- Then move on to the next batch.

This dramatically reduced the number of iterations, as the script no longer had to constantly switch between reading and writing operations. The result was a far more **efficient process**, saving both **time** and **memory**, especially when working with large files.

In the end, I chose this solution because it provided the most straightforward improvement without overcomplicating the logic. The batch processing approach also ensured that the **system’s memory** was not overwhelmed, as the script only needed to hold a **manageable number of lines** in memory at any given time.

## Steps to Run

1. **Clone the Repository**:
   
   First, clone the repository to your local machine to get access to the script and the required files. Add the large log file to this repository.
   
   ```bash
   git clone <repository_url>
   cd <repository_name>
   curl -L -o test_logs.log "https://limewire.com/d/90794bb3-6831-4e02-8a59-ffc7f3b8b2a3#X1xnzrH5s4H_DKEkT_dfBuUT1mFKZuj4cFWNoMJGX98"
   python3 src/extract_logs.py 2024-12-01
