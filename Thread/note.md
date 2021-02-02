### MultiThreading
 - Threads are components of a process.
 - There can be multiple threads in a process and
  they share the same memory space
  
Use cases for threading
- GUI programs use threading all the time to make applications responsive
- Programs that are IO bound or network bound, such web-scrapers
### MultiProcessing 
- Each process has its own memory space it uses to store the instructions
being run
#### Use Cases for Multiprocessing
- Multiprocessing outshines threading in cases where the program is CPU intensive 
and doesn’t have to do any IO or user interaction