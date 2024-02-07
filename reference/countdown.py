import time


n = 10
while True:
    print(n)
    n -= 1
    time.sleep(1)
    if n == 0:
        print('Blast off! 🚀')
        break

print('The rocket has launched')


# TODO: Run this code to see what it does
# TODO: Read through this code and understand what's happening (n does not equal 10, n is being set to 10. Break is like you break out of the loop, like you break out of a bad habit)

# MARK: Playing with the code

# TODO: What happens if we remove this break statement? When will it end?
# TODO: What happens if we change this sleep to 0.5, 0.1?, no sleep? (See how the sleep is the most important part of this code)
# TODO: Let's add back the break statement, with the sleep still removed, what happens?
# TODO: Reset the code to normal
# TODO: What if we move n = 10 inside the while loop? What happens? Let's walk through the code to understand why.
# TODO: What happens if we move n = 10 to the end of the while loop? (What is this 'n' I haven't seen it)

# How the code inside the while loop, and if statement, is like files in a folder.

# -- Extra --
# TODO: Let's change the while condition to n > 0, remove the break statement. What happens?
# TODO: What is the value of n before the loop, and after the loop, what can we know about n when the code reaches the end of the loop?

# MARK: Tweaking the code

# TODO: How can we change this to countdown from 15 instead of 10?
# TODO: What if we want to start from 0 and launch on 10?
# TODO: Let's use a for loop instead of a while loop, to go from 0 to 10, Here's the code, but it prints everything instantly, how can we make it wait like before.
# TODO: How can we make it go from 10 to 0 (Hint: the step parameter)
# TODO: Compare the code with the while loop, which one has less code and is easier to understand?
# TODO: Let's make a countdown without using any loops.
# TODO: What if we suddenly need to adjust the countdown to start from 100, which one is easier to change?

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# print('Blast off! 🚀')

# TODO: Let's say we need to start the engines 5 seconds before the launch, how can we print 'engines started' at the right time.
# TODO: What if we don't use the for loop parameter, and use our own variable instead.

# MARK: Dojo

# TODO: Write your own countdown code.
# TODO: Write it using the other way (while or for loop)
# TODO: Count up or count down.


# MARK: Applying the code
# TODO: We could make a timer that counts the seconds until we stop it.
# NOTE: This is a good detour on how computers keep track of time, and the use of time.time(). Computers don't know what time it is, they just know how many seconds have passed since a certain date.


# MARK: Future Ideas
# We could use a spinner for a timer program, and play with the different spinner styles.
# We can make a rock, paper, scissors game where we play against the computer, and we can time how long it takes us to make a choice, and we lose if we took too long.


# Play with the different ways you could count down or up using a while loop, for loop, with and without the variables, and no loops.
# Show how one way is better than others for certain needs, like if suddenly we need to adjust the next countdown from 10 to 100.
