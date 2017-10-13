# Wintner 2107

## 2

    + Select one goal that is not satisfied

    Goal 2: Deadlock cannot occur.

    + execution sequence

    Process1: flag1 = true;
    Context Switch
    Process2: flag2 = true;
    Process2: while (flag1); loop
    Context Switch
    Process1: while (flag2); loop


    + Select one goal that is satisfied
    Goal 1: Mutual exclusion is guaranteed

    + give a brief explanation
    For process1, when it access critical section, flag2 is false, flag 1 is true, so it is impossible for process2 execute Critical section.
    For process2, same reason. 