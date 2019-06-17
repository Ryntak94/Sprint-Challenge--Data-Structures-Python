Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
    O(1)
2. What is the space complexity of your ring buffer's `append` function?
    O(1)
3. What is the runtime complexity of your ring buffer's `get` method?
    O(n)
4. What is the space complexity of your ring buffer's `get` method?
    O(n)

5. What is the runtime complexity of the provided code in `names.py`?
    O(n**2)
6. What is the space complexity of the provided code in `names.py`?
    O(n**2)
7. What is the runtime complexity of your optimized code in `names.py`?
    worst case: O(n)
    best case: O(log n)
8. What is the space complexity of your optimized code in `names.py`?
    O(n)

    If you run my solution vs the original code you will see an additional 28 names on the list.
    However I have checked to make sure that the list does include the 64 names. If you comment
    out my code and uncomment the code that is commented out currently within names you will see
    that my solution and the original solution have 64 names in common, which would be the entirety of the original solution. The reason for this is the first solution doesn't take into account duplicates within the same list and my solution does. I figured that finding
    duplicates within the same list would be a good idea since you can't tell if two people with
    the same name are the same or different people, and it seems that the instructions assume
    the same name occurring twice is the same person.
